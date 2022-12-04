#!/usr/bin/python3
"""Script that lists all cities from the database."""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
            host='localhost', port=3306, user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    [print(city) for city in c.fetchall()]
