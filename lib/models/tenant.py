#!/usr/bin/env python3
from models.__init__ import CONN, CURSOR


class Tenant():
    all = {}

    def __init__(self, name, contact_info, id=None):
        self.id = id
        self.name = name
        self.contact_info = contact_info

    def __repr__(self):
        return f"<Tenant {self.id}: {self.name}, {self.contact_info}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        if isinstance(contact_info, str) and len(contact_info):
            self._contact_info = contact_info
        else:
            raise ValueError("Contact info must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS tenants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            contact_info TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS tenants;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO tenants (name, contact_info)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.contact_info))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, contact_info):
        tenant = cls(name, contact_info)
        tenant.save()
        return tenant

    def update(self):
        sql = """
            UPDATE tenants
            SET name = ?, contact_info = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.contact_info, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM tenants
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        tenant = cls.all.get(row[0])
        if tenant:
            tenant.name = row[1]
            tenant.contact_info = row[2]
        else:
            tenant = cls(row[1], row[2])
            tenant.id = row[0]
            cls.all[tenant.id] = tenant
        return tenant

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM tenants
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM tenants
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM tenants
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None





Tenant.create_table()
# tenant1 = Tenant.create("John", "0717370359")
# tenant2 = Tenant.create("Victor", '0730359548')




