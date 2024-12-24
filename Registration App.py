# A Simple Registration Process...
import ttkbootstrap as ttk
from colored import style
from tkinter import messagebox
import csv
from ttkbootstrap.constants import *
##################################################################
def Mechanism():
    with open("DB.csv" , "a", newline="" , encoding = "utf-8") as db:
        DataBase = csv.writer(db)
        FirstName = FN_Entry.get()
        LastName = LN_Entry.get()
        Email = Email_Entry.get()
        if len(FirstName) == 0 or len(LastName) == 0 or len(Email) == 0:
            messagebox.showerror("Result" , "Some of the entries are empty!")
        else:
            Information = [FirstName , LastName , Email]
            DataBase.writerow(Information)
            messagebox.showinfo("Result" , "Operation is done successfully!")
    db.close()
    FN_Entry.delete(0 , ttk.END)
    LN_Entry.delete(0 , ttk.END)
    Email_Entry.delete(0 , ttk.END)     
####################################################
Registration = ttk.Window(themename = "cyborg")
Registration.geometry("700x500+500+250")
Registration.title("Submission Process")
Registration.resizable(False , False)
####################################################
Label1 = ttk.Label(text = "Your First Name" , font= ("Calibri" , 20 , "bold" , "italic" , "underline"))
Label1.grid(row = 0 , column = 0 , padx = 200 , pady = 10)
FN_Entry = ttk.Entry(Registration , width = 40 , style = "info.TEntry")
FN_Entry.grid(row = 1 , column = 0 , padx = 200 , pady = 5)
####################################################
Label2 = ttk.Label(text = "Your Last Name" , font =("Times New Roman" , 20 , "bold" , "italic" , "underline"))
Label2.grid(row = 2 , column = 0 , padx = 200 , pady = 10)
LN_Entry = ttk.Entry(Registration , width = 40 , style = "primary.TEntry")
LN_Entry.grid(row = 3 , column = 0 , padx = 200 , pady = 5)
####################################################
Label3 = ttk.Label(text = "Your Email Address" , font = ("Arial" , 17 , "bold" , "italic" , "underline"))
Label3.grid(row = 4 , column = 0 , padx = 200 , pady = 10)
Email_Entry = ttk.Entry(Registration , width = 40 , style = "warning.TEntry")
Email_Entry.grid(row = 5 , column = 0 , padx = 200 , pady = 5)
####################################################
####################################################
Submission = ttk.Button(Registration , width = 22 , text = "Submit" , style = "success.Link.TButton" , command = Mechanism)
Submission.grid(row = 8 , column = 0 , padx = 200 , pady = 10)
####################################################
Registration.mainloop()