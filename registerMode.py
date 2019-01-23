from tkinter import *
import math
import string
import random
import re
import decisionTree

####################################
# register mode
####################################

def registerMousePressed(event, data):
    if data.width/2-60 <= event.x <= data.width/2+60 and data.height/2+250 <= event.y <= data.height/2+300:
        data.rUserInput = False
        data.rPassInput = False
        data.rInvalid = False
        data.rNotAvail = False
        if isValidUser(data) == True:
            data.allUsers[data.rUser] = data.rPass, data.allPrompts, data.numBadges, data.promptTries, data.seenBadges, data.categoryTries
            data.mode = "home"
            data.currUser = data.rUser
        else:
            data.rUser = None
            data.rPass = None
            #must reset user and password when logging out
    elif data.width/2-150 <= event.x <= data.width/2+150 and data.height/2-30 <= event.y <= data.height/2+50:
        data.rPassInput = False
        data.rUserInput = True
    elif data.width/2-150 <= event.x <= data.width/2+150 and data.height/2+120 <= event.y <= data.height/2+200:
        data.rUserInput = False
        data.rPassInput = True
    elif data.width/2-80 <= event.x <= data.width/2+80 and data.height/2+330 <= event.y <= data.height/2+360:
        data.rUser = None
        data.rPass = None
        data.mode = "login"
    elif data.width/2+170 <= event.x <= data.width/2+210 and data.height/2+140 <= event.y <= data.height/2+180:
        data.hidden = not(data.hidden)
        

        
def isValidUser(data):
    if len(data.rUser) < 6 or len(data.rUser) > 12:
        data.rInvalid = True
        return False
    for i in data.rUser:
        if i not in string.ascii_letters and i not in string.digits:
            data.rInvalid = True
            return False
    if data.rUser in data.allUsers:
        data.rNotAvail = True
        return False
    if len(data.rPass) < 6 or len(data.rPass) > 12:
        data.rInvalid = True
        return False
    for j in data.rPass:
        if j not in string.ascii_letters:
            data.rInvalid = True
            return False
    return True
    
  
def registerKeyPressed(event, data):
    if data.rUserInput == True:
        if event.keysym in string.printable:
            if data.rUser == None:
                data.rUser = event.keysym
            else:
                data.rUser = data.rUser + event.keysym
        elif event.keysym == "BackSpace":
            if data.rUser != None:
                if len(data.rUser) == 1:
                    data.rUser = None
                else:
                    data.rUser = data.rUser[:-1]
    if data.rPassInput == True:
        if event.keysym in string.printable:
            if data.rPass == None:
                data.rPass = event.keysym
            else:
                data.rPass = data.rPass + event.keysym
        elif event.keysym == "BackSpace":
            if data.rPass != None:
                if len(data.rPass) == 1:
                    data.rPass = None
                else:
                    data.rPass = data.rPass[:-1]
    
    
def registerTimerFired(data):
    pass
    
def registerRedrawAll(canvas, data):
    #background color
    canvas.create_rectangle(0,0, data.width, data.height, fill = "old lace")
    #username, password, submit rectangles
    canvas.create_rectangle(data.width/2-150, data.height/2-30, data.width/2+150, data.height/2+50, fill = "coral", outline = "orange")
    canvas.create_rectangle(data.width/2-150, data.height/2+120, data.width/2+150, data.height/2+200, fill = "orange", outline = "orange")
    canvas.create_rectangle(data.width/2-60, data.height/2+250, data.width/2+60, data.height/2+300, fill = "firebrick1", outline = "firebrick1")
    canvas.create_rectangle(data.width/2-80, data.height/2+330, data.width/2+80, data.height/2+360, fill = "firebrick1", outline = "firebrick1")
    #welcome, username, password, submit text
    canvas.create_text(data.width/2, data.height/4, text = "Register!", font = "Courier 150", fill = "firebrick1")
    canvas.create_text(data.width/2-60, data.height/2-50, text = "Username:", font = "Courier 30", fill = "brown4")
    canvas.create_text(data.width/2, data.height/2+70, text = "6-12 characters long, letters & numbers", font = "Courier 15", fill = "brown4")
    canvas.create_text(data.width/2-60, data.height/2+100, text = "Password:", font = "Courier 30", fill = "brown4")
    canvas.create_text(data.width/2, data.height/2+220, text = "6-12 characters long, only letters", font = "Courier 15", fill = "brown4")
    canvas.create_text(data.width/2, data.height/2+275, text = "Submit", font = "Courier 30", fill = "white")
    canvas.create_text(data.width/2, data.height/2+345, text = "Login", font = "Courier 20", fill = "white")
    #checkbox for hidden password
    canvas.create_rectangle(data.width/2+170, data.height/2+140, data.width/2+210, data.height/2+180, fill = "white", outline = "LightBlue1")
    canvas.create_text(data.width/2+300, data.height/2+160, text = "Hide Password", font = "Courier 20", fill = "SteelBlue1")
    if data.hidden:
        canvas.create_line(data.width/2+170-5, data.height/2+140-5, data.width/2+210+5, data.height/2+180+5, fill = "SkyBlue1")
        canvas.create_line(data.width/2+170-5, data.height/2+180+5, data.width/2+210+5, data.height/2+140-5, fill = "SkyBlue1")
    #userInput for username and password
    if data.rUser != None:
        canvas.create_text(data.width/2, data.height/2+10, text = str(data.rUser), font = "Courier 20")
    if data.rPass != None:
        if data.hidden:
            hidden = "*" * len(data.rPass)
            canvas.create_text(data.width/2, data.height/2+160, text = str(hidden), font = "Courier 20")
        else:
            canvas.create_text(data.width/2, data.height/2+160, text = str(data.rPass), font = "Courier 20")
    if data.rInvalid == True:
        canvas.create_text(data.width/2, data.height/2-80, text = "Username/Password must fit requirements.", font = "Courier 20")
    if data.rNotAvail == True:
        canvas.create_text(data.width/2, data.height/2-80, text = "Username taken.", font = "Courier 20")