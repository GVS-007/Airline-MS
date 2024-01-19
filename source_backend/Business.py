class Business:
    def __init__(self,noofseats,luxtax):
        self.seats=[False]*noofseats
        self.luxtax=luxtax
    def book(self,seatno):
        self.seats[seatno-1]=True
    def occupancycount(self):
        count=0
        for x in self.seats:
            if x==True:
                count=count+1
        return count
    def setlux(self,luxtax):
        self.luxtax=luxtax
