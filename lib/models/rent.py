
from models.__init__ import CONN, CURSOR


class Lease():
    all = {}

    def __init__(self, tenant_id, apartment_id, start_date, end_date, id=None):
        self.id = id
        self.tenant_id = tenant_id
        self.apartment_id = apartment_id
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"<Lease {self.id}: Tenant {self.tenant_id}, Apartment {self.apartment_id}, From {self.start_date} to {self.end_date}>"

    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        if isinstance(tenant_id, int):
            self._tenant_id = tenant_id
        else:
            raise ValueError("Tenant ID must be an integer")

    @property
    def apartment_id(self):
        return self._apartment_id

    @apartment_id.setter
    def apartment_id(self, apartment_id):
        if isinstance(apartment_id, int):
            self._apartment_id = apartment_id
        else:
            raise ValueError("Apartment ID must be an integer")

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS leases (
            id INTEGER PRIMARY KEY,
            tenant_id INTEGER,
            apartment_id INTEGER,
            start_date DATE,
            end_date DATE,
            FOREIGN KEY (tenant_id) REFERENCES tenants (id),
            FOREIGN KEY (apartment_id) REFERENCES apartments (id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS leases;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO leases (tenant_id, apartment_id, start_date, end_date)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.tenant_id, self.apartment_id, self.start_date, self.end_date))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, tenant_id, apartment_id, start_date, end_date):
        lease = cls(tenant_id, apartment_id, start_date, end_date)
        lease.save()
        return lease

    def update(self):
        sql = """
            UPDATE leases
            SET tenant_id = ?, apartment_id = ?, start_date = ?, end_date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.tenant_id, self.apartment_id, self.start_date, self.end_date, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM leases
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        lease = cls.all.get(row[0])
        if lease:
            lease.tenant_id = row[1]
            lease.apartment_id = row[2]
            lease.start_date = row[3]
            lease.end_date = row[4]
        else:
            lease = cls(row[1], row[2], row[3], row[4])
            lease.id = row[0]
            cls.all[lease.id] = lease
        return lease

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM leases
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM leases
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_tenant_id(cls, tenant_id):
        sql = """
            SELECT *
            FROM leases
            WHERE tenant_id = ?
        """
        rows = CURSOR.execute(sql, (tenant_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_apartment_id(cls, apartment_id):
        sql = """
            SELECT *
            FROM leases
            WHERE apartment_id = ?
        """
        rows = CURSOR.execute(sql, (apartment_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    

Lease.create_table()
# lease1 = Lease.create(1, 1, "2024-01-01", "2024-12-31")