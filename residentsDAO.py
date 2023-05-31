import datetime
from init_db import connect_to_db

class ResidentsDAO:
    def __init__(self):
        pass
    
    def insert_resident(self, resident):
        inserted_resident = {}
        try:
            conn = connect_to_db()
            curs = conn.cursor()

            resident['birthdate'] = datetime.datetime.strptime(resident['birthdate'], '%m/%d/%Y').date()
            curs.execute("""INSERT INTO tb_resident_info (first_name,last_name,email,phone,birthdate,gender) 
                            VALUES (?,?,?,?,?,?)
                        """, (resident['first_name'], resident['last_name'], resident['email'], 
                        resident['phone'], resident['birthdate'], resident['gender']))
            conn.commit()

            inserted_resident = self.get_resident_by_id(curs.lastrowid)
        except:
            pass

        return inserted_resident

    def get_resident_by_id(self, id):
        resident = ()
        try:
            conn = connect_to_db()
            curs = conn.cursor()

            curs.execute("SELECT * FROM tb_resident_info WHERE rowid = ?", (id, ))
            resident = curs.fetchone()
        except:
            pass
        return resident
    
def main():
    DAO = ResidentsDAO()
    print(DAO.get_resident_by_id(1))

if __name__=='__main__':
    main()