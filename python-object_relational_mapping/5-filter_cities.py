#!/usr/bin/python3
"""takes name of state lists all cities of that state"""

import MySQLdb
import sys

if __name__ == "__main__":

    bdd = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cursor = bdd.cursor()
    state_name_here = sys.argv[4]
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s"
                   "ORDER BY cities.id ASC", (state_name_here,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    bdd.close()
