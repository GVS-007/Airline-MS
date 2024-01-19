# AMS_SE_PROJECT
This project is done as part of the Software Engineering Course **CS29006** with contributions from the members of **Group-28**.\
This is a slightly scaled down model of an Airline Management System(so is **AMS**).\
The project with its code written in python uses *mysqllite3* for database storage and *tkinter* for the GUI.
## Breakup of the Files:
Tkinter_frontend has all the files related to frames and windows that are used for creating the GUI.\
source_backend has all the backend user classes and database modification and accesing codes.\
images has the images used as background in the GUI.\
admin.db and passenger.db are databases storing the details of Admins(Secondary Users) and Passengers(Primary Users) repectively.\
The main.py file is our application file and calls the Frontend and Backend recursively.
## Instructions to Run the Code:
Run the main.py file and the GUI for the appilcation starts.
## Instructions for using the AMS
First the LoginPortal appears,choose the role you want to login/signup with.\
If you want to Signup as Admin you need to use *"Airlines#123"* as the verification key.\
The signup and login are self explainatory
After Signup or Login a Home page appears showing a list of funtionalities unique to primary and secondary users.\
Choose from the functions to and new windows appear for each function.
