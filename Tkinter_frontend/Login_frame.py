# the file for tkinter --- GUI based.
#import os, os.path
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from Tkinter_frontend.Admin_frame import AdminFrame
from Tkinter_frontend.Passenger_frame import PassengerFrame

class LoginFrame(Frame):
    def __init__(self, master):
        master.title("Airline Management System")
        Frame.__init__(self, master)
        master.geometry("1200x630+200+50")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.original = Image.open('images/airport2.jpeg')
        self.image = ImageTk.PhotoImage(self.original)
        self.display = Canvas(self, bd=0, highlightthickness=0)
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
        self.display.grid(row=0, sticky=W+E+N+S)
        self.pack(fill=BOTH, expand=1)
        self.bind("<Configure>", self.resize)

        Pwindow = PassengerFrame(master)
        Awindow = AdminFrame(master)
        passenger_login_button = Button(self.display, text = "PASSENGER LOGIN",padx = 20, pady = 10,bg = "pink",font=('arial', 20, 'bold'),command = Pwindow.OpenPassengerWindow)
        pass_window = self.display.create_window(625,475,anchor='nw', window=passenger_login_button)

        admin_login_button = Button(self.display, text="ADMIN LOGIN", padx=20, pady=10, bg="pink",font=('arial', 20, 'bold'),command = Awindow.Openwindow)
        admin_login_button.place(x=625, y=375)

        exitbtn = Button(self.display, text='Exit', font=('arial', 20, 'bold'), height=1, width=10,bg='red', bd=4, command = self.amsexit)
        exitbtn_window = self.display.create_window(625,575,anchor='nw', window=exitbtn)

    #========================================Functions=============================================
    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
    def amsexit(self):
            exit = messagebox.askyesno("Airline Management System", "Confirm if you want to exit")
            if exit>0:
                self.master.destroy()

        
        

        
        










