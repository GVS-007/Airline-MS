#Imports
from tkinter import *
from tkinter import Toplevel, messagebox
from source_backend.UserClass import *
from Tkinter_frontend.Admin_Home import AdminHome

class AdminFrame:
    def __init__(self,root):
        self.root_frame = root

    def Openwindow(self):
        #Creating a Toplevel window for admin to login
        self.adminWindow = Toplevel(self.root_frame, bg = "aquamarine")
        self.adminWindow.title("Admin Login")
        self.adminWindow.geometry("1200x630+200+50")
        self.adminWindow.resizable(0,0)

        #userid and password attributes for the admins
        self.userid = StringVar()
        self.passwrd = StringVar()

        #Label to show that this is a Admin login frame
        theLabel = Label(self.adminWindow, text="ADMIN LOGIN PAGE", bd=10,bg='green', padx=20, pady=10, width=70, font=('arial', 20, 'bold') )
        theLabel.pack()

        #Label for User ID
        userID_input_label = Label(self.adminWindow, text="USER ID", bg="white", fg="black", width=10)
        userID_input_label.place(x=400, y=200)

        #Entrybox to enter UserID
        userID_input = Entry(self.adminWindow, textvariable=self.userid, width=30, bd=2, insertborderwidth=2,bg="white", fg="black", selectbackground="light blue")
        userID_input.place(x=550, y=200)

        #Label for Password
        Password_input_label = Label(self.adminWindow, text="PASSWORD", bg="white", fg="black", width=10)
        Password_input_label.place(x=400, y=270)

        #Entrybox to enter Password
        Password_input = Entry(self.adminWindow, textvariable=self.passwrd, width=30, bd=2, insertborderwidth=2,bg="white", fg="black",selectbackground="light blue", show="*")
        Password_input.place(x=550, y=270)

        #Button for Login after entering the creditentials
        login_button = Button(self.adminWindow, text="LOGIN", bg="sky blue", fg="black", font=("arial", 20, "bold"),command=self.Login)
        login_button.place(x=580, y=350)

        #Button to signup into airline management system
        signup_button = Button(self.adminWindow, text="SIGN UP", font=("arial", 20, "bold"), fg="black",bg="sky blue", command=self.checkboxWindow)
        signup_button.place(x=400, y=350)


    def checkboxWindow(self):

        self.checkbox = Toplevel(self.root_frame, bg="grey")
        self.checkbox.title("ADMIN KEY CHECK")
        self.checkbox.geometry("400x400")

        self.key = StringVar()

        label_1 = Label(self.checkbox, text="ENTER ADMIN VERIFICATION KEY", borderwidth=2, bg="white", fg="black")
        label_1.place(x=50, y=100)

        key_input = Entry(self.checkbox, textvariable=self.key, width=30, bd=2, insertborderwidth=2,
                          bg="white", fg="black",
                          selectbackground="light blue", show="*")
        key_input.place(x=50, y=200)

        submit_key = Button(self.checkbox, text = "SUBMIT", bg = "white", fg = "black", width = 25, bd = 3,command = self.getkey)
        submit_key.place(x = 75, y = 250)




    def OpenSignupWindow(self):
                self.signupWindow = Toplevel(self.root_frame, bg="grey")
                self.adminWindow.destroy()
                self.signupWindow.title("SIGN UP PAGE")
                self.signupWindow.geometry('1000x800')
                self.signupWindow.resizable(0,0)

                self.label0 = Label(self.signupWindow, text = "ENTER ADMIN DETAILS", bg = "white",fg = "black", font=('arial', 20, 'bold'),height = 3,width = 40)
                self.label0.place(x = 300, y = 10)

                self.userID = StringVar()
                self.Name = StringVar()
                self.Password = StringVar()

                userID_input_label = Label(self.signupWindow,text = "USER ID",bg = "white",fg = "black",width = 10)
                userID_input_label.place(x = 100, y = 100)

                userID_input = Entry(self.signupWindow,textvariable = self.userID,width = 30,bd = 2,insertborderwidth = 2,bg = "white",fg = "black", selectbackground = "light blue")
                userID_input.place(x = 250, y = 100)

                Name_input_label = Label(self.signupWindow, text="NAME", bg="white", fg="black", width=10)
                Name_input_label.place(x=100, y=200)

                Name_input = Entry(self.signupWindow, textvariable = self.Name,width=30, bd=2, insertborderwidth=2, bg="white", fg="black",
                                     selectbackground="light blue")
                Name_input.place(x=250, y=200)

                Password_input_label = Label(self.signupWindow, text="PASSWORD", bg="white", fg="black", width=10)
                Password_input_label.place(x=100, y=300)

                Password_input = Entry(self.signupWindow, textvariable = self.Password,width=30, bd=2, insertborderwidth=2, bg="white", fg="black",
                                     selectbackground="light blue",show = "*")
                Password_input.place(x=250, y=300)

                submit_button = Button(self.signupWindow,text = "SUBMIT", bg = "white", fg = "black", width = 25, bd = 3,command = self.submit)
                submit_button.place(x = 400, y = 600)

    def submit(self):
        userID = self.userID.get()
        name = self.Name.get()
        password = self.Password.get()

        temp_admin = Admin(userID,name,password,"Airline#123")
        temp_admin.signup()

        self.userID.set("")
        self.Name.set("")
        self.Password.set("")

        self.signupWindow.destroy()
        self.adminWindow.destroy()
        AdminHome(self.root_frame, temp_admin)

    def Login(self):

        userID = self.userid.get()
        password = self.passwrd.get()

        if userID=="" or password=="":
            messagebox.showerror("Error", "All fields are required")
            return

        the_admin_object = getadmin(userID)
        if the_admin_object is None:
            messagebox.showerror('No record found', 'Incorrect UserID')
        elif the_admin_object.login(password):
            self.adminWindow.destroy()
            AdminHome(self.root_frame, the_admin_object)
        else:
            messagebox.showerror('Oops!', 'Incorrect UserID or Password!!. Try again')


    def getkey(self):
        thekey = self.key.get()

        if thekey == "Airline#123":
            self.OpenSignupWindow()
            self.checkbox.destroy()
        else:
            messagebox.showerror("ERROR","Incorrect key, try again")

