#!/usr/bin/python3


import sys
import MySQLdb

'''
script that lists all states from database
'''
if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    [print(states) for states in c.fetchall()]
