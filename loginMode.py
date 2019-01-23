from tkinter import *
import math
import string
import random
import re
import decisionTree

####################################
# login mode
####################################

def loginMousePressed(event, data):
    if data.width/2-60 <= event.x <= data.width/2+60 and data.height/2+250 <= event.y <= data.height/2+300:
        data.lUserInput = False
        data.lPassInput = False
        if isValidCombo(data) == True:
            data.mode = "home"
            data.currUser = data.lUser
            data.allPrompts = data.allUsers[data.lUser][1]
            data.numBadges = data.allUsers[data.lUser][2]
            data.promptTries = data.allUsers[data.lUser][3]
            data.seenBadges = data.allUsers[data.lUser][4]
            data.categoryTries = data.allUsers[data.lUser][5]
        else:
            data.lUser = None
            data.lPass = None
            data.lInvalid = True
            #must reset user and password when logging out
    elif data.width/2-150 <= event.x <= data.width/2+150 and data.height/2-30 <= event.y <= data.height/2+50:
        data.lPassInput = False
        data.lUserInput = True
    elif data.width/2-150 <= event.x <= data.width/2+150 and data.height/2+120 <= event.y <= data.height/2+200:
        data.lUserInput = False
        data.lPassInput = True
    elif data.width/2-80 <= event.x <= data.width/2+80 and data.height/2+330 <= event.y <= data.height/2+360:
        data.lUser = None
        data.lPass = None
        data.mode = "register"
    elif data.width/2+170 <= event.x <= data.width/2+210 and data.height/2+140 <= event.y <= data.height/2+180:
        data.hidden = not(data.hidden)
    
def isValidCombo(data):
    if data.lUser in data.allUsers:
        return data.lPass == data.allUsers[data.lUser][0]
    return False

def loginKeyPressed(event, data):
    if data.lUserInput == True:
        if event.keysym in string.printable:
            if data.lUser == None:
                data.lUser = event.keysym
            else:
                data.lUser = data.lUser + event.keysym
        elif event.keysym == "BackSpace":
            if data.lUser != None:
                if len(data.lUser) == 1:
                    data.lUser = None
                else:
                    data.lUser = data.lUser[:-1]
    if data.lPassInput == True:
        if event.keysym in string.printable:
            if data.lPass == None:
                data.lPass = event.keysym
            else:
                data.lPass = data.lPass + event.keysym
        elif event.keysym == "BackSpace":
            if data.lPass != None:
                if len(data.lPass) == 1:
                    data.lPass = None
                else:
                    data.lPass = data.lPass[:-1]
    
    
def loginTimerFired(data):
    pass
    

    
    
def loginRedrawAll(canvas, data):
    #background color
    canvas.create_rectangle(0,0, data.width, data.height, fill = "old lace")
    #login, register, submit, register page rectangles
    canvas.create_rectangle(data.width/2-150, data.height/2-30, data.width/2+150, data.height/2+50, fill = "coral", outline = "orange")
    canvas.create_rectangle(data.width/2-150, data.height/2+120, data.width/2+150, data.height/2+200, fill = "orange", outline = "orange")
    canvas.create_rectangle(data.width/2-60, data.height/2+250, data.width/2+60, data.height/2+300, fill = "firebrick1", outline = "firebrick1")
    canvas.create_rectangle(data.width/2-80, data.height/2+330, data.width/2+80, data.height/2+360, fill = "firebrick1", outline = "firebrick1")
    #welcome, login, register, submit, register page text
    canvas.create_text(data.width/2, data.height/4, text = "Login!", font = "Courier 150", fill = "firebrick1")
    canvas.create_text(data.width/2-60, data.height/2-50, text = "Username:", font = "Courier 30", fill = "brown4")
    canvas.create_text(data.width/2-60, data.height/2+100, text = "Password:", font = "Courier 30", fill = "brown4")
    canvas.create_text(data.width/2, data.height/2+275, text = "Submit", font = "Courier 30", fill = "white")
    canvas.create_text(data.width/2, data.height/2+345, text = "Register", font = "Courier 20", fill = "white")
    #checkbox for hidden password
    canvas.create_rectangle(data.width/2+170, data.height/2+140, data.width/2+210, data.height/2+180, fill = "white", outline = "LightBlue1")
    canvas.create_text(data.width/2+300, data.height/2+160, text = "Hide Password", font = "Courier 20", fill = "SteelBlue1")
    if data.hidden:
        canvas.create_line(data.width/2+170-5, data.height/2+140-5, data.width/2+210+5, data.height/2+180+5, fill = "SkyBlue1")
        canvas.create_line(data.width/2+170-5, data.height/2+180+5, data.width/2+210+5, data.height/2+140-5, fill = "SkyBlue1")
    #userInput for username and password
    if data.lUser != None:
        canvas.create_text(data.width/2, data.height/2+10, text = str(data.lUser), font = "Courier 20")
    if data.lPass != None:
        if data.hidden:
            hidden = "*" * len(data.lPass)
            canvas.create_text(data.width/2, data.height/2+160, text = str(hidden), font = "Courier 20")
        else:
            canvas.create_text(data.width/2, data.height/2+160, text = str(data.lPass), font = "Courier 20")
    if data.lInvalid == True:
        canvas.create_text(data.width/2, data.height/2-80, text = "Username/Password not registered.", font = "Courier 20")