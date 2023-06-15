import sqlite3

DB_NAME = 'housing.db.sqlite3'

class HousingDatabase():
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn: sqlite3.Connection = None
        self.curs: sqlite3.Cursor = None

    def connect_to_db(self):

        # Connection to db, will either connect to existing or create new
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

        # Create cursor
        self.curs = self.conn.cursor()
        return self.conn
    
    def create_db(self):
        try: 
            self.connect_to_db()

            # Create residents info table
            self.curs.execute("""CREATE TABLE IF NOT EXISTS tb_resident_info (
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
            self.curs.execute("""CREATE TABLE IF NOT EXISTS tb_housing_complexes (
                        complex_name TEXT NOT NULL UNIQUE, 
                        street_address TEXT NOT NULL,
                        type TEXT NOT NULL
                        )
            """)

            # Create student housing table
            # type: private or shared
            self.curs.execute("""CREATE TABLE IF NOT EXISTS tb_student_housing_units (
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
            self.curs.execute("""CREATE TABLE IF NOT EXISTS tb_leases (
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
            self.conn.commit()

        except Exception as e:
            print("Error in initializing database: ", e)

        finally:
            # Close connection
            self.conn.close()

def main():
    db = HousingDatabase(DB_NAME)
    db.create_db()

if __name__=='__main__':
    main()
