from datetime import datetime as dt
from init_db import HousingDatabase


class LeasingDAO(HousingDatabase):

    def get_leases(self):
        """ Select all leases in the lease table. """

        leases = []
        try:
            self.connect_to_db()

            # SQL call to database Selecting all rows including their unique rowid.
            self.curs.execute("SELECT rowid, * FROM tb_leases")
            rows = self.curs.fetchall()

            # Convert each row to a dictionary and append to list.
            for i in rows:
                lease = {}
                lease['rowid'] = i['rowid']
                lease['resident_id'] = i['resident_id']
                lease['unit_id'] = i['unit_id']
                lease['lease_start'] = i['lease_start']
                lease['lease_end'] = i['lease_end']
                lease['created_date'] = i['created_date']
                leases.append(lease)

        # General error handling
        except Exception as e:
            print('Error getting leases: ', e)
            leases = []

        finally:
            self.conn.close()

        return leases
    
    def get_lease_by_id(self, id: int):
        """ Select lease by unique rowid. """

        lease = {}
        try:

            self.connect_to_db()

            # Select lease by unique rowid and parse into dictionary. 
            self.curs.execute("SELECT rowid, * FROM tb_leases WHERE rowid = ?", (id,))
            row = self.curs.fetchone()
            lease['rowid'] = row['rowid']
            lease['resident_id'] = row['resident_id']
            lease['unit_id'] = row['unit_id']
            lease['lease_start'] = row['lease_start']
            lease['lease_end'] = row['lease_end']
            lease['created_date'] = row['created_date']

        except Exception as e:
            print('Unable to get lease id ', id, e)
            lease = {}

        finally:
            self.conn.close()

        return lease
    
    def add_lease(self, lease: dict):
        """ Insert a new lease into lease table. 
        Params:
            lease: {'resident_id': int, 'unit_id': int, 'lease_start': str mm/dd/yyyy, 'lease_end': str mm/dd/yyyy}
        """

        new_lease = {}
        try:

            self.connect_to_db()

            # Insert the new lease into the table
            self.curs.execute("INSERT INTO tb_leases VALUES (?,?,?,?,?)", (lease['resident_id'],
                         lease['unit_id'], dt.strptime(lease['lease_start'], '%m/%d/%Y').date(),
                         dt.strptime(lease['lease_end'], '%m/%d/%Y').date(), dt.now())
                         )
            self.conn.commit()

            # Get the last added lease
            new_lease = self.get_lease_by_id(self.curs.lastrowid)
        except Exception as e:
            self.conn.rollback()
            print('LEASE WAS NOT ADDED: ', e)

        finally:
            self.conn.close()

        return new_lease
    
    def delete_lease(self, id: int):
        """ Delete the lease based on the given id. """

        # Get the data for the deleted lease 
        deleted_lease = self.get_lease_by_id(id)

        try:

            self.connect_to_db()

            # Delete the lease
            self.curs.execute("DELETE FROM tb_leases WHERE rowid = ?", (id,))
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print('Error deleting lease: ', e)

        finally:
            self.conn.close()

        return deleted_lease
    
    def get_rent_roll(self, start_date: str, end_date: str):
        """ Get the leases and rent owed over a period of time. 
            start_date: yyyy-mm-dd
            end_date: yyyy-mm-dd"""
        rent = []
        try:

            self.connect_to_db()

            # Join 4 tables to create a rent roll based on the date arguments
            self.curs.execute("""SELECT l.rowid, c.complex_name, h.unit_number, r.first_name, r.last_name, h.rent_price 
                        FROM tb_leases l
                        JOIN tb_student_housing_units h ON
                        l.unit_id = h.rowid
                        JOIN tb_resident_info r ON
                        l.resident_id = r.resident_id
                        JOIN tb_housing_complexes c ON
                        h.complex_id = c.rowid
                        WHERE l.lease_start BETWEEN ? AND ?
            """, (start_date, end_date))

            # Parse the rows and convert to a dictionary
            rows = self.curs.fetchall()
            for i in rows:
                lease = {}
                lease['lease_id'] = i['rowid']
                lease['complex_name'] = i['complex_name']
                lease['apartment'] = i['unit_number']
                lease['resident_name'] = i['first_name'] + ' ' + i['last_name']
                lease['rent_price'] = i['rent_price']
                rent.append(lease)
                
        except Exception as e:
            rent = []
            print('Unable to get rent roll. ', e)

        finally:
            self.conn.close()

        return rent

    def get_total_rent(self, start_date: str, end_date: str):
        """ Get the total rent owed over a period of time. 
            start_date: yyyy-mm-dd
            end_date: yyyy-mm-dd
        """
        
        rent = 0

        try:

            self.connect_to_db()

            # Join lease table with housing table to find sum of rent over a given time period. 
            self.curs.execute("""SELECT SUM (h.rent_price) 
                        FROM tb_student_housing_units h
                        JOIN tb_leases l ON
                        l.unit_id = h.rowid
                        WHERE l.lease_start BETWEEN ? AND ?
            """, (start_date, end_date))

            # Returns a tuple, get the first index which is the sum
            rent = self.curs.fetchone()[0]

        except Exception as e:
            print('Unable to calculate sum of rent: ', e)
        finally:
            self.conn.close()

        return rent

    def get_capacity(self, start_date: str, end_date: str):
        """ Get the fill capacity numbers between given lease dates.
            start_date: yyyy-mm-dd
            end_date: yyyy-mm-dd
        Returns:
            capacity: dictionary containing percentage filled, number of beds filled, and number of possible beds
        """
        capacity = {}
        try:
            self.connect_to_db()

            # Get the number of leases between given dates
            self.curs.execute("""SELECT COUNT(*) FROM tb_leases
                                 WHERE lease_start BETWEEN ? AND ?
            """, (start_date, end_date))
            cnt_leases = self.curs.fetchone()[0]

            # Get the number of housing units possible
            self.curs.execute("SELECT COUNT(*) FROM tb_student_housing_units")
            total_available = self.curs.fetchone()[0]

            # Format the return results
            capacity['cap_percent'] = '%' + str(round((cnt_leases / total_available) * 100, 2))
            capacity['filled_beds'] = cnt_leases
            capacity['total_beds'] = total_available
            
        except Exception as e:
            print('Error with calculating capacity: ', e)
        finally:
            self.conn.close()
        return capacity
    
def main():
    leasing = LeasingDAO()
    # leases = leasing.get_leases()
    # print(leasing.get_lease_by_id(1))
    # print(leasing.add_lease({'resident_id': 94,
    #                          'unit_id': 1,
    #                          'lease_start': '04/15/2023',
    #                          'lease_end': '07/20/2023'}))
    # print(leasing.delete_lease(17))
    rent_roll = leasing.get_rent_roll('2022-01-01', '2023-12-31')
    for i in rent_roll:
        print(i)
    # print(leasing.get_total_rent('2023-01-01', '2023-12-31'))
    print(leasing.get_capacity('2022-01-01', '2023-12-31'))

if __name__=='__main__':
    main()