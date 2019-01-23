from tkinter import *
import math
import string
import random
import re
import decisionTree
import loginMode
import registerMode
import homeMode
import playGameMouse
import playGameMouseR
import playGameTimer
import playGameRedraw


####################################
# init (citation: general animation format from 112 website)
####################################

def init(data):
    data.mode = "welcome"
    data.timerDelay = 100
    data.totalTime = 0
    
    #three beginning message prompts, used in playGame mode
    data.messagePrompt1 = "Hi, welcome to your new iPhone!"
    data.messagePrompt2 = "Turn on your iPhone. Choose one option."
    data.messagePrompt3 = "Press the home button to unlock your phone."
    data.messageIndex = 0
    data.pause, data.pauseTime = False, 0
    data.messages = [data.messagePrompt1, data.messagePrompt2, data.messagePrompt3]
    data.currMessage = 0
    data.flash = False
    data.flashTime = 0
    data.correctAnswer = None
    data.answerQuestion = True
    data.badScore = 0
    data.score = 0
    
    #register username & password
    data.rUserInput = False
    data.rPassInput = False
    data.rUser = None
    data.rPass = None
    data.rInvalid = False
    data.rNotAvail = False
    data.hidden = True
    data.currUser = None
    
    #records users (five users already programmed so ML can be easily displayed)
    data.allUsers = {"username1": (None, None, None, None, None, {"Swipe":3, "Button":1, "Control":3}), "username2": (None, None, None, None, None,{"Swipe":0, "Button":2, "Control":20}), "username3": (None, None, None, None, None,{"Swipe":1, "Button":1, "Control":1}), "username4": (None, None, None, None,None, {"Swipe":4, "Button":3, "Control":1})}
    
    #login
    data.lUserInput = False
    data.lPassInput = False
    data.lUser = None
    data.lPass = None
    data.lInvalid = False


    #quiz part of playGame mode
    data.allPrompts = {"Go to the page on the right.": (1, False, "Swipe"), "Go to the page to the left.": (1, False, "Swipe"),"Go to the left most page with widgets (you are two pages away).": (2, False, "Swipe"), "Swipe down in the middle of the screen to use search bar.": (2, False, "Swipe"),"Swipe down from the top to see notifications.": (3, False, "Swipe"),"Swipe up from bottom to see control center.": (3, False, "Swipe"),"Put phone to sleep mode.": (1, False, "Button"), "Return to home screen.": (1, False, "Button"),"Turn down volume using buttons.": (2, False, "Button"), "Turn up volume using buttons.": (2, False, "Button"),"Use home button to call siri.": (3, False, "Button"),"Use button to shut down phone.": (3, False, "Button"),"Turn on/off do not disturb through control center.": (1, False, "Control"), "Turn on/off screen rotation through control center.": (1, False, "Control"),"Turn down brightness from control center.": (2, False, "Control"), "Turn down volume from control center.": (2, False, "Control"),"Go to network menu from control center.": (3, False, "Control"),"Go to music menu from control center.": (3, False, "Control")}
    data.controlQuestions = {"Turn on/off do not disturb through control center.", "Turn on/off screen rotation through control center.","Turn down brightness from control center.", "Turn down volume from control center.","Go to network menu from control center.","Go to music menu from control center."}
    data.questionIndex = 0
    data.currQuestion = None
    data.currQValue = None
    data.currGroup = None
    data.tries = 0
    data.numQuestions = 0
    data.swipeMousePressed = False
    data.oneSwipe = False
    data.hold = False
    data.holdTime = 0
    
    
    #awarding badges
    data.seenBadges = set()
    data.newBadge = False
    data.badgeIndex = 0
    data.badges = ["You've won the beginner's badge!", "Badge: You've made no mistakes in this category!", "Badge: You've answered five consecutive questions correctly!"]
    data.numBadges = 0
    data.currBadge = None
    data.consecTries = 0
    data.promptTries = dict() #records last seen tries for each level in category
    data.categoryTries = {"Swipe": 0, "Button": 0, "Control": 0} #records total tries for each category
    
    #badge images
    data.badge1 = PhotoImage(file="badge1.gif")
    data.badge2 = PhotoImage(file="badge2.gif")
    data.badge3 = PhotoImage(file="badge3.gif")
    
    
    #resulting actions from swipe category questions
    data.displayAction = False
    data.sx = 0
    data.sy = 0
    

