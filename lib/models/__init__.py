import sqlite3

CONN = sqlite3.connect('apartment.db')
CURSOR = CONN.cursor()
