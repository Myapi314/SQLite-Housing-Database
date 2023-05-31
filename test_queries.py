from datetime import datetime as dt
import sqlite3
# Connection to db, will either connect to existing or create new
conn = sqlite3.connect('housing.db')

# Create cursor
curs = conn.cursor()

# ********* INSERT ***************
curs.execute("""INSERT INTO tb_resident_info (first_name,last_name,email,phone,birthdate,gender) 
                VALUES ('John', 'Doe', 'john@doe.com', '123-456-7890', date('1999-01-01'), 'M')
""")

lease = {'resident_id': 94,
        'unit_id': 1,
        'lease_start': '04/15/2023',
        'lease_end': '07/20/2023'}

curs.execute("INSERT INTO tb_leases VALUES (?,?,?,?,?)", (lease['resident_id'],
                         lease['unit_id'], dt.strptime(lease['lease_start'], '%m/%d/%Y').date(),
                         dt.strptime(lease['lease_end'], '%m/%d/%Y').date(), dt.now())
                         )
conn.commit()

lease_id = curs.lastrowid
curs.execute("SELECT * FROM tb_leases WHERE rowid = ?", (lease_id,))
print(curs.fetchone())

curs.execute("DELETE FROM tb_leases WHERE rowid = ?", (lease_id, ))
conn.commit()
print('********************\n')

# ********* QUERY AND FETCH *************

# SELECT all rows from tb_residents_info
curs.execute("SELECT * FROM tb_resident_info")

# Returns a python list of tuples
# print(curs.fetchall())

# Returns the first
# print(curs.fetchone())

# Return a certain number
# print(curs.fetchmany(5))

residents = curs.fetchmany(10)

# Print the names
for resident in residents:
    print(resident[1])

curs.execute("SELECT * FROM tb_resident_info WHERE last_name LIKE 'Do%'")
results = curs.fetchall()
print(results)

curs.execute("SELECT * FROM tb_resident_info WHERE datetime(birthdate) >= datetime('1995-01-01')")
results = curs.fetchall()
for result in results:
    print(result)

curs.execute("SELECT COUNT(*) FROM tb_resident_info WHERE datetime(birthdate) < datetime('1995-01-01')")
results = curs.fetchone()
print(results)

# ******* UPDATE ************
# Use primary key, use unique rowid
curs.execute(""" UPDATE tb_resident_info SET phone = '777-888-9999'
                WHERE email = 'john@doe.com' 
                AND phone = '123-456-7890'
""")
conn.commit()
curs.execute("SELECT * FROM tb_resident_info WHERE rowid = 101")
print(curs.fetchone())

# ******** DELETE ************
curs.execute("DELETE FROM tb_resident_info WHERE rowid = 101")

# Commits change to DB
conn.commit()

curs.execute("SELECT * FROM tb_resident_info WHERE first_name = 'Pepita'")
print(curs.fetchall())

curs.execute("SELECT * FROM tb_resident_info WHERE rowid > 99")
print(curs.fetchall())

curs.execute("SELECT * FROM tb_leases")
# print(curs.fetchall())

# Close connection
conn.close()