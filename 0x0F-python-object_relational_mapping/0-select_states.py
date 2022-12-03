#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    [print(states) for states in c.fetchall()]
