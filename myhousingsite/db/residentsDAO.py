import datetime
from init_db import DB_NAME, HousingDatabase

class ResidentsDAO(HousingDatabase):
    
    def insert_resident(self, resident: dict):
        """ Create and insert a new resident into table. 
        Params:
            resident: {'first_name': str, 'last_name': str, 'email': str, 'phone': str, 'birthdate': str yyyy-mm-dd, 'gender': str M/F}"""
        
        inserted_resident = {}

        try:
            self.connect_to_db()

            # Convert birthdate to date
            # resident['birthdate'] = datetime.datetime.strptime(resident['birthdate'], '%m/%d/%Y').date()

            # Insert the new resident into the resident info table
            self.curs.execute("""INSERT INTO tb_resident_info (first_name,last_name,email,phone,birthdate,gender) 
                            VALUES (?,?,?,?,?,?)
                        """, (resident['first_name'], resident['last_name'], resident['email'], 
                        resident['phone'], resident['birthdate'], resident['gender']))
                        
            self.conn.commit()

            inserted_resident = self.get_resident_by_id(self.curs.lastrowid)

        except Exception as e:
            self.conn.rollback()
            print('Issue adding new resident: ', e)

        finally:
            self.conn.close()

        return inserted_resident

    def get_resident_by_id(self, id: int):
        """ Select resident by unique resident_id. """

        resident = {}
        try:
            self.connect_to_db()

            # Select the resident based on their unique id
            self.curs.execute("SELECT * FROM tb_resident_info WHERE rowid = ?", (id, ))
            row = self.curs.fetchone()
            # resident = row
            # print(type(row))
            resident['id'] = row['resident_id']
            resident['first_name'] = row['first_name']
            resident['last_name'] = row['last_name']
            resident['email'] = row['email']
            resident['phone'] = row['phone']
            resident['birthdate'] = row['birthdate']
            resident['gender'] = row['gender']

        except Exception as e:
            print('Error getting resident: ', e)

        finally:
            self.conn.close()

        return resident
    
    def delete_resident(self, id: int):
        """ Delete resident by given id. """
        deleted_res = {}

        # Get the deleted user from the id
        deleted_res = self.get_resident_by_id(id)

        try:

            self.connect_to_db()

            # Delete the resident based on their unique id
            self.curs.execute("DELETE FROM tb_resident_info WHERE rowid = ?", (id, ))
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            print('Error deleting resident: ', e)

        finally:
            self.conn.close()

        return deleted_res
    
    def update_resident(self, id: int, resident: dict):
        """ Update resident with new resident data.
        Params:
            id: unique id corresponding with resident
            resident: {'first_name': str, 'last_name': str, 'email': str, 'phone': str, 'birthdate': str yyyy-mm-dd, 'gender': str M/F}
        """
        updated_res = {}
        try:
            self.connect_to_db()

            # Update the resident 
            self.curs.execute("""UPDATE tb_resident_info SET 
                                 first_name = ?, last_name = ?, email = ?, phone = ?, birthdate = ?, gender = ?
                                 WHERE resident_id = ?
            """, (resident['first_name'], resident['last_name'], resident['email'], 
                        resident['phone'], resident['birthdate'], resident['gender'], id))
            
            self.conn.commit()

            # Get the resident to see updated changes
            updated_res = self.get_resident_by_id(id)

        except Exception as e:
            self.conn.rollback()
            print('Error updating resident: ', e)
        
        finally:
            self.conn.close()

        return updated_res

def main():
    DAO = ResidentsDAO(DB_NAME)
    print(DAO.get_resident_by_id(10))
    print(DAO.get_resident_by_id(11))
    print(DAO.insert_resident({'first_name': 'John', 
                               'last_name': 'Doe', 
                               'email': 'john@doe.com', 
                               'phone': '123-456-7890', 
                               'birthdate': '01/01/1999', 
                               'gender': 'M'
    }))
    print(DAO.update_resident(101, {'first_name': 'John', 
                                    'last_name': 'Doe', 
                                    'email': 'john@doe.com', 
                                    'phone': '999-888-7777', 
                                    'birthdate': '1999-01-01', 
                                    'gender': 'M'}))
    print(DAO.delete_resident(101))

if __name__=='__main__':
    main()