import sqlite3

def connect_to_db():
    # Connection to db, will either connect to existing or create new
    conn = sqlite3.connect('housing.db')
    return conn

conn = connect_to_db()

# Create cursor
curs = conn.cursor()

# Create residents info table
curs.execute("""CREATE TABLE IF NOT EXISTS tb_resident_info (
            resident_id INTEGER PRIMARY KEY, 
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            birthdate TEXT NOT NULL,
            gender TEXT NOT NULL
            )
""")

# Create housing complexes table
# type: student or community
curs.execute("""CREATE TABLE IF NOT EXISTS tb_housing_complexes (
            complex_name TEXT NOT NULL UNIQUE, 
            street_address TEXT NOT NULL,
            type TEXT NOT NULL
            )
""")

# Create student housing table
# type: private or shared
curs.execute("""CREATE TABLE IF NOT EXISTS tb_student_housing_units (
            complex_id INTEGER NOT NULL,
            unit_number TEXT NOT NULL,
            gender TEXT NOT NULL,
            room TEXT NOT NULL,
            bed TEXT NOT NULL,
            room_type TEXT NOT NULL,
            rent_price REAL NOT NULL,
            FOREIGN KEY (complex_id) REFERENCES tb_housing_complexes (rowid),
            UNIQUE(unit_number, room, bed)
            )
""")

# Create lease table
curs.execute("""CREATE TABLE IF NOT EXISTS tb_leases (
            resident_id INTEGER NOT NULL,
            unit_id INTEGER NOT NULL,
            lease_start TEXT NOT NULL,
            lease_end TEXT NOT NULL,
            created_date TEXT NOT NULL,
            FOREIGN KEY (resident_id) REFERENCES tb_resident_info (resident_id),
            FOREIGN KEY (unit_id) REFERENCES tb_student_housing_units (rowid),
            UNIQUE(resident_id, unit_id, lease_start)
            )
""")

# Commits change to DB
conn.commit()

# Close connection
conn.close()