import sqlite3


class dbpassword:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS psw(
        Name text,
        Purpose text Primary Key,
        Password text,
        Length text,
        Date text,
        Time text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def inserts(self, Name, Purpose, Password, Length, Date, Time):
        self.cur.execute("insert into psw values(?,?,?,?,?,?)",
                         (Name, Purpose, Password, Length, Date, Time))
        self.con.commit()

# add = dbpassword("psw.db")
# add.inserts("Jordan", "Ums", "0=$9PsF3jJ[", "11", "20/08/2023", "13:25:24")

    def fetch(self):
        self.cur.execute("SELECT * from psw")
        rows = self.cur.fetchall()
        print(*rows)
        return rows
    def remove(self, Purpose):
        self.cur.execute("delete from psw where Purpose=?", (Purpose,))
        self.con.commit()