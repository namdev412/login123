
from ast import Pass, Str
from asyncio import subprocess
from faulthandler import disable
from pydoc import visiblename
from sys import stdout
from tabnanny import check
from tkinter import *
import tkinter as tk
#from sharepoint import SharePoint
from functools import partial
import os, sys
global btn
def migrate():
    uname = Username.get()
    pwd = Password.get()
    if uname=='' or pwd=='':
        message.set("Fill the details")
    else:
        if uname and pwd:
            cmd = subprocess.Popen(["PowerShell.exe", "-ExecutionPolicy", "Unrestricted", "-File", r"D:\Projects\MigrationPro\OSMails\\script.ps1"], stdout=sys.stdout)
            
            cmd.communicate()
            message.set("Migration success")

        else:
            message.set("Wrong username and password")

        '''
        if uname=="xyz@gmail.com" and pwd=="xyz123":
            message.set("Login Success")
        else:
            message.set("Wrong username and password")
        '''

def check_connection():
    username=Username.get()
    password=Password.get()
    if(radio_option.get()>0):
        sharepoint = SharePoint(username,password)
        try:
            result,msg = sharepoint.auth()
            if(result):
                print(result,msg)
                conn_result = "Connection Successfull"
                conn_result_label.config(fg="green", text=conn_result)
                btn.config(state=tk.ACTIVE)
                
            else:
                print(result,msg)
                conn_result = "Connection Failed"
                conn_result_label.config(fg="blue", text=conn_result)
        except Exception as e:
            print(result,msg)
            conn_result_label.config(fg="red")
            conn_result = "Connection Failed"
    else:
        message.set("Please select radio option")

#testing purpose can be removed
def selection():
    options = {1:"File Share", 2:"Share Point", 3:"GMB Mail"}
    print("option choosed",radio_option.get())


# global root
root = Tk()
root.title("Login Form")
root.geometry("800x500")

Username = StringVar()
Password = StringVar()
message = StringVar()
FileSharePath = StringVar()
SharePointURL = StringVar()
radio_option = IntVar()
conn_result = StringVar()
GMBMail = StringVar()
text = StringVar()
text1 = StringVar()
text.set('(ex: uname@xyzcom)')
text1.set('(ex:dest_uname@xyz.com')
conn_result = ""

Label(root, text="Group Email Box Migration Tool", width=55, font=("bold", 15), bg="blue", fg="white").place(x=60, y=53)
Label(root, text="Username", width=20, font=("bold", 10)).place(x=200, y=130)
Entry(root, textvariable=Username, width=30).place(x=330, y=130)
Label(root, text="Password:", width=20, font=("bold",10)).place(x=200, y=180)
Entry(root, textvariable=Password, show='*', width= 30).place(x=330, y=180)
Label(root,text="", textvariable=message, font=("bold", 10), fg="red").place(x=550, y=200)
Label(root, text="FileSharePath:", font=("bold", 10)).place(x=60, y=260)
Entry(root, textvariable=FileSharePath, width=75).place(x=215, y=260)
Label(root, text="SharePointURL:", font=("bold", 10)).place(x=60, y=290)
Entry(root, textvariable=SharePointURL, width=75).place(x=215, y=290)
btn=Button(root, text="Migrate", font=("bold", 10), width=15, height=1, bg="orange", command=migrate, state=tk.DISABLED)
btn.place(x=360, y=320)
Button(root, text="Check Connection", font=("bold", 10), width=15, height=1, bg="orange",command=check_connection).place(x=550, y=160)
conn_result_label= Label(root,text=conn_result, font=("bold", 10),padx=20,pady=5, fg="black")
conn_result_label.place(x=530, y=130)
Radiobutton(root, text="File Share", font=("bold", 10), padx=20, variable=radio_option,command=selection, value=1).place(x=35, y=130)
Radiobutton(root, text="Share Point", font=("bold", 10), padx=20, variable=radio_option,command=selection, value=2).place(x=35, y=160)
Label(root, text="Destination MailBox", font=("bold",10)).place(x=190, y=210)
Entry(root, textvariable=GMBMail, width=30).place(x=330, y=210)
Entry(root, textvariable=text, width=22, font=("bold",10), state=DISABLED).place(x=330, y=155)
Radiobutton(root, text="GMB Mail", font=("bold", 10),padx=20, variable=radio_option, command=selection, value=3).place(x=35, y=210)
root.mainloop()
