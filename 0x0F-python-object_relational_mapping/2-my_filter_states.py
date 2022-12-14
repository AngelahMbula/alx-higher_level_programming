#!/usr/bin/python3
"""Script that takes an argument and display all values in states."""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
            host='localhost', port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
            FROM states \
            WHERE BINARY name = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
    c.close()
    db.close()
