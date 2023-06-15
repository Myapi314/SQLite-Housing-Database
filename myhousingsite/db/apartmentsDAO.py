import json
from init_db import DB_NAME, HousingDatabase

class ApartmentsDAO(HousingDatabase):
    def get_complex_by_id(self, id):
        complex = {}
        try:
            self.connect_to_db()
            self.curs.execute("SELECT rowid, * FROM tb_housing_complexes WHERE rowid = ?", (id, ))
            row = self.curs.fetchone()
            complex['id'] = row['rowid']
            complex['name'] = row['complex_name']
            complex['addr'] = row['street_address']
            complex['type'] = row['type']
        except Exception as e:
            print('Error getting complex: ', e)
        finally:
            self.conn.close()
        return complex
    
    def get_unit_by_id(self, id):
        unit = {}
        try:
            self.connect_to_db()

            self.curs.execute("SELECT rowid, * FROM tb_student_housing_units WHERE rowid = ?", (id, ))
            row = self.curs.fetchone()
            unit['rowid'] = row['rowid']
            unit['complex_id'] = row['complex_id']
            unit['apt_num'] = row['unit_number']
            unit['gender'] = row['gender']
            unit['room'] = row['room']
            unit['bed'] = row['bed']
            unit['room_type'] = row['room_type']
            unit['rent'] = row['rent_price']

        except Exception as e:
            print('Error getting unit: ', e)
        finally: 
            self.conn.close()
        return unit
    
    def get_units_with_leases(self, complex_id, lease_start, lease_end):
        units = []
        try:
            self.connect_to_db()
            # self.curs.execute('''SELECT tbu.rowid, tbu.*, tbl.*
            #                     FROM tb_student_housing_units tbu
            #                     LEFT JOIN tb_leases tbl ON
            #                     tbu.rowid = tbl.unit_id
            #                     WHERE tbl.lease_start BETWEEN ? AND ?
            # ''', ('2022-09-10', '2023-09-10'))
            self.curs.execute('''SELECT tbu.rowid, tbu.*, tbl.*
                                FROM tb_student_housing_units tbu
                                LEFT JOIN (
                                    SELECT l.*, r.first_name
                                    FROM tb_leases l
                                    JOIN tb_resident_info r ON
                                    l.resident_id = r.resident_id
                                    WHERE lease_start BETWEEN ? AND ?
                                ) as tbl
                                ON
                                tbu.rowid = tbl.unit_id
                                WHERE tbu.complex_id = ?
            ''', (lease_start, lease_end, complex_id))
            rows = self.curs.fetchall()
            for row in rows:
                unit = {k: row[k] for k in row.keys()}
                units.append(unit)
                
        except Exception as e:
            print('Error retrieving units with leases: ', e)
        finally:self.conn.close()
        
        # return json.dumps(units, indent=2)
        return units

def main():
    dao = ApartmentsDAO(DB_NAME)
    print(dao.get_complex_by_id(1))
    print(dao.get_unit_by_id(1))
    units = dao.get_units_with_leases()
    print(units)

if __name__=='__main__':
    main()