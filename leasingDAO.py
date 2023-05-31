from datetime import datetime as dt
from init_db import connect_to_db

class LeasingDAO:
    def __init__(self):
        pass

    def get_leases(self):
        leases = []
        try:
            conn = connect_to_db()
            curs = conn.cursor()
            curs.execute("SELECT rowid, * FROM tb_leases")
            leases = curs.fetchall()
        except:
            pass
        return leases
    
    def get_lease_by_id(self, id):
        lease = ()
        try:
            conn = connect_to_db()
            curs = conn.cursor()

            curs.execute("SELECT * FROM tb_leases WHERE rowid = ?", (id,))
            lease = curs.fetchone()
        except:
            pass
        return lease
    
    def add_lease(self, lease):
        new_lease = ()
        try:
            conn = connect_to_db()
            curs = conn.cursor()

            curs.execute("INSERT INTO tb_leases VALUES (?,?,?,?,?)", (lease['resident_id'],
                         lease['unit_id'], dt.strptime(lease['lease_start'], '%m/%d/%Y').date(),
                         dt.strptime(lease['lease_end'], '%m/%d/%Y').date(), dt.now())
                         )
            conn.commit()
            new_lease = self.get_lease_by_id(curs.lastrowid)
        except:
            print('LEASE WAS NOT ADDED')
        return new_lease
    
    def delete_lease(self, id):
        del_lease = ()
        try:
            conn = connect_to_db()
            curs = conn.cursor()

            del_lease = self.get_lease_by_id(id)
            curs.execute("DELETE FROM tb_leases WHERE rowid = ?", (id,))
            conn.commit()
        except:
            pass
        return del_lease
    
    def get_rent(self):
        rent = ()
        try:
            conn = connect_to_db()
            curs = conn.cursor()

            curs.execute("""SELECT l.rowid, l.*, h.rent_price FROM tb_leases l
                        JOIN tb_student_housing_units h ON
                        l.unit_id = h.rowid
                        WHERE l.lease_start BETWEEN '2022-09-01' AND '2022-12-01'
                        AND h.complex_id = 2
            """)

            rent = curs.fetchall()
        except:
            print('FAILED')
        return rent

def main():
    leasing = LeasingDAO()
    # print(leasing.get_leases())
    # print(leasing.get_lease_by_id(1))
    # print(leasing.add_lease({'resident_id': 94,
    #                          'unit_id': 1,
    #                          'lease_start': '04/15/2023',
    #                          'lease_end': '07/20/2023'}))
    print(leasing.get_rent())

if __name__=='__main__':
    main()