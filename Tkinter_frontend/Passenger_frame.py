#Imports
from tkinter import *
from tkinter import Toplevel
from source_backend.UserClass import *
import sqlite3 as sq
from tkinter import messagebox as ms
from Tkinter_frontend.Passenger_Home import PassengerHome

class PassengerFrame:
    def __init__(self,root):
        self.root_frame = root

    def OpenPassengerWindow(self):
        #Creating a Toplevel window for passenger to login
        self.passengerWindow = Toplevel(self.root_frame, bg = "coral")
        self.passengerWindow.title("Passenger Login")
        self.passengerWindow.geometry("1200x630")
        self.passengerWindow.resizable(0,0)

        #userid and password attributes for the passengers
        self.userid = StringVar()
        self.passwrd = StringVar()

        #Label to show that this is a passenger login frame
        theLabel = Label(self.passengerWindow,text = "PASSENGER LOGIN PAGE", bd=10,bg='sky blue', padx=20, pady=10, width=70, font=('arial', 20, 'bold') )
        theLabel.pack()

        #Label for User ID
        userID_input_label = Label(self.passengerWindow, text="USER ID", bg="white", fg="black", width=10)
        userID_input_label.place(x=400, y=200)

        #Entrybox to enter UserID
        userID_input = Entry(self.passengerWindow, textvariable=self.userid, width=30, bd=2, insertborderwidth=2,bg="white", fg="black", selectbackground="light blue")
        userID_input.place(x=550, y=200)

        #Label for Password
        Password_input_label = Label(self.passengerWindow, text="PASSWORD", bg="white", fg="black", width=10)
        Password_input_label.place(x=400, y=270)

        #Entrybox to enter Password
        Password_input = Entry(self.passengerWindow, textvariable=self.passwrd, width=30, bd=2, insertborderwidth=2,bg="white", fg="black",selectbackground="light blue", show="*")
        Password_input.place(x=550, y=270)

        #Button for Login after entering the creditentials
        login_button = Button(self.passengerWindow,text = "LOGIN",bg = "sky blue",fg = "black",font = ("arial",20,"bold"),command = self.Login)
        login_button.place(x = 580, y = 350)

        #Button to signup into airline management system
        signup_button = Button(self.passengerWindow, text="SIGN UP", font = ("arial",20,"bold"), fg = "black", bg = "sky blue", command =self.OpenSignupWindow)
        signup_button.place(x = 400,y = 350)



    def OpenSignupWindow(self):
            self.signupWindow = Toplevel(self.root_frame, bg="grey")
            # self.passengerWindow.destroy()
            self.signupWindow.title("SIGN UP PAGE")
            self.signupWindow.geometry('1200x630+200+50')
            self.signupWindow.resizable(0,0)

            self.label0 = Label(self.signupWindow, text = "ENTER YOUR DETAILS", bg = "red",fg = "black", font=('arial', 30, 'bold'),height = 2,width = 30)
            self.label0.place(x = 0, y = 0)

            self.userID = StringVar()
            self.Name = StringVar()
            self.Password = StringVar()
            self.City = StringVar()
            self.phno = StringVar()
            self.dob = StringVar()
            self.emailid = StringVar()

            userID_input_label = Label(self.signupWindow,text = "USER ID",bg = "white",fg = "black",width = 10)
            userID_input_label.place(x = 100, y = 150)

            userID_input = Entry(self.signupWindow,textvariable = self.userID,width = 30,bd = 2,insertborderwidth = 2,bg = "white",fg = "black", selectbackground = "light blue")
            userID_input.place(x = 250, y = 150)

            Name_input_label = Label(self.signupWindow, text="NAME", bg="white", fg="black", width=10)
            Name_input_label.place(x=100, y=200)

            Name_input = Entry(self.signupWindow, textvariable = self.Name,width=30, bd=2, insertborderwidth=2, bg="white", fg="black",
                                 selectbackground="light blue")
            Name_input.place(x=250, y=200)

            Password_input_label = Label(self.signupWindow, text="PASSWORD", bg="white", fg="black", width=10)
            Password_input_label.place(x=100, y=250)

            Password_input = Entry(self.signupWindow, textvariable = self.Password,width=30, bd=2, insertborderwidth=2, bg="white", fg="black",
                                 selectbackground="light blue",show = "*")
            Password_input.place(x=250, y=250)


            City_input_label = Label(self.signupWindow, text="CITY", bg="white", fg="black", width=10)
            City_input_label.place(x=100, y=300)

            City_input = Entry(self.signupWindow, textvariable = self.City,width=30, bd=2, insertborderwidth=2, bg="white", fg="black",
                                   selectbackground="light blue")
            City_input.place(x=250, y=300)

            phno_input_label = Label(self.signupWindow, text="Phone number", bg="white", fg="black", width=10)
            phno_input_label.place(x=100, y=350)

            phno_input = Entry(self.signupWindow, textvariable = self.phno,width=30, bd=2, insertborderwidth=2, bg="white", fg="black",
                                   selectbackground="light blue")
            phno_input.place(x=250, y=350)

            dob_input_label = Label(self.signupWindow, text="Date of birth", bg="white", fg="black", width=10)
            dob_input_label.place(x=100, y=400)

            dob_input = Entry(self.signupWindow, textvariable = self.dob,width=30, bd=2, insertborderwidth=2, bg="white", fg="black",
                                   selectbackground="light blue")
            dob_input.place(x=250, y=400)

            email_input_label = Label(self.signupWindow, text="Email ID", bg="white", fg="black", width=10)
            email_input_label.place(x=100, y=450)

            email_input = Entry(self.signupWindow, textvariable = self.emailid,width=30, bd=2, insertborderwidth=2, bg="white", fg="black",
                                   selectbackground="light blue")
            email_input.place(x=250, y=450)

            submit_button = Button(self.signupWindow,text = "SUBMIT", bg = "white", fg = "black", width = 25, bd = 3,command = self.submit)
            submit_button.place(x = 400, y = 550)

    def submit(self):
        userID = self.userID.get()
        name = self.Name.get()
        password = self.Password.get()
        city = self.City.get()
        phno = self.phno.get()
        dob = self.dob.get()
        mailid = self.emailid.get()
        temp_passenger = Passenger(userID,name,password,city,phno,dob,mailid)
        temp_passenger.signup()

        self.userID.set("")
        self.Name.set("")
        self.Password.set("")
        self.City.set("")
        self.phno.set("")
        self.dob.set("")
        self.emailid.set("")

        self.signupWindow.destroy()
        PassengerHome(self.root_frame, temp_passenger)
        self.passengerWindow.destroy()


    def Login(self):
        userID = self.userid.get()
        password = self.passwrd.get()

        if userID=="" or password=="":
            ms.showerror("Error", "All fields are required")
            return

        the_pass_object = getPassenger(userID)
        if the_pass_object is None:
            ms.showerror('No record found', 'Incorrect UserID')
        elif the_pass_object.login(password):
            self.passengerWindow.destroy()
            PassengerHome(self.root_frame, the_pass_object)
        else:
            ms.showerror('Oops!', 'Incorrect UserID or Password!!. Try again')


        
