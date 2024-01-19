import sqlite3 as sq
from source_backend import *
from source_backend.Flight import *

city = sq.connect("City.db")
ci_c = city.cursor()

flight = sq.connect("Flight.db")
fi_c = flight.cursor()

passenger = sq.connect("passenger.db")
ps_c = passenger.cursor()


class Ticket:
    def __init__(self, theList, seatno, Passenger):
        self.theList = theList
        self.ticketID = theList[0]+"-"+theList[2]+"-"+str(seatno)
        self.flightID = theList[0]
        self.scheduleID = theList[2]
        self.date = theList[3]
        self.classType = theList[-1]
        self.seatno = seatno
        self.distance = 0
        self.duration = 0
        self.ticketprice = 1.0


    def bookTicket(self):
        fi_c.execute("SELECT * FROM FlightOccupancy WHERE FlightID = ? AND ScheduleID1 = ?",(self.flightID,self.scheduleID))
        for i in fi_c:
            if self.classType == "First class":
                thearray_1 = i[4].split(",")
                flag = False
                for g in thearray_1:
                    if g == "0":
                        flag = True
                if flag:
                    if thearray_1[self.seatno] == "0":
                        thearray_1[self.seatno] = "1"
                        the_string = ""
                        for j in range(len(thearray_1)):
                            the_string += thearray_1[j] + ","
                        the_string_final = the_string[:-1]
                        fi_c.execute("UPDATE FlightOccupancy SET FirstclassID1 = ? WHERE FlightID = ? AND ScheduleID1 = ?",
                                     (the_string_final, self.flightID, self.scheduleID))
                        flight.commit()
                        return 1
                    else:
                        return 2
                else:
                    return 0
            if self.classType == "Business class":
                thearray_1 = i[5].split(",")
                flag = False
                for g in thearray_1:
                    if g == "0":
                        flag = True
                if flag:
                    if thearray_1[self.seatno] == "0":
                        thearray_1[self.seatno] = "1"
                        the_string = ""
                        for j in range(len(thearray_1)):
                            the_string += thearray_1[j] + ","
                        the_string_final = the_string[:-1]
                        fi_c.execute("UPDATE FlightOccupancy SET BusinessclassID1 = ? WHERE FlightID = ? AND ScheduleID1 = ?",
                                     (the_string_final, self.flightID, self.scheduleID))
                        flight.commit()
                        return 1
                    else:
                        return 2
                else:
                    return 0
            if self.classType == "Economic class":
                thearray_1 = i[6].split(",")
                flag = False
                for g in thearray_1:
                    if g == "0":
                        flag = True
                if flag:
                    if thearray_1[self.seatno] == "0":
                        thearray_1[self.seatno] = "1"
                        the_string = ""
                        for j in range(len(thearray_1)):
                            the_string += thearray_1[j] + ","
                        the_string_final = the_string[:-1]
                        fi_c.execute("UPDATE FlightOccupancy SET EconomyclassID1 = ? WHERE FlightID = ? AND ScheduleID1 = ?",
                                     (the_string_final, self.flightID,self.scheduleID))
                        flight.commit()
                        return 1
                    else:
                        return 2
                else:
                    return 0
        fi_c.execute("SELECT * FROM FlightOccupancy WHERE FlightID = ? AND ScheduleID2 = ?",
                     (self.flightID, self.scheduleID))
        for i in fi_c:
            if self.classType == "First class":
                thearray_1 = i[7].split(",")
                flag = False
                for g in thearray_1:
                    if g == "0":
                        flag = True
                if flag:
                    if thearray_1[self.seatno] == "0":
                        thearray_1[self.seatno] = "1"
                        the_string = ""
                        for j in range(len(thearray_1)):
                            the_string += thearray_1[j] + ","
                        the_string_final = the_string[:-1]
                        fi_c.execute("UPDATE FlightOccupancy SET FirstclassID2 = ? WHERE FlightID = ? AND ScheduleID2 = ?",
                                     (the_string_final, self.flightID, self.scheduleID))
                        flight.commit()
                        return 1
                    else:
                        return 2
                else:
                    return 0
            if self.classType == "Business class":
                thearray_1 = i[8].split(",")
                flag = False
                for g in thearray_1:
                    if g == "0":
                        flag = True
                if flag:
                    if thearray_1[self.seatno] == "0":
                        thearray_1[self.seatno] = "1"
                        the_string = ""
                        for j in range(len(thearray_1)):
                            the_string += thearray_1[j] + ","
                        the_string_final = the_string[:-1]
                        fi_c.execute("UPDATE FlightOccupancy SET BusinessclassID2 = ? WHERE FlightID = ? AND ScheduleID2 = ?",
                                     (the_string_final, self.flightID, self.scheduleID))
                        flight.commit()
                        return 1
                    else:
                        return 2
                else:
                    return 0
            if self.classType == "Economic class":
                thearray_1 = i[9].split(",")
                flag = False
                for g in thearray_1:
                    if g == "0":
                        flag = True
                if flag:
                    if thearray_1[self.seatno] == "0":
                        thearray_1[self.seatno] = "1"
                        the_string = ""
                        for j in range(len(thearray_1)):
                            the_string += thearray_1[j] + ","
                        the_string_final = the_string[:-1]
                        fi_c.execute("UPDATE FlightOccupancy SET EconomyclassID2 = ? WHERE FlightID = ? AND ScheduleID2 = ?",
                                     (the_string_final, self.flightID, self.scheduleID))
                        flight.commit()
                        return 1
                    else:
                        return 2
                else:
                    return 0


    def computeFare(self):
        ci_c.execute("SELECT * FROM Citygrid")
        for k in ci_c.fetchall():
            flag1 = (k[0] == self.theList[5] and k[1] == self.theList[6])
            flag2 = (k[0] == self.theList[6] and k[1] == self.theList[5])
            if flag1 or flag2:
                self.distance = k[2]
                self.duration = k[3]
                break

        if self.theList[1] == "Jumbo":
            the_flight_obj = Jumbo(self.flightID)
            self.ticketprice = the_flight_obj.basicprice
            if self.classType == "First class":
                lux_tax = the_flight_obj.firstclass.luxtax
                self.ticketprice += (the_flight_obj.costperkm*self.distance)
                self.ticketprice *= (1+lux_tax)
            elif self.classType == "Business class":
                lux_tax = the_flight_obj.businessclass.luxtax
                self.ticketprice += (the_flight_obj.costperkm * self.distance)
                self.ticketprice *= (1 + lux_tax)
            elif self.classType == "Economic class":
                lux_tax = the_flight_obj.enconomyclass.luxtax
                self.ticketprice += (the_flight_obj.costperkm * self.distance)
                self.ticketprice *= (1 + lux_tax)
        elif self.theList[1] == "Midsize":
            the_flight_obj = Midsize(self.flightID)
            self.ticketprice = the_flight_obj.basicprice
            if self.classType == "First class":
                lux_tax = the_flight_obj.firstclass.luxtax
                self.ticketprice += (the_flight_obj.costperkm * self.distance)
                self.ticketprice *= (1 + lux_tax)
            elif self.classType == "Business class":
                lux_tax = the_flight_obj.businessclass.luxtax
                self.ticketprice += (the_flight_obj.costperkm * self.distance)
                self.ticketprice *= (1 + lux_tax)
            elif self.classType == "Economic class":
                lux_tax = the_flight_obj.enconomyclass.luxtax
                self.ticketprice += (the_flight_obj.costperkm * self.distance)
                self.ticketprice *= (1 + lux_tax)
        else:
            the_flight_obj = Light(self.flightID)
            self.ticketprice = the_flight_obj.basicprice
            if self.classType == "First class":
                lux_tax = the_flight_obj.firstclass.luxtax
                self.ticketprice += (the_flight_obj.costperkm * self.distance)
                self.ticketprice *= (1 + lux_tax)
            elif self.classType == "Business class":
                lux_tax = the_flight_obj.businessclass.luxtax
                self.ticketprice += (the_flight_obj.costperkm * self.distance)
                self.ticketprice *= (1 + lux_tax)
            elif self.classType == "Economic class":
                lux_tax = the_flight_obj.enconomyclass.luxtax
                self.ticketprice += (the_flight_obj.costperkm * self.distance)
                self.ticketprice *= (1 + lux_tax)

        return self.ticketprice




