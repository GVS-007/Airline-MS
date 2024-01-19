import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from source_backend.Ticket import *
from tkinter import *
from source_backend.UserClass import *
from source_backend.Ticket import *


class PassengerHome:
    def __init__(self, root, passenger):
        self.root_frame = root
        self.my_home = tk.Toplevel(self.root_frame, bg="sky blue")
        self.my_home.title("Passenger Home Page")
        self.my_home.geometry('800x630')
        self.my_home.resizable(0, 0)
        self.passenger = passenger
        self.s = "Welcome" + " " + passenger.Name
        homepage_label = tk.Label(self.my_home, text=self.s, bd=10, bg='coral', padx=20, pady=10, width=70,
                                  font=('arial', 20, 'bold'))
        homepage_label.grid(row=0, column=0)
        update_button = tk.Button(self.my_home, text="Update Profile", bg="blue", font=('arial', 20, 'bold'),
                                  command=self.update)
        update_button.grid(row=3, column=0, columnspan=2, pady=10, padx=1)
        availability_button = tk.Button(self.my_home, text="Check Availability", bg="blue", font=('arial', 20, 'bold'),
                                        command=self.checkavailability)
        availability_button.grid(row=1, column=0, columnspan=2, pady=10, padx=1)
        cancelticket_button = tk.Button(self.my_home, text="Cancel Ticket", bg="blue", font=('arial', 20, 'bold'), command = self.displaytrips)
        cancelticket_button.grid(row=2, column=0, columnspan=2, pady=10, padx=1)
        logout_button = tk.Button(self.my_home, text="Logout", bg="blue", font=('arial', 20, 'bold'),
                                  command=self.my_home.destroy)
        logout_button.grid(row=4, column=0, columnspan=2, pady=10, padx=1)

    def update(self):
        self.updatewindow = tk.Toplevel(self.root_frame, bg="grey")
        self.updatewindow.title("SIGN UP PAGE")
        self.updatewindow.geometry('800x630')
        self.updatewindow.resizable(0, 0)

        self.label0 = tk.Label(self.updatewindow, text="UPDATE YOUR DETAILS", bg="white", font=('arial', 20),
                               fg="black", padx=20, pady=1, width=50)
        self.label0.place(x=0, y=0)

        self.userid = tk.StringVar()
        self.name = tk.StringVar()
        self.password = tk.StringVar()
        self.city = tk.StringVar()
        self.phno = tk.StringVar()
        self.dob = tk.StringVar()
        self.emailid = tk.StringVar()

        name_input_label = tk.Label(self.updatewindow, text="NAME", bg="white", fg="black", width=10)
        name_input_label.place(x=100, y=200)

        name_input = tk.Entry(self.updatewindow, textvariable=self.name, width=30, bd=2, insertborderwidth=2,
                              bg="white", fg="black",
                              selectbackground="lightblue")
        name_input.place(x=250, y=200)

        password_input_label = tk.Label(self.updatewindow, text="PASSWORD", bg="white", fg="black", width=10)
        password_input_label.place(x=100, y=250)

        password_input = tk.Entry(self.updatewindow, textvariable=self.password, width=30, bd=2, insertborderwidth=2,
                                  bg="white", fg="black",
                                  selectbackground="light blue", show="*")
        password_input.place(x=250, y=250)

        city_input_label = tk.Label(self.updatewindow, text="CITY", bg="white", fg="black", width=10)
        city_input_label.place(x=100, y=300)

        city_input = tk.Entry(self.updatewindow, textvariable=self.city, width=30, bd=2, insertborderwidth=2,
                              bg="white", fg="black",
                              selectbackground="light blue")
        city_input.place(x=250, y=300)

        phno_input_label = tk.Label(self.updatewindow, text="Phone number", bg="white", fg="black", width=10)
        phno_input_label.place(x=100, y=350)

        phno_input = tk.Entry(self.updatewindow, textvariable=self.phno, width=30, bd=2, insertborderwidth=2,
                              bg="white", fg="black",
                              selectbackground="light blue")
        phno_input.place(x=250, y=350)

        dob_input_label = tk.Label(self.updatewindow, text="Date of birth", bg="white", fg="black", width=10)
        dob_input_label.place(x=100, y=400)

        dob_input = tk.Entry(self.updatewindow, textvariable=self.dob, width=30, bd=2, insertborderwidth=2, bg="white",
                             fg="black",
                             selectbackground="light blue")
        dob_input.place(x=250, y=400)

        email_input_label = tk.Label(self.updatewindow, text="Email ID", bg="white", fg="black", width=10)
        email_input_label.place(x=100, y=450)

        email_input = tk.Entry(self.updatewindow, textvariable=self.emailid, width=30, bd=2, insertborderwidth=2,
                               bg="white", fg="black",
                               selectbackground="light blue")
        email_input.place(x=250, y=450)

        # userid_input.insert(0, self.passenger.userID)
        name_input.insert(0, self.passenger.Name)
        password_input.insert(0, self.passenger.password)
        city_input.insert(0, self.passenger.city)
        phno_input.insert(0, self.passenger.phonenumber)
        dob_input.insert(0, self.passenger.dob)
        email_input.insert(0, self.passenger.emailid)
        # print(list)
        submit_button = tk.Button(self.updatewindow, text="Update", bg="white", fg="black", width=25, bd=3,
                                  command=self.updating)
        submit_button.place(x=400, y=550)

        # self.updatewindow.destroy()

    def updating(self):
        self.list = [self.name.get(), self.password.get(), self.city.get(), self.phno.get(), self.dob.get(),
                     self.emailid.get()]
        self.passenger.update_profile(self.list)
        messagebox.showinfo("Udpate Profile", "Succesfully Updated")
        self.updatewindow.destroy()

    def checkavailability(self):
        self.addnew_home = tk.Toplevel(self.root_frame, bg="grey")
        self.addnew_home.title("Passenger Home Page")
        self.addnew_home.geometry('1200x630+200+50')
        # self.addnew_home.resizable(0,0)

        choose_label = tk.Label(self.addnew_home, text="Choose from below", bg="sky blue", fg="black", width=30,
                                height=2, font=('arial', 30, 'bold'))
        choose_label.place(x=300, y=0)

        # Label for From airport
        from_label = tk.Label(self.addnew_home, text="from Airport", bg="white", fg="black", width=10, height=2)
        from_label.place(x=50, y=150)
        # self.Drop down box for from aiport
        self.drop = ttk.Combobox(self.addnew_home, values=["Mumbai", "Kolkata", "Delhi", "Chennai"])
        self.drop.current(0)
        self.drop.place(x=150, y=150)

        # Label for to aiport
        to_label = tk.Label(self.addnew_home, text="To Airport", bg="white", fg="black", width=10, height=2)
        to_label.place(x=400, y=150)
        # self.Drop down box for To aiport
        self.dropto = ttk.Combobox(self.addnew_home, values=["Mumbai", "Kolkata", "Delhi", "Chennai"])
        self.dropto.current(0)
        self.dropto.place(x=500, y=150)

        # Label for Preffered class
        class_label = tk.Label(self.addnew_home, text="Preffered Class", bg="white", fg="black", width=12, height=2)
        class_label.place(x=770, y=150)
        # self.Drop down box for To airport
        self.dropclass = ttk.Combobox(self.addnew_home, values=["First class", "Business class", "Economic class"])
        self.dropclass.current(0)
        self.dropclass.place(x=890, y=150)

        # Label for date
        class_label = tk.Label(self.addnew_home, text="Date", bg="white", fg="black", width=12, height=2)
        class_label.place(x=450, y=250)
        # self.Drop down box for To airport
        self.dropdate = ttk.Combobox(self.addnew_home,
                                     values=["07/04/2021", "08/04/2021", "09/04/2021", "10/04/2021", "11/04/2021",
                                             "12/04/2021", "13/04/2021"])
        self.dropdate.current(0)
        self.dropdate.place(x=570, y=250)

        confirm_button = tk.Button(self.addnew_home, text="Confirm", bg="white", font=('arial', 20, 'bold'),
                                   command=self.confirm)
        confirm_button.place(x=530, y=450)

    def confirm(self):
        exit = messagebox.askyesno("Confirmatiom", "Are you sure to confirm!!")
        if exit > 0:
            self.theFLIGHT = getInfo(self.drop.get(), self.dropto.get(), self.dropdate.get(), self.dropclass.get())
            self.addnew_home.destroy()
            self.FlightsWindow = Toplevel(self.root_frame, bg="white")
            self.FlightsWindow.title("Avaliable Flights")
            self.FlightsWindow.geometry("1000x500")
            theFlight_details = ['FlightID', 'Flight Type', 'ScheduleID', 'DATE', 'DAY', 'FROM', 'DESTINATION',
                                 'DEPARTURE', 'ARRIVAL', 'Seat Class']
            for i in range(2):
                for j in range(len(self.theFLIGHT)):
                    self.e = Entry(self.FlightsWindow, width=12, fg='blue',
                                   font=('Arial', 10, 'bold'))
                    if i == 0:
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, theFlight_details[j])
                    else:
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, self.theFLIGHT[j])

            book_button = Button(self.FlightsWindow, text="BOOK TICKET", fg="black", borderwidth=3,
                                 command=self.seatselection)
            book_button.grid(row=1, column=11)

    def seatselection(self):
        seatClass = self.theFLIGHT[-1]
        flightType = self.theFLIGHT[1]

        self.seatWindow = Toplevel(self.FlightsWindow, bg="white")
        self.seatWindow.title("Seat selection window")
        self.seatWindow.geometry("300x300")

        self.seatno = StringVar()
        seat_label = Label(self.seatWindow, text = "Seat no.", fg = "black", width = 10)
        seat_label.place(x = 50, y = 100)
        seatchoosen = ttk.Combobox(self.seatWindow, textvariable = self.seatno,width = 10)
        if flightType == "Jumbo":
            if seatClass == "First class":
                seatchoosen['values'] = ['1','2','3']
            elif seatClass == "Business class":
                seatchoosen['values'] = ['1', '2', '3','4','5','6']
            else:
                seatchoosen['values'] = ['1', '2', '3','4','5','6','7','8','9']
        elif flightType == "Midsize":
            if seatClass == "First class":
                seatchoosen['values'] = ['1', '2']
            elif seatClass == "Business class":
                seatchoosen['values'] = ['1', '2', '3', '4']
            else:
                seatchoosen['values'] = ['1', '2', '3', '4', '5', '6']
        else:
            if seatClass == "First class":
                seatchoosen['values'] = ['1']
            elif seatClass == "Business class":
                seatchoosen['values'] = ['1', '2']
            else:
                seatchoosen['values'] = ['1', '2', '3']
        seatchoosen.current(0)
        seatchoosen.place(x = 100, y = 100)

        select_button = Button(self.seatWindow, text = "SELECT", fg = "black", highlightcolor = "sky blue", bd = 3, command = self.bookTicket)
        select_button.place(x = 150, y = 200)

    def bookTicket(self):
        seatNo = self.seatno.get()
        the_seat_number = int(seatNo)
        the_seat_number -= 1
        self.ticket_obj = Ticket(self.theFLIGHT, the_seat_number, self.passenger)
        k = self.ticket_obj.bookTicket()
        if k == 1:
            option = messagebox.askyesno("Booking Successful", "Make Payment?")
            if option:
                self.seatWindow.destroy()
                d = self.ticket_obj.computeFare()
                self.PaymentWindow = Toplevel(self.FlightsWindow, bg = "sky blue")
                self.PaymentWindow.title("Payment Window")
                self.PaymentWindow.geometry("400x200")
                thestr = "Ticket Fare is "+str(d)
                thelabel1 = Label(self.PaymentWindow, text = thestr, width = 30, bg = "white", fg = "black", borderwidth = 2)
                thelabel1.place(x = 20, y = 10)

                thepay_button = Button(self.PaymentWindow, text = "PAY", width = 10, bg = 'white', fg = "black",borderwidth = 2, command = self.payment)
                thepay_button.place(x = 100, y = 75)
        elif k == 2:
            messagebox.showerror("Booking Failed", "Seat already taken!")
        elif k == 0:
            messagebox.showerror("Booking Failed", "No seats avaliable!")
            self.seatWindow.destroy()
            self.FlightsWindow.destroy()

    def payment(self):
        messagebox.showinfo("OK","BOOKING SUCCESSFUL!")
        self.passenger.addticket(self.ticket_obj)
        self.PaymentWindow.destroy()
        self.FlightsWindow.destroy()

    def displaytrips(self):
       self.cancelTicketWindow = Toplevel(self.root_frame, bg = "sky blue")
       self.cancelTicketWindow.title("Ticket Cancellation Window")
       self.cancelTicketWindow.geometry("1200x500")

       self.trips = self.passenger.gettrips()
       names = ['TicketID', 'FlightID', 'ScheduleID', 'Date','Class Type', 'Ticket fare', 'Seat no']
       for i in range(len(self.trips)+1):
           for j in range(7):
               self.e = Entry(self.cancelTicketWindow, width=20, fg='blue',
                              font=('Arial', 10, 'bold'))
               self.e.grid(row=i, column=j)
               if i == 0:
                   self.e.insert(END, names[j])
               else:
                   self.e.insert(END, self.trips[i-1][j])

               if j == 6 and i != 0:
                   thestr = str(i)
                   cancel_button = Button(self.cancelTicketWindow, text=thestr, bg="white", fg="black", command = lambda r = i: self.cancelTicket(r))
                   cancel_button.grid(row=i, column=7)

    def cancelTicket(self, r):
        opt = messagebox.askyesno("Confirmation","Are you sure to cancel the ticket?")
        if opt:
            ticketid = self.trips[r-1][0]
            flightid = self.trips[r-1][1]
            scheduleid = self.trips[r-1][2]
            classType = self.trips[r-1][4]
            cancelTicket(ticketid, flightid, scheduleid, classType, self.passenger)
            messagebox.showinfo("Cancelled","The Ticket has been cancelled")
            self.cancelTicketWindow.destroy()
        else:
            pass

