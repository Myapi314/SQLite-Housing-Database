import sqlite3
# Connection to db, will either connect to existing or create new
conn = sqlite3.connect('housing.db')

# Create cursor
curs = conn.cursor()

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

# Commits change to DB
conn.commit()

# Close connection
conn.close()