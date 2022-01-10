from tkinter import *
import json
import sqlite3
import os

try:
    con = sqlite3.connect("database/data.db")
    c = con.cursor()
    print("Connection Sucsses Fully")
except(Exception):
    print("Connection Failed")

try:
    data = open(file="json/api.json")
    js = json.load(data)
except(Exception) as e:
    print("File Not Connect")

Background = js["BackGround"]
Fontcolor = js["FontColor"]
Title = js["Title"]
Font = js["Font"]

class code(Tk):
    def Login(self):
        try:
            Uname = Username.get()
            Passwd = password.get()
            Email = "None User Email"
            try:
                c.execute(f"""INSERT INTO UserData VALUES (
                    '{Uname}',
                    '{Passwd}',
                    '{Email}'
                )""")
                con.commit()
                con.close()
            except(Exception) as e:
                pass

        except(Exception) as e:
            pass

        Ap.destroy()

    def App(self):
        Label(text="Login To Code", font=("certificate", 25),
              bg=Background, fg=Fontcolor).place(x=40, y=35)

        Label(text="UserName", font=(Font, 15),
              bg=Background, fg=Fontcolor).place(x=20, y=100)

        global Username
        Username = Entry(bg='black', fg='lime', font=(
            'hack', 13), borderwidth=0, insertbackground='lime')
        Username.place(x=40, y=135)

        Label(text="Password", font=(Font, 15),
              bg=Background, fg=Fontcolor).place(x=20, y=170)

        global password
        password = Entry(bg='black', fg='lime', font=(
            'hack', 13), borderwidth=0, insertbackground='lime')
        password.place(x=40, y=205)

        Button(text="Join Now", font=(Font, 15),
               bg=Background, fg=Fontcolor, activebackground='lime', activeforeground='red', command=Ap.Login, borderwidth=0).place(x=80, y=300)

        mainloop()


Ap = code()
Ap.title(Title)
Ap.geometry("285x500")
Ap.configure(bg=Background)
Ap.resizable(False, False)
Ap.App()
os.system("clear")
