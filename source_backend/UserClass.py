import sqlite3 as sq

import calendar

x = sq.connect("passenger.db")
y = sq.connect('admin.db')

x_c = x.cursor()
y_c = y.cursor()


x_c.execute("""CREATE TABLE IF NOT EXISTS passengers(
            userID text,
            name text,
            password text,
            city text,
            phonenumber text,
            dob text,
            emailID text,
            TicketID text
            )""")
y_c.execute("""CREATE TABLE IF NOT EXISTS admins(userID text,name text,password text,airlineID text)""")

x.commit()
y.commit()


def findday(date):
    day, month, year = (int(i) for i in date.split('/'))
    daynumber = calendar.weekday(year, month, day)
    days = ["MON", "TUE", "WED", "THU",
            "FRI", "SAT", "SUN"]
    return days[daynumber]


class UserClass:

    def __init__(self, userid, name, password):
        self.userID = userid
        self.Name = name
        self.password = password

    def login(self, password):
        if self.password == password:
            return True
        else:
            return False


class Passenger(UserClass):
    def __init__(self, userid, name, password, city, phno, dob, mailid):
        super().__init__(userid, name, password)
        self.city = city
        self.phonenumber = phno
        self.dob = dob
        self.emailid = mailid


    def signup(self):
        st = "0"
        x_c.execute("""INSERT INTO passengers (userID,name,password,city,phonenumber,dob,emailID, TicketID)            
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
                    (self.userID, self.Name, self.password, self.city, self.phonenumber, self.dob, self.emailid, st))
        x.commit()

    def update_profile(self, tup):
        x_c.execute("""UPDATE passengers 
                    SET 
                        name = ?,
                        password = ?,
                        city = ?,
                        phonenumber = ?,
                        dob = ?,
                        emailID = ?
                    WHERE 
                        userID = ?;
                    """, (tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], self.userID))
        x.commit()

    def addticket(self, ticket):
        x_c.execute("INSERT INTO Tickets VALUES(?, ?, ?, ?, ?, ?, ?)",
                    (ticket.ticketID, ticket.flightID, ticket.scheduleID,
                     ticket.date, ticket.classType, ticket.ticketprice, ticket.seatno + 1))
        x.commit()

        x_c.execute("SELECT * FROM passengers WHERE userID = ? AND name = ?", (self.userID, self.Name))
        i = x_c.fetchone()
        tickets = i[7]
        if tickets == "0":
            newTickets = ticket.ticketID
        else:
            newTickets = tickets + "," + ticket.ticketID

        x_c.execute("UPDATE passengers SET TicketID = ? WHERE userID = ? AND name = ?",
                        (newTickets, self.userID, self.Name))
        x.commit()

    def gettrips(self):
        x_c.execute("SELECT * FROM passengers WHERE userID = ? AND name = ?", (self.userID, self.Name))
        i = x_c.fetchone()
        temp = i[7].split(",")
        x_c.execute("SELECT * FROM Tickets")
        tkts = x_c.fetchall()
        thetrips = []
        for id in temp:
            for j in tkts:
                if j[0] == id:
                    thetrips.append(j)

        return thetrips





class Admin(UserClass):
    def __init__(self, userid, name, password, key):
        super().__init__(userid, name, password)
        self.key = key

    def signup(self):
        y_c.execute("INSERT INTO admins (userID,name,password,airlineID) VALUES(?, ?, ?, ?)",
                    (self.userID, self.Name, self.password, self.key))
        y.commit()

    def addflight(self, details):
        day = findday(details[5])
        s = "SC_" + day + "_X"
        t = "SC_" + day + "_Y"
        z = sq.connect("Flight.db")
        z_c = z.cursor()
        z_c.execute("""INSERT INTO FlightSchedule 
                    (FlightID,ScheduleID,Date,Day,Origin,Destination,Departure,Arrival)
                    VALUES(?,?,?,?,?,?,?,?)""",
                    (details[6], s, details[5], day, details[0], details[1], details[3], details[4]))
        z.commit()
        jumbo = ["0,0,0", "0,0,0,0,0,0", "0,0,0,0,0,0,0,0,0"]
        mid = ["0,0", "0,0,0,0", "0,0,0,0,0,0"]
        light = ["0", "0,0", "0,0,0"]
        ft = details[2] + "@new"
        action = """INSERT INTO FlightOccupancy
                        (FlightID,ScheduleID1,ScheduleID2,Flighttype,FirstclassID1,BusinessclassID1,EconomyclassID1,FirstclassID2,BusinessclassID2,EconomyclassID2)
                        VALUES(?,?,?,?,?,?,?,?,?,?)"""
        if details[2] == "Jumbo":
            z_c.execute(action,
                        (ft, s, t, details[2], jumbo[0], jumbo[1], jumbo[2], jumbo[0], jumbo[1], jumbo[2]))
            z.commit()

        if details[2] == "Midsize":
            z_c.execute(action,
                        (ft, s, t, details[2], mid[0], mid[1], mid[2], mid[0], mid[1], mid[2]))
            z.commit()

        if details[2] == "Light":
            z_c.execute(action,
                        (ft, s, t, details[2], light[0], light[1], light[2], light[0], light[1], light[2]))
            z.commit()

    def checkoccupancy(self, date, filghtid):
        actual_day = findday(date)
        z = sq.connect("Flight.db")
        z_c = z.cursor()
        z_c.execute("SELECT * FROM FlightOccupancy")
        l = ""
        for k in z_c:
            if k[0] == filghtid and (k[1])[3:6] == actual_day:
                l = k[4] + "  -  " + k[5] + "  -  " + k[6]
                return l



    def checkingprofits(self, date):
        x_c.execute("SELECT * FROM Tickets")
        psum = 0.0

        for k in x_c:
            if k[3] == date:
                psum += k[5]
        return str(psum)


def getPassenger(userid):
    x_c.execute("SELECT * FROM passengers")
    for i in x_c:
        if i[0] == userid:
            temp = Passenger(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
            return temp

def getadmin(userid):
    y_c.execute("SELECT * FROM admins")
    for j in y_c:
        if j[0] == userid:
            adm = Admin(j[0],j[1],j[2],j[3])
            return adm

'''
if __name__ == '__main__':
    pass_1 = Passenger("dimpu123", "Dimpu", "sAMUWL", "Hyderabad")
    pass_2 = Passenger("sath123","Sath","SP","Kothagudem")
    pass_1.signup()
    pass_2.signup()

    print(login('Passenger',"sath123","SP"))

    x.close()
    y.close()
'''
