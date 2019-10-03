from tkinter import *
import os
import requests
import time
#from pyfingerprint.pyfingerprint import PyFingerprint
#import RPi.GPIO as GPIO

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("350x350")

    global username
    global pin
    global email
    global heightft
    global heightinch

    global username_entry
    global pin_entry
    global email_entry
    global heightft_entry
    global heightinch_entry

    username = StringVar()
    pin = StringVar()
    email = StringVar()
    heightft = IntVar()
    heightinch = IntVar()


    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()

    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    pin_lable = Label(register_screen, text="Pin Number of 6 digits ")
    pin_lable.pack()
    pin_entry = Entry(register_screen, textvariable=pin, show='*')
    pin_entry.pack()

    email_lable = Label(register_screen, text="email * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    heightft_lable = Label(register_screen, text="Height in Feet * ")
    heightft_lable.pack()
    heightft_entry = Entry(register_screen, textvariable=heightft)
    heightft_entry.pack()

    heightinch_lable = Label(register_screen, text="Height in Inches ")
    heightinch_lable.pack()
    heightinch_entry = Entry(register_screen, textvariable=heightinch)
    heightinch_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("350x350")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Pin Number * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
    Button(login_screen, text="onward", width=10, height=1, command=fingerprint).pack()

#fingerprint screen reachable from either login or register screen
def fingerprint():
    global fingerprint_screen
    fingerprint_screen = Toplevel(main_screen)
    fingerprint_screen.title("Login")
    fingerprint_screen.geometry("350x350")
    Label(fingerprint_screen, text="Please scan your favorite finger").pack()
    Label(fingerprint_screen, text="").pack()

    global username_verify
   
    username_verify = StringVar()

    global username_login_entry

    Label(fingerprint_screen, text="Username * ").pack()
    username_login_entry = Entry(fingerprint_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(fingerprint_screen, text="").pack()
  
    Button(fingerprint_screen, text="Register Fingerprint", width=10, height=1, command=register_fingerprint).pack()

"""# enroll user with fingerprint function
def register_fingerprint():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to enroll new finger
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Checks if finger is already enrolled
        result = f.searchTemplate()
        positionNumber = result[0]

        if ( positionNumber >= 0 ):
            print('Template already exists at position #' + str(positionNumber))
            exit(0)

        print('Remove finger...')
        time.sleep(2)

        print('Waiting for same finger again...')

        ## Wait that finger is read again
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 2
        f.convertImage(0x02)

        ## Compares the charbuffers
        if ( f.compareCharacteristics() == 0 ):
            raise Exception('Fingers do not match')

        ## Creates a template
        f.createTemplate()

        ## Saves template at new position number
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

# Implementing event on register button

def fingerprint_login():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to search the finger and calculate hash
    try:
        print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            print('No match found!')
            exit(0)
        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))

        ## OPTIONAL stuff
        ##

        ## Loads the found template to charbuffer 1
        f.loadTemplate(positionNumber, 0x01)

        ## Downloads the characteristics of template loaded in charbuffer 1
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

        ## Hashes characteristics of template
        print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)"""


def register_user():
    username_info = username.get()
    pin_info = pin.get()
    email_info = email.get()
    heightft_info = heightft.get()
    heightinch_info = heightinch.get()

    #file = open(username_info, "w")
    #file.write(username_info + "\n")
    #file.write(pin_info + "\n")
    #file.write(email_info)

    print(heightinch_info)
    print(type(heightft_info))
    print(type(heightinch_info))

    #file.close()

    #payload = { 'username': str(username_info), 'pin_number': str(pin_info), 'email': str(email_info), 'user_height': int(heightft_info + heightinch_info) }
    #r = requests.post('http://localhost:3003/create', json=payload)
    #print(r.json)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    Button(register_screen, text="Complete Registration", height="2", width="30", command=next).pack()

def sit():
    global sit_option
    sit_option = Toplevel(main_screen)
    sit_option.title("Register")
    sit_option.geometry("350x350")


def next():
    global Suggestions_screen
    Suggestions_screen = Toplevel(main_screen)
    Suggestions_screen.title("Suggestions")
    Suggestions_screen.geometry("350x350")
    Label(Suggestions_screen, text="Here are our suggestions").pack()
    Label(Suggestions_screen, text="").pack()

    #Label(Suggestions_screen, text="Here is where Andres' stuff goes").pack()
    #Label(Suggestions_screen, text="").pack()

    def sitting():
        print("Desk is adjusting to sitting position")

    def standing():
        print("Desk is adjusting to standing position")

    def manual():
        print("Please position to manual position")


    # height calculation
    heightft_info = int(heightft.get())
    heightinch_info = int(heightinch.get())
    print(str(heightft_info))
    X = int(heightft_info) * 12
    height_total = int(X) + int(heightinch_info)
    standing_height = int((height_total / 2) + 8)
    sitting_height = int((height_total / 4) + 9)


    print("You have selected to stand" + str(standing_height))
    print("You have selected to sit" + str(sitting_height))

    #email_entry.delete(0, END)
    #username_entry.delete(0, END)
    #pin_entry.delete(0, END)
    #heightft_entry.delete(0, END)
    #heightinch_entry.delete(0, END)

    #Label(Suggestions_screen, text="Here is where Andres stuff goes").pack()

    Label(Suggestions_screen, text="Your height in inches: ").pack()
    Label(Suggestions_screen, text=height_total).pack()

    Label(Suggestions_screen, text="Recommended height for standing height: ").pack()
    Label(Suggestions_screen, text=standing_height).pack()

    Label(Suggestions_screen, text="Recommended height for sitting height: ").pack()
    Label(Suggestions_screen, text=sitting_height).pack()
    Label(Suggestions_screen, text="").pack()

    Button(Suggestions_screen, text="Sit", fg="red", width=7, height=1,command = lambda: sitting()).place(relx=0.65, rely=0.83, anchor=S)
    Button(Suggestions_screen, text="Stand", fg="red", width=7, height=1, command= lambda: standing()).place(relx=0.35, rely=.83, anchor=S)

#Inserting Michaels Code

    def next_2():
        global Timer_screen
        global timer
        global timer_entry
        timer = IntVar()
        timerinfo = timer.get()
    
        Timer_screen = Toplevel(main_screen)
        Timer_screen.title("Timer Option")
        Timer_screen.geometry("350x350")

        Label(Timer_screen, text="Please choose a preferred timer option").pack()
        Label(Timer_screen, text="").pack()

        timer_label = Label(Timer_screen, text="Set repeated timer _label ")
        timer_label.pack()
        timer_entry = Entry(Timer_screen, textvariable=timer)
        timer_entry.pack()

        print(int(timerinfo))

        Button(Timer_screen, text="Complete Registration", height="2", width="18", command=next_4).pack()

        Button(Timer_screen, text="Manual", width=6, height=1, command=lambda: manual()).place(relx=0.85, rely=.980, anchor=S)





    Button(Suggestions_screen, text="Complete Registration", height="2", width="18", command=next_2).pack()
    Button(Suggestions_screen, text="Manual", width=6, height=1, command=lambda: manual()).place(relx=0.85, rely=.980, anchor=S)



def next_4():
    payload = { 'username': str(username.get()), 'pin_number': str(pin.get()), 'email': str(email.get()), 'user_height': int(heightft.get() + heightinch.get()), 'mmt': str(timer.get()) }
    r = requests.post('http://localhost:3003/create', json=payload)
    print(r.json)

    email_entry.delete(0, END)
    username_entry.delete(0, END)
    pin_entry.delete(0, END)
    heightft_entry.delete(0, END)
    heightinch_entry.delete(0, END)
    timer_entry.delete(0,END)

    Button(Suggestions_screen, text="Manual", width=6, height=1, command=lambda: manual()).place(relx=0.85, rely=.980, anchor=S)





def next_3():
    minutes = int(timer.get())
    seconds = minutes*60

    for i in range(seconds):
        print(str(seconds - i) + " seconds remain")
        time.sleep(1)

    print("Time's up")

    timer_entry.delete(0, END)



# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    print(password1)

    payload1 = { 'username': str(username1), 'pin_number': str(password1) }
    r = requests.post('http://localhost:3003/login', json=payload1)
    print(r.json)

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Invalid Login")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Invalid Login")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x350")
    main_screen.title("Smart Desk")
    Label(text="The Vault Login", bg="grey", width="50", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()