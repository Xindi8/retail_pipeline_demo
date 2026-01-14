import sqlite3

class DB:
    def __init__(self, path="demo.db"):
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row

    def close(self):
        self.conn.close()

    def exec(self, sql, params=()):
        return self.conn.execute(sql, params)

    def commit(self):
        self.conn.commit()
