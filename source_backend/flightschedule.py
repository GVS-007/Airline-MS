import sqlite3 as sq
import datetime

#x = sq.connect("flights.db")
#y = sq.connect("schedule.db")
x= sq.connect("routes.db")
x_c = x.cursor()
#y_c = y.cursor()

x_c.execute("""CREATE TABLE IF NOT EXISTS routes(
             city1 text,
             city2 text,
             distance real
            )""")

#y_c.execute("""CREATE TABLE IF NOT EXISTS admins(userID text,name text,password text,airlineID text)""")
x.commit()
#y.commit()
#z.commit()

x_c.execute("INSERT INTO routes VALUES('A','B',100)")
x_c.execute("INSERT INTO routes VALUES('B','C',200)")
x_c.execute("INSERT INTO routes VALUES('C','A',300)")
x.commit()



