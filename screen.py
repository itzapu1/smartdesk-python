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


def saved():
    screen10 = Toplevel(screen)
    screen10.title("Saved")
    screen10.geometry("100x100")
    Label(screen10, text="Saved").pack()

def save():
    height = raw_height.get()   #saving info that is being entered below
    timer = raw_timer.get()


    data = open(height, "w")
    data.write(height)
    data.write(timer)
    data.close()

    saved()

def update_preferences():
    global raw_height
    raw_height = StringVar()
    global raw_timer
    raw_timer = StringVar()  # carries height info that user entered

    screen9 = Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("300x250")
    Label(screen9, text = "Please enter your height" ).pack()
    Entry(screen9, textvariable = raw_height ).pack()
    Label(screen9, text = "Please enter your recommended timer reminder" ).pack()
    Entry(screen9, textvariable = raw_timer).pack()
    Button(screen9, text = "Save", command = save).pack()


def session():
    screen8 = Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Welcome to the dashboard").pack()
    Button(screen8, text = "Update Preferences", command = update_preferences).pack()



def login_success():
    session()
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Success").pack()
    Button(screen3, text = "OK", command = delete2).pack()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text= "User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


root = Tk()

def register_user():
    print("working")
    username_info = username.get()
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    email_info = email.get()
    pin_info = pin.get()
    timer_info = timer.get()
    preferences_info = preferences.get()
    suggestions_info = suggestions.get()
    password_info = password.get()
    print(lastname.get())
#file-output.py

    file = open(username_info + ".txt", "w")
    file.write(username_info + "\n")
    file.write(firstname_info + "\n")
    file.write(lastname_info + "\n")
    file.write(email_info + "\n")
    file.write(pin_info + "\n")
    file.write(timer_info + "\n")
    file.write(preferences_info + "\n")
    file.write(suggestions_info + "\n")
    file.write(password_info)
    file.close()


    #firstname_info = 'first_name'
    #lastname_info = 'last_name'
    #email_info = 'email'
    #pin_info = 'pin_number'
    #timer_info = 'mmt'
    #preferences_info = 'preferences'
    #suggestions_info = 'suggestions' 

    #payload = { 'first_name': str(firstname_info), 'last_name': lastname_info, 'email': email_info, 'pin_number': pin_info, 'mmt': timer_info, 'preferences': preferences_info, 'suggestions': suggestions_info}
    #r = requests.post('http://localhost:3003/create', json=payload)
    #print(r.json)



    username_entry.delete(0, END)
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    email_entry.delete(0, END)
    pin_entry.delete(0, END)
    timer_entry.delete(0, END)
    preferences_entry.delete(0, END)
    suggestions_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Successful!", fg = "green", font = ("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()

    else:
        user_not_found()




def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen.geometry("300x250")

    global username
    global firstname
    global lastname
    global email
    global pin
    global timer
    global preferences
    global suggestions
    global password

    global username_entry
    global firstname_entry
    global lastname_entry
    global email_entry
    global pin_entry
    global timer_entry
    global preferences_entry
    global suggestions_entry
    global password_entry

    username = StringVar()
    firstname = StringVar()
    lastname = StringVar()
    email = StringVar()
    pin = StringVar()
    timer = StringVar()
    preferences = StringVar()
    suggestions = StringVar()
    password = StringVar()


    Label(screen1, text="Please enter details below ").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()


    Label(screen1, text="First Name * ").pack()
    firstname_entry = Entry(screen1, textvariable=firstname)
    firstname_entry.pack()

    Label(screen1, text="Last Name * ").pack()
    lastname_entry = Entry(screen1, textvariable=lastname)
    lastname_entry.pack()

    Label(screen1, text="Email Address * ").pack()
    email_entry = Entry(screen1, textvariable=email)
    email_entry.pack()

    Label(screen1, text="Pin * ").pack()
    pin_entry = Entry(screen1, textvariable=pin)
    pin_entry.pack()

    Label(screen1, text="Timer * ").pack()
    timer_entry = Entry(screen1, textvariable=timer)
    timer_entry.pack()

    Label(screen1, text="Preferences * ").pack()
    preferences_entry = Entry(screen1, textvariable=preferences)
    preferences_entry.pack()

    Label(screen1, text="Suggestions  ").pack()
    suggestions_entry = Entry(screen1, textvariable=suggestions)
    suggestions_entry.pack()

    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()

    Label(screen1, text="").pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

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
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1



    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()



def main_screen() :
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Smart Desk")
    Label(text="Smart Desk", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command = register).pack()

    screen.mainloop()
main_screen()