####################################
# mode dispatcher (citation: 112 Course Website for mode dispatcher format)
####################################

def mousePressed(event, data):
    if (data.mode == "welcome"):      welcomeMousePressed(event, data)
    elif (data.mode == "login"):      loginMode.loginMousePressed(event, data)
    elif (data.mode == "register"):   registerMode.registerMousePressed(event, data)
    elif (data.mode == "home"):       homeMode.homeMousePressed(event, data)
    elif (data.mode == "playGame"):   playGameMouse.playGameMousePressed(event, data)
    elif (data.mode == "badges"):     badgesMousePressed(event, data)
    elif (data.mode == "progress"):   progressMousePressed(event, data)
    
def mouseReleased(event, data):
    if (data.mode == "playGame"):      playGameMouseR.playGameMouseReleased(event, data)
    

def keyPressed(event, data):
    if (data.mode == "welcome"):      welcomeKeyPressed(event, data)
    elif (data.mode == "login"):      loginMode.loginKeyPressed(event, data)
    elif (data.mode == "register"):   registerMode.registerKeyPressed(event, data)
    elif (data.mode == "home"):       homeMode.homeKeyPressed(event, data)
    elif (data.mode == "playGame"):   playGameMouse.playGameKeyPressed(event, data)
    elif (data.mode == "progress"):   progressKeyPressed(event, data)
    elif (data.mode == "badges"):     badgesKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "welcome"):      welcomeTimerFired(data)
    elif (data.mode == "login"):      loginMode.loginTimerFired(data)
    elif (data.mode == "register"):   registerMode.registerTimerFired(data)
    elif (data.mode == "home"):       homeMode.homeTimerFired(data)
    elif (data.mode == "playGame"):   playGameTimer.playGameTimerFired(data)
    elif (data.mode == "progress"):   progressTimerFired(data)
    elif (data.mode == "badges"):     badgesTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "welcome"):      welcomeRedrawAll(canvas, data)
    elif (data.mode == "login"):      loginMode.loginRedrawAll(canvas, data)
    elif (data.mode == "register"):   registerMode.registerRedrawAll(canvas, data)
    elif (data.mode == "home"):       homeMode.homeRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedraw.playGameRedrawAll(canvas, data)
    elif (data.mode == "progress"):   progressRedrawAll(canvas, data)
    elif (data.mode == "badges"):     badgesRedrawAll(canvas, data)

####################################
# welcome mode
####################################

def welcomeMousePressed(event, data):
    if data.width/4-100 <= event.x <= data.width/4+200 and \
    data.height/2 <= event.y <= data.height/2+100:
        data.mode = "login"
    elif 3*data.width/4-200 <= event.x <= 3*data.width/4+100 and \
    data.height/2 <= event.y <= data.height/2+100:
        data.mode = "register"

def welcomeKeyPressed(event, data):
    pass
    
def welcomeTimerFired(data):
    pass

def welcomeRedrawAll(canvas, data):
    #background color
    canvas.create_rectangle(0,0, data.width, data.height, fill = "old lace")
    #login, register rectangles
    canvas.create_rectangle(data.width/4-100, data.height/2, data.width/4+200, data.height/2+100, fill = "coral", outline = "orange")
    canvas.create_rectangle(3*data.width/4-200, data.height/2, 3*data.width/4+100, data.height/2+100, fill = "orange", outline = "orange")
    #welcome, login, register text
    canvas.create_text(data.width/2, data.height/4, text = "Welcome!", font = "Courier 150", fill = "firebrick1")
    canvas.create_text(data.width/4+50, data.height/2+50, text = "Login", font = "Courier 50", fill = "brown4")
    canvas.create_text(3*data.width/4-50, data.height/2+50, text = "Register", font = "Courier 50", fill = "brown4")


####################################
# progress mode
####################################

def progressMousePressed(event, data):
    if 0 <= event.x <= 175 and 0 <= event.y <= 75:
        data.mode = "home"

def progressKeyPressed(event, data):
    pass

def progressTimerFired(data):
    pass

