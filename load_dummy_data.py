import sqlite3
import csv

# Connection to db, will either connect to existing or create new
conn = sqlite3.connect('housing.db')

# Create cursor
curs = conn.cursor()

# INSERT one record
# curs.execute("INSERT INTO tb_resident_info VALUES ('John', 'Doe', 'john@doe.com', '123-456-7890', '01-01-1999')")

# THIS HAS BEEN EXECUTED
with open('../MOCK_DATA/MOCK_RESIDENT_DATA.csv', newline='') as residents_file:
    reader = csv.reader(residents_file, delimiter=',')
    for row in reader:
        curs.execute("INSERT INTO tb_resident_info (first_name,last_name,email,phone,birthdate) VALUES (?,?,?,?,?)", row)

# residents = [('John', 'Doe', 'john@doe.com', '1234567890', '01-01-1999'), 
#              ('Mary', 'Jane', 'mary@yahoo.com', '9876543210', '01-02-1999'), 
#              ('Alice', 'West', 'alice@yahoo.com', '1112223333', '02-01-1999')]

# curs.executemany("INSERT INTO tb_resident_info VALUES (?,?,?,?,?)", residents)

# Commits change to DB
conn.commit()

# Close connection
conn.close()