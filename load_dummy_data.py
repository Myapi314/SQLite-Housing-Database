import sqlite3
import datetime
import csv

# Connection to db, will either connect to existing or create new
conn = sqlite3.connect('housing.db')

# Create cursor
curs = conn.cursor()

# with open('../MOCK_DATA/MOCK_RESIDENT_DATA.csv', newline='') as residents_file:
#     reader = csv.reader(residents_file, delimiter=',')
#     for row in reader:
#         row[4] =  datetime.datetime.strptime(row[4], '%m/%d/%Y').date()
#         curs.execute("INSERT INTO tb_resident_info (first_name,last_name,email,phone,birthdate,gender) VALUES (?,?,?,?,?,?)", row)
        
# conn.commit()

# complexes = [('Red Brick Apartments', '14 Badeau Park', 'student'), 
#              ('Avonlea Womens', '90 Warner Junction','student'),
#              ('Avonlea Mens', '257 Armistice Point','student'),
#              ('Liberty Corner', '6810 Golf Course Court','community')]
# curs.executemany("INSERT INTO tb_housing_complexes VALUES (?,?,?)", complexes)

# conn.commit()

# with open('../MOCK_DATA/MOCK_UNITS_DATA.csv', newline='') as units_file:
#     reader = csv.reader(units_file, delimiter=',')
#     for row in reader:
#         row[0] = int(row[0])
#         row[6] = float(row[6])
#         curs.execute("INSERT INTO tb_student_housing_units VALUES (?,?,?,?,?,?,?)", row)

# conn.commit()

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
curs.executemany("INSERT INTO tb_leases VALUES (?,?,?,?,?)", leases)
conn.commit()

# Close connection
conn.close()