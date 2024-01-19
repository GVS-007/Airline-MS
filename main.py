#the_main.py for arbitrary uses.
import tkinter as tk
from Tkinter_frontend import LoginFrame
from testing import *


if __name__ == '__main__':
    root = tk.Tk()
    login_frame = LoginFrame(root)
    login_frame.mainloop()
    Test()



