from tkinter import *
import math
import string
import random
import re
import decisionTree


####################################
# playGame mode, mousePressed, keyPressed
####################################

def playGameMousePressed(event, data):
    if data.currMessage == 1 and data.flash:
        #pressing on button
        if 500 <= event.x <= 507 and 150 <= event.y <= 215:
            data.correctAnswer = True
            data.score += 1
            data.flash = False
            data.pause = False
            data.messageIndex = 0
            data.currMessage += 1
        elif 250 <= event.x <= 300 and data.height-85 <= event.y <= data.height-35:
            data.correctAnswer = True
            data.score += 1
            data.flash = False
            data.pause = False
            data.messageIndex = 0
            data.currMessage += 1
        elif 43 <= event.x <= 50 and 160 <= event.y <= 210:
            data.correctAnswer = False
            data.badScore += 1
            data.pause = True
            data.messageIndex = 0
        elif 43 <= event.x <= 50 and 230 <= event.y <= 280:
            data.correctAnswer = False
            data.badScore += 1
            data.pause = True
            data.messageIndex = 0
    if data.currMessage == 2 and data.flash:
        if 250 <= event.x <= 300 and data.height-85 <= event.y <= data.height-35:
            data.correctAnswer = True
            data.score += 1
            data.flash = False
            # data.pause = True
            data.messageIndex = 0
            data.currMessage += 1
    #exiting game
    if data.width-200 <= event.x <= data.width-50 and data.height-75 <= event.y <= data.height-25:
        data.mode = "home"
        data.messageIndex = 0
        data.pause, data.pauseTime = False, 0
        data.currMessage = 0
        data.flash = False
        data.flashTime = 0
        data.correctAnswer = None
        data.answerQuestion = True
        data.score = 0
        data.badScore = 0
        data.newBadge = False
        data.badgeIndex = 0
        data.questionIndex = 0
        data.currQuestion = None
        data.currQValue = None
        data.currGroup = None
        data.tries = 0
        #saves user progress
        data.allUsers[data.currUser] = (data.allUsers[data.currUser][0], data.allPrompts, data.numBadges, data.promptTries, data.seenBadges, data.categoryTries)
        data.numQuestions = 0
        data.oneSwipe = False
        data.currBadge = None
        data.consecTries = 0
    
    #Swipe 1a
    if data.answerQuestion == True and data.currQuestion == "Go to the page on the right.":
        #start coordinates for swiping are on the right side of the iphone screen
        if 275 <= event.x <= 475 and 100 <= event.y <= data.height-100:
            data.swipeMousePressed = True
        elif 75 <= event.x <= 275 and 100 <= event.y <= data.height-100:
            data.swipeMousePressed = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else: data.swipeMousePressed = False


    #Swipe 1b
    if data.answerQuestion == True and data.currQuestion == "Go to the page to the left.":
        #start coordinates for swiping are on the right side of the iphone screen
        if 75 <= event.x <= 275 and 100 <= event.y <= data.height-100:
            data.swipeMousePressed = True
        elif 275 <= event.x <= 475 and 100 <= event.y <= data.height-100:
            data.swipeMousePressed = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else: data.swipeMousePressed = False
        
        
    #Swipe 2a
    if data.answerQuestion == True and data.currQuestion == "Go to the left most page with widgets (you are two pages away).":
        #start coordinates for swiping are on the left side of the iphone screen
        if 75 <= event.x <= 275 and 100 <= event.y <= data.height-100:
            data.swipeMousePressed = True
        elif 275 <= event.x <= 475 and 100 <= event.y <= data.height-100:
            data.swipeMousePressed = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else: data.swipeMousePressed = False
     
        
    #Swipe 2b
    if data.answerQuestion == True and data.currQuestion == "Swipe down in the middle of the screen to use search bar.":
        #start coordinates for swiping are on the top part of the iphone screen
        if 75 <= event.x <= 475 and 100 <= event.y <= 387:
            data.swipeMousePressed = True
        elif 75 <= event.x <= 475 and 387 <= event.y <= data.height-100:
            data.swipeMousePressed = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else: data.swipeMousePressed = False
        
        
    #Swipe 3a
    if data.answerQuestion == True and data.currQuestion == "Swipe down from the top to see notifications.":
        #start coordinates for swiping are on the top part of the iphone screen
        if 75 <= event.x <= 475 and 100 <= event.y <= 200:
            data.swipeMousePressed = True
        elif 75 <= event.x <= 475 and 200 <= event.y <= data.height-100:
            data.swipeMousePressed = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else: data.swipeMousePressed = False
    
    
    #Swipe 3b
    if data.answerQuestion == True and data.currQuestion == "Swipe up from bottom to see control center.":
        #start coordinates for swiping are on the top part of the iphone screen
        if 75 <= event.x <= 475 and data.height-200 <= event.y <= data.height-100:
            data.swipeMousePressed = True
        elif 75 <= event.x <= 475 and 100 <= event.y <= data.height-200:
            data.swipeMousePressed = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else: data.swipeMousePressed = False
    
    #Button 1a
    if data.currQuestion == "Put phone to sleep mode.":
        if 500 <= event.x <= 507 and 150 <= event.y <= 215:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
    
    #Button 1b
    if data.currQuestion == "Return to home screen.":
        if 250 <= event.x <= 300 and data.height-85 <= event.y <= data.height-35:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
    
    #Button 2a
    if data.currQuestion == "Turn down volume using buttons.":
        if 43 <= event.x <= 50 and 230 <= event.y <= 280:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
    
    #Button 2b
    if data.currQuestion == "Turn up volume using buttons.":
        if 43 <= event.x <= 50 and 160 <= event.y <= 210:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
    
    #Button 3a
    if data.answerQuestion == True and data.currQuestion == "Use home button to call siri.":
        #if home button is pressed
        if 250 <= event.x <= 300 and data.height-85 <= event.y <= data.height-35:
            data.hold = True
        #any other button is pressed
        elif (500 <= event.x <= 507 and 150 <= event.y <= 215) or (43 <= event.x <= 50 and 160 <= event.y <= 210) or (43 <= event.x <= 50 and 230 <= event.y <= 280):
            data.hold = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else:
            data.hold = False
    
    #Button 3b
    if data.answerQuestion == True and data.currQuestion == "Use button to shut down phone.":
        #if shut down button is pressed
        if 500 <= event.x <= 507 and 150 <= event.y <= 215:
            data.hold = True
        #any other button is pressed
        elif (250 <= event.x <= 300 and data.height-85 <= event.y <= data.height-35) or (43 <= event.x <= 50 and 160 <= event.y <= 210) or (43 <= event.x <= 50 and 230 <= event.y <= 280):
            data.hold = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else:
            data.hold = False
    
    #Control 1a
    if data.currQuestion == "Turn on/off do not disturb through control center.":
        if 190 <= event.x <= 265 and data.height-380 <= event.y <= data.height-305:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
    #Control 1b
    if data.currQuestion == "Turn on/off screen rotation through control center.":
        if 95 <= event.x <= 170 and data.height-380 <= event.y <= data.height-305:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            
    #Control 2a
    if data.answerQuestion == True and data.currQuestion == "Turn down brightness from control center.":
        #start coordinates for swiping are on the top part of the brightness block
        if 285 <= event.x <= 360 and data.height-385 <= event.y <= data.height-300:
            data.swipeMousePressed = True
        #anywhere else on phone screen except for top part of brightness button
        elif 75 <= event.x <= 475 and 100 <= event.y <= data.height-100 and not (285 <= event.x <= 360 and data.height-385 <= event.y <= data.height-300):
            data.swipeMousePressed = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else: data.swipeMousePressed = False
        
    #Control 2b
    if data.answerQuestion == True and data.currQuestion == "Turn down volume from control center.":
        #start coordinates for swiping are on the top part of the volume block
        if 380 <= event.x <= 455 and data.height-385 <= event.y <= data.height-300:
            data.swipeMousePressed = True
        #anywhere else on phone screen except for top part of volume button
        elif 75 <= event.x <= 475 and 100 <= event.y <= data.height-100 and not (380 <= event.x <= 455 and data.height-385 <= event.y <= data.height-300):
            data.swipeMousePressed = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else: data.swipeMousePressed = False
        
                
    #Control 3a
    if data.answerQuestion == True and data.currQuestion == "Go to network menu from control center.":
        #if network menu is pressed
        if 95 <= event.x <= 265 and data.height-570 <= event.y <= data.height-400:
            data.hold = True
        #anything other than network menu is pressed
        elif 75 <= event.x <= 475 and 100 <= event.y <= data.height-100 and not (95 <= event.x <= 265 and data.height-570 <= event.y <= data.height-400):
            data.hold = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else:
            data.hold = False
            

    #Control 3b
    if data.answerQuestion == True and data.currQuestion == "Go to music menu from control center.":
        #if music is pressed
        if 285 <= event.x <= 455 and data.height-570 <= event.y <= data.height-400:
            data.hold = True
        #anything other than music menu is pressed
        elif 75 <= event.x <= 475 and 100 <= event.y <= data.height-100 and not (285 <= event.x <= 455 and data.height-570 <= event.y <= data.height-400):
            data.hold = False
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
        else:
            data.hold = False


def playGameKeyPressed(event, data):
    pass