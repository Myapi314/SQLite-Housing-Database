import sqlite3
import csv

# Connection to db, will either connect to existing or create new
conn = sqlite3.connect('housing.db')

# Create cursor
curs = conn.cursor()

# Create residents info table
curs.execute("""CREATE TABLE IF NOT EXISTS tb_resident_info (
            resident_id INTEGER PRIMARY KEY, 
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            birthdate TEXT NOT NULL
            )
""")

# Commits change to DB
conn.commit()

# Close connection
conn.close()