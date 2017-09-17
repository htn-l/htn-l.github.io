# Import the driver.
import psycopg2  # Connect to the "bank" database.


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
        self.cur.execute("INSERT INTO lectures (transcript, summary, date,coursecode,profname) VALUES (%s,%s,%s,%s,%s)",
                    (transcript, summary, date, coursecode, profname))
        self.cur.execute("INSERT INTO users_to_lectures (username) VALUES (%s)",[USERNAME])

    def find_user(self, username):
        self.cur.execute("SELECT * FROM users WHERE username=%s", [username])
        return len(self.cur.fetchall()) > 0

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    db = RoachDB()
    print(db.find_user("leonf"))
    if not db.find_user("leonf"):
        db.create_user("leonf", "Fattakhov")
    db.add_lecture("leonf","djfjaslkdjfkdsajf lksdjflksjlkfjdslkfjdsalkjfds;lkajflkdsajflksajdlkfjdsalkfjdslkajfdlksajflkjlkdjfalkdsjflkdsjflkdsjfldsjfjflkdsajf;lsaf")
    db.close()
