from tkinter import *
import os
import requests

#making them pop out windows
def delete2(): #deletes screen 3's pop up
    screen3.destroy()

def delete3(): #deletes screen 4's pop up
    screen4.destroy()

def delete4(): #deletes screen 5's pop up
    screen5.destroy()

def logout():
    screen7.destroy()


def login_success():
    session()
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Success").pack()
    Button(screen3, text = "OK", command = delete2).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text= "User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


root = Tk()

def register():
    def sit():
        heightft_info = heightft.get()
        heightinch_info = heightinch.get()
        print(str(heightft_info))
        X=int(heightft_info)*12
        height_total=int(X) + int(heightinch_info)
        standing_height = int((height_total/2) + 8)
        sitting_height = int((height_total/4) + 9)
        print("You have selected to sit" + str(standing_height))

    def stand():
        print("You have selected to stand")

    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen.geometry("300x250")

    global username
    global email
    global pin
    global heightft
    global heightinch
    global username_entry
    global email_entry
    global pin_entry
    global heightft_entry
    global heightinch_entry
    username = StringVar()
    email = StringVar()
    pin = StringVar()
    timer = StringVar()
    heightft = IntVar()
    heightinch = IntVar()



    Label(screen1, text="Please enter details below ").pack()

    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()

    Label(screen1, text="Pin * ").pack()
    pin_entry = Entry(screen1, textvariable=pin)
    pin_entry.pack()


   #Label(screen1, text="Full Name * ").pack()
   #firstname_entry = Entry(screen1, textvariable=firstname)
   #firstname_entry.pack()

    Label(screen1, text="Email Address * ").pack()
    email_entry = Entry(screen1, textvariable=email)
    email_entry.pack()

    Label(screen1, text="Height (Feet) * ").pack()
    heightft_entry = Entry(screen1, textvariable=heightft)
    heightft_entry.pack()

    Label(screen1, text="Height (Inches) * ").pack()
    heightinch_entry = Entry(screen1, textvariable=heightinch)
    heightinch_entry.pack()

    Label(screen1, text="Preferable Option ").pack()

    Button(screen1, text = "Sit", fg="red",  width = 7, height = 1,command = sit).place(relx=0.75, rely=0.93, anchor=S)
    Button(screen1, text="Stand", fg="red", width=7, height=1,command = stand).place(relx=0.25, rely=.93, anchor=S)

    Label(screen1, text="").pack()
    Button(screen1, text = "Next", width = 15, height = 1, command = register_user).pack()


def register_user():
    print("working")

    username_info = username.get()
  #  fullname_info = fullname.get()
    email_info = email.get()
    pin_info = pin.get()
    #timer_info = timer.get()
    heightft_info = heightft.get()
    heightinch_info = heightinch.get()

    print(str(username.get()))


    username_entry.delete(0, END)
  #  fullname_entry.delete(0, END)
    email_entry.delete(0, END)
    pin_entry.delete(0, END)
    #timer_entry.delete(0, END)
    heightft_entry.delete(0,END)
    heightinch_entry.delete(0,END)


    Label(screen1, text = "Registration Successful!", fg = "green", font = ("calibri", 15)).pack()
    Label(text="").pack()
    Button(screen1, text="Next", height="2", width="30", command=next).pack()

def login_verify():
    username1 = username_verify.get()
    pin1 = pin_verify.get()
    username_entry1.delete(0,END)
    pin_entry1.delete(0,END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if pin1 in verify:
            login_success()
        else:
            pin_not_recognised()

    else:
        user_not_found()

def next():
    print("Here is your height information")
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("Suggestions")
    screen9.geometry("300x250")

    Label(screen9, text="Here is where Andres' stuff goes").pack()
    Label(screen9, text="").pack()

    #payload = { 'username': str(username_info), }
    #r = requests.post('http://localhost:3003/create', json=payload)
    #print(r.json)

def login():
    print("Login session started")
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()



#variable types
    global username_verify
    global pin_verify

    username_verify = StringVar()
    pin_verify = StringVar()

    global username_entry1
    global pin_entry1

    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Pin *").pack()
    pin_entry1 = Entry(screen2, textvariable = pin_verify)
    pin_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()



def main_screen() :
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Smart Desk")
    Label(text="The Vault Login", bg="grey", width="50", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command = register).pack()
    Label(text="").pack()


    screen.mainloop()
main_screen()