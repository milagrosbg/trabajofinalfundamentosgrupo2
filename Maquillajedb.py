import sqlite3
DATABASE_NAME = "maquillajes.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS maquillajes(
                codigo INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio INTEGER NOT NULL,
                stock INTEGER NOT NULL,
                marca TEXT NOT NULL,
                color TEXT NOT NULL,
                acabado TEXT NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

