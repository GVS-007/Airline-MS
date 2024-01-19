#the_backend classes and functionalities.
from source_backend.Economy import Economy
from source_backend.Business import Business
from source_backend.Firstclass import Firstclass
import sqlite3 as sq
x = sq.connect("rates.db")


x_c = x.cursor()


class Flight:
    def __init__(self,flightid,basicprice,costperkm):
        self.flightID=flightid
        self.basicprice=basicprice
        self.costperkm=costperkm
        self.trips=[]

    def setcostkm(self, new_costofkm):
        self.costperkm = new_costofkm

    def totaloccupancy(self):
        occ=self.enconomyclass.occupancycount()+self.businessclass.occupancycount()+self.firstclass.occupancycount()
        occ=occ*100/(len(self.firstclass.seats)+len(self.businessclass.seats)+len(self.enconomyclass.seats))
        return occ
    #def profits(self):
      #  profit=0
      #  for x in self.firstclass.seats:
        #    if x:
         #       profit=profit+f

class Jumbo(Flight):
    def __init__(self,flightid):
        x_c.execute("SELECT * FROM flightrates WHERE type='JUMBO'")
        i = x_c.fetchone()
        baseprice=i[1]
        costperkm=i[2]
        firlux=i[3]
        bizlux=i[4]
        super().__init__(flightid,baseprice,costperkm)
        self.firstclass=Firstclass(3,firlux)
        self.businessclass=Business(6,bizlux)
        self.enconomyclass = Economy(9,0)


class Midsize(Flight):
    def __init__(self,flightid):
        x_c.execute("SELECT * FROM flightrates WHERE type='MID'")
        i=x_c.fetchone()
        baseprice=i[1]
        costperkm=i[2]
        firlux=i[3]
        bizlux=i[4]
        super().__init__(flightid,baseprice,costperkm)
        self.firstclass=Firstclass(2,firlux)
        self.businessclass=Business(4,bizlux)
        self.enconomyclass = Economy(6,0)


class Light(Flight):
    def __init__(self,flightid):
        x_c.execute("SELECT * FROM flightrates WHERE type='LIGHT'")
        i = x_c.fetchone()
        baseprice=i[1]
        costperkm=i[2]
        firlux=i[3]
        bizlux=i[4]
        super().__init__(flightid,baseprice,costperkm)
        self.firstclass=Firstclass(1,firlux)
        self.businessclass=Business(2,bizlux)
        self.enconomyclass = Economy(3,0)

def update_prices(list):
        if list[0] != "":
            x_c.execute("UPDATE flightrates SET baseprice = ? WHERE type = ?",(list[0],"JUMBO"))
        if list[4] != "":
            x_c.execute("UPDATE flightrates SET baseprice = ? WHERE type = ?",(list[4],"MID"))
        if list[8] != "":
            x_c.execute("UPDATE flightrates SET baseprice = ? WHERE type = ?",(list[8],"LIGHT"))
        if list[1] != "":
            x_c.execute("UPDATE flightrates SET perkm = ? WHERE type = ?",(list[1],"JUMBO"))
        if list[5] != "":
            x_c.execute("UPDATE flightrates SET perkm = ? WHERE type = ?",(list[5],"MID"))
        if list[9] != "":
            x_c.execute("UPDATE flightrates SET perkm = ? WHERE type = ?",(list[9],"LIGHT"))
        if list[2] != "":
            x_c.execute("UPDATE flightrates SET luxfirst = ? WHERE type = ?",(list[2],"JUMBO"))
        if list[6] != "":
            x_c.execute("UPDATE flightrates SET luxfirst = ? WHERE type = ?",(list[6],"MID"))
        if list[10] != "":
            x_c.execute("UPDATE flightrates SET luxfirst = ? WHERE type = ?",(list[10],"LIGHT"))
        if list[3] != "":
            x_c.execute("UPDATE flightrates SET luxb = ? WHERE type = ?",(list[3],"JUMBO"))
        if list[7] != "":
            x_c.execute("UPDATE flightrates SET luxb = ? WHERE type = ?",(list[7],"MID"))
        if list[11] != "":
            x_c.execute("UPDATE flightrates SET luxb = ? WHERE type = ?",(list[11],"LIGHT"))
        x.commit()
class Pricelist():
    def __init__(self):
        x_c.execute("SELECT * from flightrates")
        i=x_c.fetchall()
        self.jcpk=i[0][2]
        self.jbp=i[0][1]
        self.jflt=i[0][3]
        self.jblt=i[0][4]
        self.mcpk=i[1][2]
        self.mbp=i[1][1]
        self.mflt=i[1][3]
        self.mblt=i[1][4]
        self.lcpk=i[2][2]
        self.lbp=i[2][1]
        self.lflt=i[2][3]
        self.lblt=i[2][4]



