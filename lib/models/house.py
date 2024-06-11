
from models.__init__ import CONN, CURSOR


class Apartment():
    all = {}

    def __init__(self, address, rent, availability=True, id=None):
        self.id = id
        self.address = address
        self.rent = rent
        self.availability = availability

    def __repr__(self):
        return f"<Apartment {self.id}: {self.address}, Rent: {self.rent}, Available: {self.availability}>"

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, str) and len(address):
            self._address = address
        else:
            raise ValueError("Address must be a non-empty string")

    @property
    def rent(self):
        return self._rent

    @rent.setter
    def rent(self, rent):
        if isinstance(rent, (int, float)) and rent > 0:
            self._rent = rent
        else:
            raise ValueError("Rent must be a number greater than 0")

    @property
    def availability(self):
        return self._availability

    @availability.setter
    def availability(self, availability):
        if isinstance(availability, bool):
            self._availability = availability
        else:
            raise ValueError("Availability must be a boolean")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS apartments (
            id INTEGER PRIMARY KEY,
            address TEXT,
            rent REAL,
            availability BOOLEAN)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS apartments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO apartments (address, rent, availability)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.address, self.rent, self.availability))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, address, rent, availability):
        apartment = cls(address, rent, availability)
        apartment.save()
        return apartment

    def update(self):
        sql = """
            UPDATE apartments
            SET address = ?, rent = ?, availability = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.address, self.rent, self.availability, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM apartments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        apartment = cls.all.get(row[0])
        if apartment:
            apartment.address = row[1]
            apartment.rent = row[2]
            apartment.availability = bool(row[3])
        else:
            apartment = cls(row[1], row[2], bool(row[3]))
            apartment.id = row[0]
            cls.all[apartment.id] = apartment
        return apartment

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM apartments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM apartments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_address(cls, address):
        sql = """
            SELECT *
            FROM apartments
            WHERE address = ?
        """
        row = CURSOR.execute(sql, (address,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    

Apartment.create_table()
# apartment1 = Apartment.create("123 Main St", 1200.00,True)
# apartment2 = Apartment.create("456 Elm St", 1500.00, True)
