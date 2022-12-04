#!/usr/bin/python3
"""
Script that takes name of state as an argument and
lists all cities of that state.
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
            host='localhost', port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    print(", ".join([city[2] for city in c.fetchall()
                    if city[4] == sys.argv[4]]))
