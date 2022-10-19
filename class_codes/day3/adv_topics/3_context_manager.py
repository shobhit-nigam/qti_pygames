import time
import sqlite3
import os
class DataBaseManager():
    def __init__(self, dbName, hostname=None, port=None, path=None):
        self.dbName = dbName
        self.con = None

    def __enter__(self):
        if self.dbName in os.listdir():
            print("found the db")
            self.flag = 1
        else:
            self.flag = 0
            print("does not exist")
            # raise an exception
        return self

    def connect(self):
        self.con = sqlite3.connect(self.dbName)
        cur = dbObject.con.cursor()
        return cur

    def __exit__(self, x, y, z):
        if self.flag == 1:
            self.con.close()
        print("exiting now")


with DataBaseManager("chinook.db") as dbObject:
    # dbactivities
    print("working with database")
    cur = dbObject.connect()
    query = "SELECT * FROM employees"
    cur.execute(query)
    for x in cur.fetchall():
        print(x[1])

    time.sleep(5)

print("outside the with block")
