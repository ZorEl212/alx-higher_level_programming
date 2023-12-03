#!/usr/bin/python3
""" Module that contains a script that lists all states from the database
    hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def list_states():
    """List all rows in states table matching user input"""
    username = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           password=passwd, database=db)
    cursor = conn.cursor()
    sql = f"SELECT * FROM states WHERE name = '{name}' ORDER BY states.id"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    list_states()
