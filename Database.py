import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS MyEmployees(
            id Integer Primary Key,
            name text,
            age text,
            dob text,
            email text,
            gender text,
            contact text,
            Company text,
            Job text,
            CGPA text,
            address text,
            country text
        )
        """
        self.cur.execute(sql)
        self.con.commit()


 # o = Database("MyEmployees.db")


    # Insert Function

    def insert(self, name, age, dob, email, gender, contact, Company, Job, CGPA, address, country):
        self.cur.execute("insert into MyEmployees values(NULL,?,?,?,?,?,?,?,?,?,?,?)",
                         (name, age, dob, email, gender, contact, Company, Job, CGPA, address, country))
        self.con.commit()


# o = Database("MyEmployees.db")
# o.insert("Ram", "25", "25-10-1996", "ram@gmail.com", "male", "98566412377", "Microsoft", "Data Analyst", "9.0", "Cherry Road", "India")

    # Fetch all data from db

    def fetch(self):
        self.cur.execute("SELECT * from MyEmployees")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a record in DB
    def remove(self, id):
        self.cur.execute("delete from MyEmployees where id=?", (id,))
        self.con.commit()

    # Update a record in DB
    def update(self, id, name, age, dob, email, gender, contact, Company, Job, CGPA, address, country):
        self.cur.execute(
            "update MyEmployees set name=?, age=?, dob=?, email=?, gender=?, contact=?, company=?, Job=?, CGPA=?, address=?, country=? where id=?",
            (name, age, dob, email, gender, contact, Company, Job, CGPA, address, country, id))
        self.con.commit()
