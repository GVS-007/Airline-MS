import tkinter as tk
from tkinter import Label, ttk
from tkinter import messagebox

from source_backend.Flight import Pricelist, update_prices


class AdminHome:
    def __init__(self,root,admin):
        self.root_frame = root
        self.admin_home = tk.Toplevel(self.root_frame, bg="black")
        self.admin_home.title("Administrator Home Page")
        self.admin_home.geometry('1200x630+200+50')
        self.admin_home.resizable(0,0)
        self.admin = admin
        self.s = "Welcome" + " "+ self.admin.Name
        self.pricelist = Pricelist()
        homepage_label = tk.Label(self.admin_home, text=self.s, bd=10,bg='green', padx=20, pady=10, width=70, font=('arial', 20, 'bold') )
        homepage_label.grid(row=0, column=0)
        newflight_button = tk.Button(self.admin_home, text="Add new flight", padx=20, pady=10, bg="blue",font=('arial', 20, 'bold'), command=self.add_newflight)
        newflight_button.grid(row=1, column=0,columnspan=2, pady=10, padx=1)
        occupancy_button = tk.Button(self.admin_home, text="Check Occupancy", padx=20, pady=10, bg="blue",font=('arial', 20, 'bold'), command = self.checkoccupancy)
        occupancy_button.grid(row=2, column=0,columnspan=2, pady=10, padx=1)
        profits_button = tk.Button(self.admin_home, text="Check profits", padx=20, pady=10, bg="blue",font=('arial', 20, 'bold'), command = self.checkprofits)
        profits_button.grid(row=3, column=0,columnspan=2, pady=10, padx=1)
        modify_ticket_price_button = tk.Button(self.admin_home, text="modify ticket price", padx=20, pady=10, bg="blue",font=('arial', 20, 'bold'), command = self.modifyticketprice)
        modify_ticket_price_button.grid(row=4, column=0,columnspan=2, pady=10, padx=1)
        logout_button = tk.Button(self.admin_home, text="Logout", bg="blue",font=('arial', 20, 'bold'), command=self.admin_home.destroy)
        logout_button.grid(row=5, column=0,columnspan=2, pady=10, padx=1)

    def add_newflight(self):
        self.addnew_home = tk.Toplevel(self.root_frame, bg="black")
        self.addnew_home.title("Administrator Home Page")
        self.addnew_home.geometry('1200x630+200+50')
        self.addnew_home.resizable(0, 0)

        self.fromtime = tk.StringVar()
        self.totime = tk.StringVar()
        self.flightid = tk.StringVar()

        from_label = Label(self.addnew_home, text="from Station", bg="SeaGreen1", fg="black", width=10, height=2)
        from_label.place(x=50, y=100)
        # Drop down box
        self.drop = ttk.Combobox(self.addnew_home, values=["Mumbai", "Kolkata", "Delhi", "Chennai"])
        self.drop.current(0)
        self.drop.place(x=150, y=100)

        to_label = Label(self.addnew_home, text="To Station", bg="SeaGreen1", fg="black", width=10, height=2)
        to_label.place(x=350, y=100)
        # Drop down box
        self.dropto = ttk.Combobox(self.addnew_home, values=["Mumbai", "Kolkata", "Delhi", "Chennai"])
        self.dropto.current(0)
        self.dropto.place(x=450, y=100)

        type_label = Label(self.addnew_home, text="Type of flight", bg="SeaGreen1", fg="black", width=10, height=2)
        type_label.place(x=650, y=100)
        # Drop down box
        self.typeof = ttk.Combobox(self.addnew_home, values=["Jumbo", "Midsize", "Light"])
        self.typeof.current(0)
        self.typeof.place(x=750, y=100)

        # from time
        from_time = Label(self.addnew_home, text="Departure time", bg="SeaGreen1", fg="black", width=10, height=2)
        from_time.place(x=50, y=250)
        # Entry box
        self.from_input = tk.Entry(self.addnew_home, textvariable=self.fromtime, width=20, bd=2, insertborderwidth=2,
                                   bg="white", fg="black",
                                   selectbackground="light blue")
        self.from_input.place(x=150, y=250)

        # To time
        to_time = Label(self.addnew_home, text="Arrival time", bg="SeaGreen1", fg="black", width=10, height=2)
        to_time.place(x=300, y=250)
        self.totime_input = tk.Entry(self.addnew_home, textvariable=self.totime, width=20, bd=2, insertborderwidth=2,
                                     bg="white", fg="black",
                                     selectbackground="light blue")
        self.totime_input.place(x=400, y=250)

        # Label for date
        class_label = tk.Label(self.addnew_home, text="Date", bg="SeaGreen1", fg="black", width=12, height=2)
        class_label.place(x=550, y=250)
        # Drop down box for Date
        self.dropdate = ttk.Combobox(self.addnew_home,
                                     values=["07/04/2021", "08/04/2021", "09/04/2021", "10/04/2021", "11/04/2021",
                                             "12/04/2021", "13/04/2021"])
        self.dropdate.current(0)
        self.dropdate.place(x=650, y=250)

        flight_id = Label(self.addnew_home, text="Flight ID", bg="SeaGreen1", fg="black", width=10, height=2)
        flight_id.place(x=300, y=350)
        self.flightid_input = tk.Entry(self.addnew_home, textvariable=self.flightid, width=20, bd=2,
                                       insertborderwidth=2,
                                       bg="white", fg="black",
                                       selectbackground="light blue")
        self.flightid_input.place(x=400, y=350)

        # Button to submit the additions
        submit = tk.Button(self.addnew_home, text="Add flight", bg="blue", font=('arial', 20, 'bold'),
                           command=self.adding_flight)
        submit.place(x=650, y=450)

    def adding_flight(self):
        self.admin_home.destroy()
        if self.from_input.get() == "" or self.totime_input.get() == "":
            messagebox.showerror("Error", "Time Not Entered!!")
            return
        self.flight_details = [self.drop.get(), self.dropto.get(), self.typeof.get(), self.from_input.get(),
                               self.totime_input.get(), self.dropdate.get(), self.flightid_input.get()]
        self.admin.addflight(self.flight_details)

        messagebox.showinfo("Success", "Flight added succesfully")
        self.addnew_home.destroy()

    def checkoccupancy(self):
        self.addnew_home = tk.Toplevel(self.root_frame, bg="black")
        self.addnew_home.title("Administrator check occupancy window")
        self.addnew_home.geometry('1200x630+200+50')
        self.addnew_home.resizable(0, 0)
        self.id = tk.StringVar()

        date_label = Label(self.addnew_home, text="Date", bg="SeaGreen1", fg="black", width=8, height=2, font=(20))
        date_label.place(x=50, y=100)

        # Drop down box for Date
        self.date = ttk.Combobox(self.addnew_home,
                                 values=["07/04/2021", "08/04/2021", "09/04/2021", "10/04/2021", "11/04/2021",
                                         "12/04/2021", "13/04/2021"])
        self.date.current(0)
        self.date.place(x=150, y=100)

        # flight id
        date_label = Label(self.addnew_home, text="Flight ID", bg="SeaGreen1", fg="black", width=8, height=2, font=(20))
        date_label.place(x=300, y=100)

        self.identry = tk.Entry(self.addnew_home, textvariable=self.id, width=20, bd=2, insertborderwidth=2, bg="white",
                                fg="black", selectbackground="light blue")
        self.identry.place(x=400, y=100)

        # submit button
        submit = tk.Button(self.addnew_home, text="Submit", bg="blue", font=('arial', 20, 'bold'),
                           command=self.checking)
        submit.place(x=250, y=250)

    def checking(self):
        L = "FirstClass - BusinessClass - EconomyClass\n" + self.admin.checkoccupancy(self.date.get(),
                                                                                      self.identry.get())
        # Label to display Occupancies
        from_label = Label(self.addnew_home, text=L, bg="black", fg="white", width=40, height=20, font=(20))
        from_label.place(x=650, y=100)

    def checkprofits(self):
        self.addnew_home = tk.Toplevel(self.root_frame, bg="black")
        self.addnew_home.title("Administrator checkprofits window")
        self.addnew_home.geometry('1200x630+200+50')
        self.addnew_home.resizable(0,0)
        date_label = Label(self.addnew_home, text="Date", bg="SeaGreen1", fg="black", width=8, height=2, font=(20))
        date_label.place(x=50, y=100)
        # Drop down box for Date
        self.date = ttk.Combobox(self.addnew_home, values=["07/04/2021", "08/04/2021", "09/04/2021", "10/04/2021", "11/04/2021", "12/04/2021", "13/04/2021" ])
        self.date.current(0)
        self.date.place(x=150, y=100)
        # submit button
        submit = tk.Button(self.addnew_home, text="Submit",  bg="blue",font=('arial', 20, 'bold'),command = self.checkingprofits)
        submit.place(x=250, y=250)

    def checkingprofits(self):
        psum = "Profits\n" + self.admin.checkingprofits(self.date.get())
        from_label = Label(self.addnew_home, text=psum, bg="black", fg="white", width=40, height=20, font=20)
        from_label.place(x=550, y=10)

    def modifyticketprice(self):
        self.pricewindow = tk.Toplevel(self.root_frame, bg="black")
        self.pricewindow.title("Administrator modify ticketprice window")
        self.pricewindow.geometry('1200x630+200+50')
        self.pricewindow.resizable(0, 0)
        self.label0 = tk.Label(self.pricewindow, text="   UPDATE TICKET PRICING SCHEME ", bg="white",
                               font=('arial', 20),
                               fg="black", padx=20, pady=1, width=63)
        self.label0.place(x=0, y=0)

        self.JCostperkm = tk.StringVar()
        self.JBaseprice = tk.StringVar()
        self.JluxF = tk.StringVar()
        self.JluxB = tk.StringVar()
        self.MCostperkm = tk.StringVar()
        self.MBaseprice = tk.StringVar()
        self.MluxF = tk.StringVar()
        self.MluxB = tk.StringVar()
        self.LCostperkm = tk.StringVar()
        self.LBaseprice = tk.StringVar()
        self.LluxF = tk.StringVar()
        self.LluxB = tk.StringVar()
        x = tk.Label(self.pricewindow, text="   JUMBO", bg="white", fg="black", width=26)
        x.place(x=100, y=150)
        y = tk.Label(self.pricewindow, text=" MID SIZED", bg="white", fg="black", width=26)
        y.place(x=300, y=150)
        x = tk.Label(self.pricewindow, text="   LIGHT", bg="white", fg="black", width=26)
        x.place(x=500, y=150)

        x1 = tk.Label(self.pricewindow, text="COST PER KM:", bg="white", fg="black", width=20)
        x1.place(x=100, y=250)

        jcpk = tk.Entry(self.pricewindow, textvariable=self.JCostperkm, width=5, bd=2, insertborderwidth=2,
                        bg="white", fg="black",
                        selectbackground="lightblue")
        jcpk.place(x=250, y=250)

        x2 = tk.Label(self.pricewindow, text="BASE PRICE", bg="white", fg="black", width=20)
        x2.place(x=100, y=200)

        jbp = tk.Entry(self.pricewindow, textvariable=self.JBaseprice, width=5, bd=2, insertborderwidth=2,
                       bg="white", fg="black",
                       selectbackground="light blue")
        jbp.place(x=250, y=200)

        x3 = tk.Label(self.pricewindow, text="FIRSTCLASS LUXTAX", bg="white", fg="black", width=20)
        x3.place(x=100, y=300)

        jflt = tk.Entry(self.pricewindow, textvariable=self.JluxF, width=5, bd=2, insertborderwidth=2,
                        bg="white", fg="black",
                        selectbackground="light blue")
        jflt.place(x=250, y=300)

        x4 = tk.Label(self.pricewindow, text="BIZCLASS LUXTAX", bg="white", fg="black", width=20)
        x4.place(x=100, y=350)

        jblt = tk.Entry(self.pricewindow, textvariable=self.JluxB, width=5, bd=2, insertborderwidth=2,
                        bg="white", fg="black",
                        selectbackground="light blue")
        jblt.place(x=250, y=350)

        ##############                                                                  ###########

        y1 = tk.Label(self.pricewindow, text="COST PER KM:", bg="white", fg="black", width=20)
        y1.place(x=300, y=250)

        mcpk = tk.Entry(self.pricewindow, textvariable=self.MCostperkm, width=5, bd=2, insertborderwidth=2,
                        bg="white", fg="black",
                        selectbackground="lightblue")
        mcpk.place(x=450, y=250)

        y2 = tk.Label(self.pricewindow, text="BASE PRICE", bg="white", fg="black", width=20)
        y2.place(x=300, y=200)

        mbp = tk.Entry(self.pricewindow, textvariable=self.MBaseprice, width=5, bd=2, insertborderwidth=2,
                       bg="white", fg="black",
                       selectbackground="light blue")
        mbp.place(x=450, y=200)

        y3 = tk.Label(self.pricewindow, text="FIRSTCLASS LUXTAX", bg="white", fg="black", width=20)
        y3.place(x=300, y=300)

        mflt = tk.Entry(self.pricewindow, textvariable=self.MluxF, width=5, bd=2, insertborderwidth=2,
                        bg="white", fg="black",
                        selectbackground="light blue")
        mflt.place(x=450, y=300)

        y4 = tk.Label(self.pricewindow, text="BIZCLASS LUXTAX", bg="white", fg="black", width=20)
        y4.place(x=300, y=350)

        mblt = tk.Entry(self.pricewindow, textvariable=self.MluxB, width=5, bd=2, insertborderwidth=2,
                        bg="white", fg="black",
                        selectbackground="light blue")
        mblt.place(x=450, y=350)

        #############                                                      #######################

        z1 = tk.Label(self.pricewindow, text="COST PER KM:", bg="white", fg="black", width=20)
        z1.place(x=500, y=250)

        lcpk = tk.Entry(self.pricewindow, textvariable=self.LCostperkm, width=5, bd=2, insertborderwidth=2,
                        bg="white", fg="black",
                        selectbackground="lightblue")
        lcpk.place(x=650, y=250)

        z2 = tk.Label(self.pricewindow, text="BASE PRICE", bg="white", fg="black", width=20)
        z2.place(x=500, y=200)

        lbp = tk.Entry(self.pricewindow, textvariable=self.LBaseprice, width=5, bd=2, insertborderwidth=2,
                       bg="white", fg="black",
                       selectbackground="light blue")
        lbp.place(x=650, y=200)

        z3 = tk.Label(self.pricewindow, text="FIRSTCLASS LUXTAX", bg="white", fg="black", width=20)
        z3.place(x=500, y=300)

        lflt = tk.Entry(self.pricewindow, textvariable=self.LluxF, width=5, bd=2, insertborderwidth=2,
                        bg="white", fg="black",
                        selectbackground="light blue")
        lflt.place(x=650, y=300)

        z4 = tk.Label(self.pricewindow, text="BIZCLASS LUXTAX", bg="white", fg="black", width=20)
        z4.place(x=500, y=350)

        lblt = tk.Entry(self.pricewindow, textvariable=self.LluxB, width=5, bd=2, insertborderwidth=2,
                        bg="white", fg="black",
                        selectbackground="light blue")
        lblt.place(x=650, y=350)
        #####################                                              ###########################
        jcpk.insert(0, Pricelist().jcpk)
        jbp.insert(0, Pricelist().jbp)
        jflt.insert(0, Pricelist().jflt)
        jblt.insert(0, Pricelist().jblt)
        mcpk.insert(0, Pricelist().mcpk)
        mbp.insert(0, Pricelist().mbp)
        mflt.insert(0, Pricelist().mflt)
        mblt.insert(0, Pricelist().mblt)
        lcpk.insert(0, Pricelist().lcpk)
        lbp.insert(0, Pricelist().lbp)
        lflt.insert(0, Pricelist().lflt)
        lblt.insert(0, Pricelist().lblt)

        submit_button = tk.Button(self.pricewindow, text="Update", bg="white", fg="black", width=25, bd=3,
                                  command=self.updating)
        submit_button.place(x=350, y=400)

    def updating(self):
        x = [self.JBaseprice.get(), self.JCostperkm.get(), self.JluxF.get(), self.JluxB.get(),
             self.MBaseprice.get(), self.MCostperkm.get(), self.MluxF.get(), self.MluxB.get(),
             self.LBaseprice.get(), self.LCostperkm.get(), self.LluxF.get(), self.LluxB.get()]
        update_prices(x)
        messagebox.showinfo("Update Ticket Price", "Succesfully Updated")
        self.pricewindow.destroy()