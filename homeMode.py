from tkinter import *
import math
import string
import random
import re
import decisionTree


####################################
# home mode
####################################

def homeMousePressed(event, data):
    if data.width/2-250 <= event.x <= data.width/2+250 and data.height/2-50 <= event.y <= data.height/2+250:
        data.mode = "playGame"
    if 0 <= event.x <= 175 and 0 <= event.y <= 75:
        data.mode = "welcome"
        data.rUser, data.rPass, data.lUser, data.lPass, data.currUser = None, None, None, None, None
        data.allPrompts = {"Go to the page on the right.": (1, False, "Swipe"), "Go to the page to the left.": (1, False, "Swipe"),"Go to the left most page with widgets (you are two pages away).": (2, False, "Swipe"), "Swipe down in the middle of the screen to use search bar.": (2, False, "Swipe"),"Swipe down from the top to see notifications.": (3, False, "Swipe"),"Swipe up from bottom to see control center.": (3, False, "Swipe"),"Put phone to sleep mode.": (1, False, "Button"), "Return to home screen.": (1, False, "Button"),"Turn down volume using buttons.": (2, False, "Button"), "Turn up volume using buttons.": (2, False, "Button"),"Use home button to call siri.": (3, False, "Button"),"Use button to shut down phone.": (3, False, "Button"),"Turn on/off do not disturb through control center.": (1, False, "Control"), "Turn on/off screen rotation through control center.": (1, False, "Control"),"Turn down brightness from control center.": (2, False, "Control"), "Turn down volume from control center.": (2, False, "Control"),"Go to network menu from control center.": (3, False, "Control"),"Go to music menu from control center.": (3, False, "Control")}
        data.score = 0
        data.totalTime = 0
        data.badScore = 0
        data.numBadges = 0
        data.rUserInput = False
        data.rPassInput = False
        data.rInvalid = False
        data.rNotAvail = False
        data.lUserInput = False
        data.lPassInput = False
        data.lInvalid = False
        data.numQuestions = 0
        data.seenBadges = set()
        data.promptTries = dict()
        data.categoryTries = {"Swipe":0, "Button":0, "Control":0}
    if data.width-175 <= event.x <= data.width and 0 <= event.y <= 75:
        data.mode = "progress"
    if 0 <= event.x <= 175 and data.height-75 <= event.y <= data.height:
        data.mode = "badges"

        

def homeKeyPressed(event, data):
    #cheat keys
    
    if event.keysym == "b":
        #all badges are seen
        data.seenBadges.add(data.badges[0])
        data.seenBadges.add(data.badges[1])
        data.seenBadges.add(data.badges[2])

    #all categories and levels are seen
    if event.keysym == "p":
        for prompt in data.allPrompts:
            data.allPrompts[prompt] = (data.allPrompts[prompt][0], True, data.allPrompts[prompt][2])
    
def homeTimerFired(data):
    pass


def homeRedrawAll(canvas, data):
    #background color
    canvas.create_rectangle(0,0, data.width, data.height, fill = "old lace", outline = "old lace")
    
    #logout block
    x1,y1,x2,y2,r = 0,0, 175, 75, 10
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = "coral", smooth=True, outline = "coral", width = 3)
    canvas.create_text(175/2, 75/2, text = "Logout", fill = "white", font = "Courier 30")
    
    #progress block
    x1,y1,x2,y2,r = data.width-175,0, data.width, 75, 10
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = "coral", smooth=True, outline = "coral", width = 3)
    canvas.create_text(data.width-175/2, 75/2, text = "Progress", fill = "white", font = "Courier 30")
    
    
    #badges block
    x1,y1,x2,y2,r = 0,data.height-75, 175, data.height, 10
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = "coral", smooth=True, outline = "coral", width = 3)
    canvas.create_text(175/2, data.height-75/2, text = "Badges", fill = "white", font = "Courier 30")


    #categories
    canvas.create_text(data.width/2, data.height/4, text = "Home", font = "Courier 150", fill = "firebrick1")
    
    #play game
    x1,y1,x2,y2,r = data.width/2-250,data.height/2-50, data.width/2+250, data.height/2+250, 7
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = "coral", smooth=True, outline = "coral", width = 3)
    canvas.create_text(data.width/2, data.height/2+100, text = "Play!", fill = "white", font = "Courier 70")
    