def cancelTicket(ticketid, flightid, scheduleid, classType, Passenger):
    ps_c.execute("SELECT * FROM Tickets WHERE TicketID = ? AND FlightID = ?", (ticketid, flightid))
    j = ps_c.fetchone()
    ps_c.execute("DELETE FROM Tickets WHERE TicketID = ? AND FlightID = ?", (ticketid, flightid))
    passenger.commit()
    ps_c.execute("SELECT * FROM passengers WHERE userID = ? AND city = ?", (Passenger.userID, Passenger.city))
    i = ps_c.fetchone()
    temp = i[7].split(",")
    newidstr = ""
    if len(temp) == 1:
        finalstr = "0"
    else:
        for id in temp:
            if id == ticketid:
                pass
            else:
                newidstr += (id + ",")
        finalstr = newidstr[:-1]
    ps_c.execute("UPDATE passengers SET TicketID = ? WHERE userID = ?", (finalstr, Passenger.userID))
    passenger.commit()

    seatno = j[6]
    seatno -= 1


    fi_c.execute("SELECT * FROM FlightOccupancy WHERE FlightID = ? AND ScheduleID1 = ?",(flightid, scheduleid))
    k = fi_c.fetchone()
    if k is not None:
        if classType == "First class":
            thearray_1 = k[4].split(",")
            if thearray_1[seatno] == "1":
                thearray_1[seatno] = "0"
                the_string = ""
                for j in range(len(thearray_1)):
                    the_string += thearray_1[j] + ","
                the_string_final = the_string[:-1]
                fi_c.execute("UPDATE FlightOccupancy SET FirstclassID1 = ? WHERE FlightID = ? AND ScheduleID1 = ?",
                             (the_string_final, flightid, scheduleid))
                flight.commit()
        elif classType == "Business class":
            thearray_1 = k[5].split(",")
            if thearray_1[seatno] == "1":
                thearray_1[seatno] = "0"
                the_string = ""
                for j in range(len(thearray_1)):
                    the_string += thearray_1[j] + ","
                the_string_final = the_string[:-1]
                fi_c.execute("UPDATE FlightOccupancy SET BusinessclassID1 = ? WHERE FlightID = ? AND ScheduleID1 = ?",
                             (the_string_final, flightid, scheduleid))
                flight.commit()
        elif classType == "Economic class":
            thearray_1 = k[6].split(",")
            if thearray_1[seatno] == "1":
                thearray_1[seatno] = "0"
                the_string = ""
                for j in range(len(thearray_1)):
                    the_string += thearray_1[j] + ","
                the_string_final = the_string[:-1]
                fi_c.execute("UPDATE FlightOccupancy SET EconomyclassID1 = ? WHERE FlightID = ? AND ScheduleID1 = ?",
                             (the_string_final, flightid, scheduleid))
                flight.commit()

    fi_c.execute("SELECT * FROM FlightOccupancy WHERE FlightID = ? AND ScheduleID2 = ?", (flightid, scheduleid))
    k = fi_c.fetchone()
    if k is not None:
        if classType == "First class":
            thearray_1 = k[7].split(",")
            if thearray_1[seatno] == "1":
                thearray_1[seatno] = "0"
                the_string = ""
                for j in range(len(thearray_1)):
                    the_string += thearray_1[j] + ","
                the_string_final = the_string[:-1]
                fi_c.execute("UPDATE FlightOccupancy SET FirstclassID2 = ? WHERE FlightID = ? AND ScheduleID1 = ?",
                             (the_string_final, flightid, scheduleid))
                flight.commit()
        elif classType == "Business class":
            thearray_1 = k[8].split(",")
            if thearray_1[seatno] == "1":
                thearray_1[seatno] = "0"
                the_string = ""
                for j in range(len(thearray_1)):
                    the_string += thearray_1[j] + ","
                the_string_final = the_string[:-1]
                fi_c.execute("UPDATE FlightOccupancy SET BusinessclassID2 = ? WHERE FlightID = ? AND ScheduleID1 = ?",
                             (the_string_final, flightid, scheduleid))
                flight.commit()
        elif classType == "Economic class":
            thearray_1 = k[9].split(",")
            if thearray_1[seatno] == "1":
                thearray_1[seatno] = "0"
                the_string = ""
                for j in range(len(thearray_1)):
                    the_string += thearray_1[j] + ","
                the_string_final = the_string[:-1]
                fi_c.execute("UPDATE FlightOccupancy SET EconomyclassID2 = ? WHERE FlightID = ? AND ScheduleID1 = ?",
                             (the_string_final, flightid, scheduleid))
                flight.commit()


def getInfo(origin, destination, date, classType):
    fi_c.execute("SELECT * FROM FlightSchedule WHERE Date = ? AND Origin = ? AND Destination = ?",(date, origin, destination))
    List = []
    theScheduleID = ""
    theFlightID = ""
    for i in fi_c.fetchall():
        theScheduleID = i[1]
        List.append(i[1])
        List.append(i[2])
        List.append(i[3])
        List.append(i[4])
        List.append(i[5])
        List.append(i[6])
        List.append(i[7])

    fi_c.execute("SELECT * FROM FlightOccupancy WHERE ScheduleID1 = ? OR ScheduleID2 = ?", (theScheduleID,theScheduleID))
    for j in fi_c.fetchall():
        theFlightID = j[0]
        List.insert(0,j[0])
        List.insert(1,j[3])
    List.append(classType)
    return List

'''
if __name__ == '__main__':
    getInfo("Mumbai", "Delhi", "08/04/2021", "FirstClass")
'''
        
