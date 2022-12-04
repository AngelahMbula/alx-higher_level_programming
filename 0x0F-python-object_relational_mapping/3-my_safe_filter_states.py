#!/usr/bin/python3
"""
Script that takes in arguments and display all values
safe from SQL injections.
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
            host='localhost', port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