def progressRedrawAll(canvas, data):
    #background color
    canvas.create_rectangle(0,0, data.width, data.height, fill = "old lace", outline = "old lace")
    
    #main menu block
    #curved outine of rectangle from https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners. This code is used throughout the project, but this is the first instance in this main file.
    x1,y1,x2,y2,r = 0,0, 175, 75, 10
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = "coral", smooth=True, outline = "coral", width = 3)
    canvas.create_text(175/2, 75/2, text = "Main Menu", fill = "white", font = "Courier 30")
    
    #progress table
    for row in range(4):
        for col in range(4):
            #drawing rectangle
            if (row == 0 or col == 0) and not(row == 0 and col == 0):
                thickness = 10
            else:
                thickness = 4
            canvas.create_rectangle(data.width/2-500+250*col, data.height/2-300+150*row, data.width/2-250+250*col, data.height/2-150+150*row, width = thickness)
            #category labels
            categories = ["Swipe", "Button", "Control"]
            category = categories[col-1]
            if row == 0 and col != 0:
                canvas.create_text(data.width/2-375+250*col, data.height/2-225+150*row, text = str(category), font = "Courier 50", fill = "IndianRed1")
            #level labels
            elif col == 0 and row != 0:
                levels = ["Level 1", "Level 2", "Level 3"]
                level = levels[row-1]
                canvas.create_text(data.width/2-375+250*col, data.height/2-225+150*row, text = str(level), font = "Courier 50", fill = "IndianRed1")
            elif row != 0 and col != 0:
                level = row
                #calls unseen function written above, checks if level of category has been reached
                if not playGameTimer.unseen(data, level, category):
                    canvas.create_text(data.width/2-375+250*col, data.height/2-225+150*row, text = "Seen", font = "Courier 50", fill = "IndianRed1")
            



####################################
# badges mode
####################################

def badgesMousePressed(event, data):
    if 0 <= event.x <= 175 and 0 <= event.y <= 75:
        data.mode = "home"

def badgesKeyPressed(event, data):
    pass
    
def badgesTimerFired(data):
    pass

def badgesRedrawAll(canvas, data):
    #background color
    canvas.create_rectangle(0,0, data.width, data.height, fill = "old lace", outline = "old lace")
    
    #main menu block
    x1,y1,x2,y2,r = 0,0, 175, 75, 10
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = "coral", smooth=True, outline = "coral", width = 3)
    canvas.create_text(175/2, 75/2, text = "Main Menu", fill = "white", font = "Courier 30")
    
    #three badges
    canvas.create_oval(data.width/2-200, data.height/2-200, data.width/2+200, data.height/2+200, outline = "coral", fill = "coral")
    canvas.create_oval(data.width/2-700, data.height/2-200, data.width/2-300, data.height/2+200, outline = "coral", fill = "coral")
    canvas.create_oval(data.width/2+300, data.height/2-200, data.width/2+700, data.height/2+200, outline = "coral", fill = "coral")
    
    #badge category
    canvas.create_text(data.width/2, data.height/2+300, text = "Consecutive Correct Answers", font = "Courier 30", fill = "coral")
    canvas.create_text(data.width/2-500, data.height/2+300, text = "Beginner's Badge", font = "Courier 30", fill = "coral")
    canvas.create_text(data.width/2+500, data.height/2+300, text = "Mastered a Category", font = "Courier 30", fill = "coral")
    
    #badge checkmarks
    if "You've won the beginner's badge!" in data.seenBadges:
        canvas.create_image(data.width/2-500, data.height/2, image = data.badge1)


    if "Badge: You've answered five consecutive questions correctly!" in data.seenBadges:
        canvas.create_image(data.width/2, data.height/2, image = data.badge2)

    
    if "Badge: You've made no mistakes in this category!" in data.seenBadges:
        canvas.create_image(data.width/2+500, data.height/2, image = data.badge3)




####################################
# use the run function as-is
#run function from 15-112 Course Website
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)
    
    def mouseReleasedWrapper(event, canvas, data):
        mouseReleased(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
        
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<ButtonRelease>", lambda event:
                            mouseReleasedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)

    # and launch the app
    root.mainloop()  # blocks until window is closed

run(1450, 775)