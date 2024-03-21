#!/usr/bin/python3
"""module show all cities of a specific state"""

import MySQLdb
import sys

if __name__ == "__main__":

    bdd = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cursor = bdd.cursor()
    state_name_here = sys.argv[4]
    cursor.execute("SELECT cities.name, states.name "
                   "FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s "
                   "ORDER BY cities.id ASC", (state_name_here,))
    rows_of_rows_in_rows_more_rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows_of_rows_in_rows_more_rows))

    cursor.close()
    bdd.close()
