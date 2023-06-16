import datetime
import csv

from init_db import DB_NAME, HousingDatabase

class LoadDummyData(HousingDatabase):
    def insert_residents(self):
        try:
            self.connect_to_db()
            with open('./MOCK_DATA/MOCK_RESIDENT_DATA.csv', newline='') as residents_file:
                reader = csv.reader(residents_file, delimiter=',')
                for row in reader:
                    row[4] =  datetime.datetime.strptime(row[4], '%m/%d/%Y').date()
                    self.curs.execute("INSERT OR IGNORE INTO tb_resident_info (first_name,last_name,email,phone,birthdate,gender) VALUES (?,?,?,?,?,?)", row)
                    
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.conn.close()
            

    def insert_complexes(self):
        complexes = [('Red Brick Apartments', '14 Badeau Park', 'student'), 
        ('Avonlea Womens', '90 Warner Junction','student'),
        ('Avonlea Mens', '257 Armistice Point','student'),
        ('Liberty Corner', '6810 Golf Course Court','community')]

        try:
            self.connect_to_db()

            self.curs.executemany("INSERT OR IGNORE INTO tb_housing_complexes VALUES (?,?,?)", complexes)

            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.conn.close()


    def insert_leases(self):
        leases = [(1, 61, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('12/15/2022', '%m/%d/%Y').date(), datetime.datetime.now()),
          (2, 60, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('12/15/2022', '%m/%d/%Y').date(), datetime.datetime.now()),
          (4, 1, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('12/15/2022', '%m/%d/%Y').date(), datetime.datetime.now()),
          (6, 2, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('12/15/2022', '%m/%d/%Y').date(), datetime.datetime.now()),
          (10, 61, datetime.datetime.strptime('01/03/2023', '%m/%d/%Y').date(), datetime.datetime.strptime('04/08/2023', '%m/%d/%Y').date(), datetime.datetime.now()),
          (12, 60, datetime.datetime.strptime('01/03/2023', '%m/%d/%Y').date(), datetime.datetime.strptime('04/08/2023', '%m/%d/%Y').date(), datetime.datetime.now()),
          (16, 64, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('04/08/2023', '%m/%d/%Y').date(), datetime.datetime.now()),
          (15, 65, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('12/15/2022', '%m/%d/%Y').date(), datetime.datetime.now()),
          (18, 43, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('12/15/2022', '%m/%d/%Y').date(), datetime.datetime.now()),
          (34, 44, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('12/15/2022', '%m/%d/%Y').date(), datetime.datetime.now()),
          (41, 65, datetime.datetime.strptime('01/03/2023', '%m/%d/%Y').date(), datetime.datetime.strptime('04/08/2023', '%m/%d/%Y').date(), datetime.datetime.now()),
          (42, 45, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('12/15/2022', '%m/%d/%Y').date(), datetime.datetime.now()),
          (43, 68, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('12/15/2022', '%m/%d/%Y').date(), datetime.datetime.now()),
          (44, 69, datetime.datetime.strptime('01/03/2023', '%m/%d/%Y').date(), datetime.datetime.strptime('04/08/2023', '%m/%d/%Y').date(), datetime.datetime.now()),
          (50, 46, datetime.datetime.strptime('01/03/2023', '%m/%d/%Y').date(), datetime.datetime.strptime('04/08/2023', '%m/%d/%Y').date(), datetime.datetime.now()),
          (55, 55, datetime.datetime.strptime('09/10/2022', '%m/%d/%Y').date(), datetime.datetime.strptime('04/08/2023', '%m/%d/%Y').date(), datetime.datetime.now())]

        try:
            self.connect_to_db()
            self.curs.executemany("INSERT OR IGNORE INTO tb_leases VALUES (?,?,?,?,?)", leases)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.conn.close()

    def insert_units(self):
        try:
            self.connect_to_db()
            with open('./MOCK_DATA/MOCK_UNITS_DATA.csv', newline='') as units_file:
                reader = csv.reader(units_file, delimiter=',')
                for row in reader:
                    row[0] = int(row[0])
                    row[6] = float(row[6])
                    self.curs.execute("INSERT OR IGNORE INTO tb_student_housing_units VALUES (?,?,?,?,?,?,?)", row)

            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.conn.close()

def main():
    loadData = LoadDummyData(DB_NAME)
    loadData.insert_residents()
    loadData.insert_complexes()
    loadData.insert_leases()
    loadData.insert_units()

if __name__=='__main__':
    main()