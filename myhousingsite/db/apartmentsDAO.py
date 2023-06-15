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

def main():
    dao = ApartmentsDAO(DB_NAME)
    print(dao.get_complex_by_id(1))
    print(dao.get_unit_by_id(1))

if __name__=='__main__':
    main()