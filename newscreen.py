from tkinter import *
import tkinter as tk
import os
import requests
import time
from threading import Thread
#from requests.auth import HTTPBasicAuth
#from getpass import getpass
#import RPi.GPIO as GPIO
#from pyfingerprint import PyFingerprint
import hashlib

# Designing window for registration


class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        currentHeight = 0
        self.items[-1] = int(currentHeight)

    def get_stack(self):
        return self.items



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


    Label(register_screen, text="Please enter details below", bg="white").pack()
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

    #register_screen.attributes('-fullscreen', True)
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()


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
  
    Button(fingerprint_screen, text="Login", width=10, height=1, command=login_fingerprint).pack()

# enroll user with fingerprint function
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

        f.loadTemplate(positionNumber, 0x01)
        char_store = str(f.downloadCharacteristics(0x01))

        f.loadTemplate(positionNumber, 0x01)

        characteristics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

        global fingerprint
        fingerprint = hashlib.sha256(characteristics).hexdigest()

        print("hash form of your fingerprint " + fingerprint)

        return positionNumber, fingerprint


        GPIO.cleanup()

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)

# Implementing event on register button

def login_fingerprint():
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
        fplogin = hashlib.sha256(characterics).hexdigest()
        print('SHA-2 hash of template: ' + fplogin)

        global user_data
        try:    
            payload3 = {'fingerprint': str(fplogin)}
            r = requests.post('https://tranquil-wildwood-84911.herokuapp.com/login_fp', json=payload3)
            print(r.json)
            user_data = r.json()
            print(r.status_code)
            print(r.text)
            print(user_data['user_height'])
            login_sucess()
        except:
            user_not_found()





    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)


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


def next():
    global Suggestions_screen
    global height_total
    Suggestions_screen = Toplevel(main_screen)
    Suggestions_screen.title("Suggestions")
    Suggestions_screen.geometry("350x350")
    Label(Suggestions_screen, text="Here are our suggestions").pack()
    Label(Suggestions_screen, text="").pack()

    # height calculation
    heightft_info = int(heightft.get())
    heightinch_info = int(heightinch.get())
    print(str(heightft_info))
    X = int(heightft_info) * 12
    height_total = int(X) + int(heightinch_info)
    standing_height = int((height_total / 2) + 8)
    sitting_height = int((height_total / 4) + 9)

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

    Button(Suggestions_screen, text="Register Fingerprint", height="2", width="30", command=register_fingerprint).pack()


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



    Button(Suggestions_screen, text="Complete Registration", height="2", width="18", command=next_2).pack()


# registers user in DB via api call to heroku platform
def next_4():
    payload = { 'username': str(username.get()), 'pin_number': str(pin.get()), 'email': str(email.get()), 'user_height': int(height_total), 'mmt': str(timer.get()), 'fingerprint': str(fingerprint)}
    r = requests.post('https://tranquil-wildwood-84911.herokuapp.com/create', json=payload)
    print(height_total)
    print(fingerprint)
    print(r.json)

    email_entry.delete(0, END)
    username_entry.delete(0, END)
    pin_entry.delete(0, END)
    heightft_entry.delete(0, END)
    heightinch_entry.delete(0, END)
    timer_entry.delete(0,END)




def timer():
    minutes = user_data['timer'] 
    seconds = minutes*60

    Label(Loggin_screen, text="Please choose a preferred timer option").pack()

    clock = time.strftime("%H:%M:%S")

    for i in range(seconds):
        print(str(seconds - i) + " seconds remain")
        time.sleep(1)

        Label(Loggin_screen, text=currentTime).pack()


    print("Time's up! Please Stand")

    timer_entry.delete(0, END)



# Implementing event on login button

def login_verify():
    
    username1 = username_verify.get()
    password1 = password_verify.get()

    global user_data


    try:
        payload1 = { 'username': str(username1), 'pin_number': str(password1) }
        r = requests.post('https://tranquil-wildwood-84911.herokuapp.com/login', json=payload1)
        user_data = r.json()
        print(r.status_code)
        print(r.text)
        print(user_data['user_height'])
        login_sucess()
    except:
        user_not_found()
            
# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("200x100")
    Label(login_success_screen, text="Login Success for user " + username_verify.get()).pack()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
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
    global Loggin_screen
    global standing_height
    global sitting_height
    Loggin_screen = Toplevel(main_screen)
    Loggin_screen.title("Suggestions")
    Loggin_screen.geometry("350x350")
    Label(Loggin_screen, text="Here are our suggestions").pack()
    Label(Loggin_screen, text="").pack()
    #Loggin_screen.attributes('-fullscreen', True)

    s = Stack()
    s.push(0)


    t1 = Thread(target = timer, daemon = True)

    #GPIO.cleanup()

    #Label(Loggin_screen, text="Here is where Andres' stuff goes").pack()
    #Label(Loggin_screen, text="").pack()

    def sitting():
    #retrieves top most element in stack and equates it to be the current height
        currentHeight = s.pop()
        desk_moving = sitting_height *25.4/10
        print(desk_moving)
        coag_desk = desk_moving/6
        if currentHeight < coag_desk:
            moveToSitting = coag_desk - currentHeight
            print(moveToSitting)
            #needs to move up
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(18,GPIO.OUT)
            GPIO.setup(23,GPIO.OUT)
            GPIO.setup(24,GPIO.OUT)
            GPIO.setup(25,GPIO.OUT)

            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)

            time.sleep(moveToSitting)
            GPIO.cleanup()
            s.push(coag_desk)
            print(s.get_stack())
        elif currentHeight > coag_desk:
            moveToSitting = currentHeight - coag_desk
            print(moveToSitting)
            #move down
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(18,GPIO.OUT)
            GPIO.setup(23,GPIO.OUT)
            GPIO.setup(24,GPIO.OUT)
            GPIO.setup(25,GPIO.OUT)

            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.HIGH)

            time.sleep(moveToSitting)
            GPIO.cleanup()
            s.push(coag_desk)
            print(s.get_stack())

        elif currentHeight == coag_desk:
            s.push(currentHeight)
            print("desk is already at that height")

        

    def standing():
        #retrieves top most element in stack and equates it to be the current height
        currentHeight = s.pop()
        desk_moving = standing_height*25.4/10
        print(desk_moving)
        coag_desk = desk_moving/5        
        if currentHeight < coag_desk:
            moveToStanding = coag_desk - currentHeight
            print(moveToStanding)
            #move up
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(18,GPIO.OUT)
            GPIO.setup(23,GPIO.OUT)
            GPIO.setup(24,GPIO.OUT)
            GPIO.setup(25,GPIO.OUT)

            GPIO.output(18,GPIO.LOW)
            GPIO.output(23,GPIO.HIGH)
            GPIO.output(24,GPIO.HIGH)
            GPIO.output(25,GPIO.LOW)
            time.sleep(moveToStanding)
            GPIO.cleanup()
            s.push(coag_desk)
            print(s.get_stack())

        elif currentHeight > coag_desk:
            moveToStanding = currentHeight - coag_desk
            print(moveToStanding)
            #move down
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(18,GPIO.OUT)
            GPIO.setup(23,GPIO.OUT)
            GPIO.setup(24,GPIO.OUT)
            GPIO.setup(25,GPIO.OUT)

            GPIO.output(18,GPIO.HIGH)
            GPIO.output(23,GPIO.LOW)
            GPIO.output(24,GPIO.LOW)
            GPIO.output(25,GPIO.HIGH)
            time.sleep(moveToStanding)
            GPIO.cleanup()
            s.push(coag_desk)
            print(s.get_stack())
        elif currentHeight == coag_desk:
            s.push(currentHeight)
            print("desk is already at that height")

    def manual():
        #manual adjust function goes here
        print("Please position to manual position")

    def logout():
        #add logout button here
        currentHeight = s.pop()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        GPIO.setup(24,GPIO.OUT)
        GPIO.setup(25,GPIO.OUT)

        GPIO.output(18,GPIO.HIGH)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.LOW)
        GPIO.output(25,GPIO.HIGH)

        time.sleep(27)
        GPIO.cleanup()

        s.push(0)
        print(bottomOut)
        print(s.get_stack())
        main_screen.destroy()

    global hold_down

    def manual_up(event):
        hold_down = True
        while hold_down:
            print("raising desk... ")

    def manual_down(event):
        global running
        print("lowering desk... ")

    # height calculation
    height_total = int(user_data["user_height"])
    print(height_total)
    standing_height = int((height_total / 2) + 8)
    sitting_height = int((height_total / 4) + 9)


    print("You have selected to stand" + str(standing_height))
    print("You have selected to sit" + str(sitting_height))

    #email_entry.delete(0, END)
    #username_entry.delete(0, END)
    #pin_entry.delete(0, END)
    #heightft_entry.delete(0, END)
    #heightinch_entry.delete(0, END)

    #Label(Loggin_screen, text="Here is where Andres stuff goes").pack()
    
    Label(Loggin_screen, text="Your height in inches: ").pack()
    Label(Loggin_screen, text=height_total).pack()

    Label(Loggin_screen, text="Recommended height for standing height: ").pack()
    Label(Loggin_screen, text=standing_height).pack()

    Label(Loggin_screen, text="Recommended height for sitting height: ").pack()
    Label(Loggin_screen, text=sitting_height).pack()
    Label(Loggin_screen, text="").pack()

    Button(Loggin_screen, text="Sit", fg="red", width=12, height=4,command = lambda: sitting()).place(relx=0.65, rely=0.83, anchor=S)
    Button(Loggin_screen, text="Stand", fg="red", width=12, height=4, command= lambda: standing()).place(relx=0.35, rely=.83, anchor=S)
    Button(Loggin_screen, text="Manual", width=6, height=1, command=lambda: manual()).place(relx=0.85, rely=.980, anchor=S)
    Button(Loggin_screen, text="Logout", width=10, height=2, command=lambda: logout()).place(relx=0.15, rely=.980, anchor=S)
    Button(Loggin_screen, text="Run Timer", height="2", width="18", command=lambda:t1.start()).pack()

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