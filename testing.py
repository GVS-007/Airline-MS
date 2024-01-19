from source_backend.Flight import Jumbo, Light ,Midsize
from source_backend.Ticket import Ticket
from source_backend.UserClass import *
#passenger object
testpassenger=Passenger("test1","passenger1","testpass","test","9"*9,"1/1/2001","test@test.com")
#admin object
testadmin=Admin("test2","admin1","testadmn","testp")
#3 types of flight objects
testjumbo=Jumbo("testid1")
testmid=Midsize("testid2")
testlight=Light("testid3")
#ticket1=Ticket(['Delhi','Kolkata',],1,testpassenger)
####################################################################################
##add passenger to database
testpassenger.signup()
##update profile in database by passing the details list
testpassenger.update_profile(['modpassenger','modtestpass','modtest','000000000','2/1/2001','modemail@m.com'])
##getting the modified passenger from database
modpass=getPassenger("test1")
##add a ticket to passenger database by passing a ticket
#testpassenger.addticket()
#trips=testpassenger.gettrips()
def printpass(passen):
    print(passen.userID,passen.Name,passen.password,passen.city,passen.phonenumber,passen.dob,passen.emailid)
def Test():
    printpass(testpassenger)
    printpass(modpass)
    #print(trips)