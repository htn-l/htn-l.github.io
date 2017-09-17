# Import the driver.
import psycopg2  # Connect to the "bank" database.
import uuid


class RoachDB:
    def __init__(self):
        self.conn = psycopg2.connect(database='sumnotes', user='maxroach', host='localhost', port=26257)
        # Make each statement commit immediately.
        self.conn.set_session(autocommit=True)
        # Open a cursor to perform database operations.
        self.cur = self.conn.cursor()
        # Print out the balances.
        self.cur.execute("SET DATABASE = sumnotes")
        self.cur.execute("GRANT ALL ON DATABASE sumnotes TO maxroach;")
        self.cur.execute("GRANT ALL ON TABLE * TO maxroach")

    def create_user(self, username, password):
        self.cur.execute('INSERT INTO users (username, password) VALUES (%s,%s)', (username, password))

    def add_lecture(self, USERNAME, transcript, summary="TEMWP", date="TODAY", coursecode="NONE", profname="LOSER"):
        self.cur.execute(
            "INSERT INTO lectures (transcript, summary, date,coursecode,profname) VALUES (%s,%s,%s,%s,%s) RETURNING lectureid",
            (transcript, summary, date, coursecode, profname))
        number = self.cur.fetchone()[0]
        self.cur.execute("INSERT INTO users_to_lectures (username, lectureid) VALUES (%s,%s)", [USERNAME, number])

    def find_user(self, username):
        self.cur.execute("SELECT * FROM users WHERE username = %s", [username])
        return len(self.cur.fetchall()) > 0

    def get_user_hash(self, username):
        self.cur.execute("SELECT password FROM users WHERE username = (%s)", [username])
       # print(self.cur.fetchall())
        return self.cur.fetchall()[0][0]



    def view_lecture(self, id):
        self.cur.execute("SELECT (transcript, summary) FROM lectures WHERE lectureid = %s", [id])
        return self.cur.fetchall()

    def get_all_lectures(self, username):
        self.cur.execute("SELECT lectureid FROM users_to_lectures WHERE username=(%s)", [username])
        temp = []
        for i in self.cur.fetchall():
            data = self.view_lecture(str(i[0]))
            data2 = list(data)
            temp.append(data2[0][0])
        return temp



    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    db = RoachDB()
    # print(db.find_user("leonf"))
    # db.view_lecture("280333094310215681")
    # db.get_user_hash("leon")
    # if not db.find_user("leonf"):
    #     db.create_user("leonf", "Fattakhov")
    db.add_lecture("leon",
                   "djfjaslkdjfkdsajf lksdjflksjlkfjdslkfjdsalkjfds;lkajflkdsajflksajdlkfjdsalkfjdslkajfdlksajflkjlkdjfalkdsjflkdsjflkdsjfldsjfjflkdsajf;lsaf")
    print(db.get_all_lectures("leon"))
    db.close()
