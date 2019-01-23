from tkinter import *
import math
import string
import random
import re
import decisionTree


####################################
# playGame mode, mouseReleased
####################################

def playGameMouseReleased(event, data):
    #Swipe 1a
    if data.currQuestion == "Go to the page on the right." and data.swipeMousePressed == True:
        if 75 <= event.x <= 275 and 100 <= event.y <= data.height-100:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            data.swipeMousePressed = False
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
            data.displayAction = True
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.swipeMousePressed = False
    
    #Swipe 1b
    if data.currQuestion == "Go to the page to the left." and data.swipeMousePressed == True:
        if 275 <= event.x <= 475 and 100 <= event.y <= data.height-100:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            data.swipeMousePressed = False
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
            data.displayAction = True
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.swipeMousePressed = False

    #Swipe 2a
    if data.currQuestion == "Go to the left most page with widgets (you are two pages away)." and data.swipeMousePressed == True:
        if data.oneSwipe == True and 275 <= event.x <= 475 and 100 <= event.y <= data.height-100:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            data.swipeMousePressed = False
            data.oneSwipe = False
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
            data.displayAction = True
        elif 275 <= event.x <= 475 and 100 <= event.y <= data.height-100:
            data.oneSwipe = True
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.swipeMousePressed = False
            data.oneSwipe = False
    
    #Swipe 2b
    if data.currQuestion == "Swipe down in the middle of the screen to use search bar." and data.swipeMousePressed == True:
        if 75 <= event.x <= 475 and 387 <= event.y <= data.height-100:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            data.swipeMousePressed = False
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
            data.displayAction = True
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.swipeMousePressed = False
    
    #Swipe 3a
    if data.currQuestion == "Swipe down from the top to see notifications." and data.swipeMousePressed == True:
        if 75 <= event.x <= 475 and 200 <= event.y <= data.height-100:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            data.swipeMousePressed = False
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
            data.displayAction = True
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.swipeMousePressed = False
            
    #Swipe 3b
    if data.currQuestion == "Swipe up from bottom to see control center." and data.swipeMousePressed == True:
        if 75 <= event.x <= 475 and 100 <= event.y <= data.height-200:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            data.swipeMousePressed = False
            if data.tries == 0:
                data.consecTries += 1
            else:
                data.consecTries = 0
            data.promptTries[(data.currGroup, data.currQValue)] = data.tries
            data.categoryTries[data.currGroup] += data.tries
            data.displayAction = True
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.swipeMousePressed = False
    
    #Button 3a
    if data.currQuestion == "Use home button to call siri." and data.hold == True:
        if 250 <= event.x <= 300 and data.height-85 <= event.y <= data.height-35:
            if data.holdTime >= 10:
                data.correctAnswer = True
                data.pause = False
                data.questionIndex = 0
                data.hold = False
                data.holdTime = 0
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
                data.holdTime = 0
                data.hold = False
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.holdTime = 0
            data.hold = False
    
    #Button 3b
    if data.currQuestion == "Use button to shut down phone." and data.hold == True:
        if 500 <= event.x <= 507 and 150 <= event.y <= 215:
            if data.holdTime >= 10:
                data.correctAnswer = True
                data.pause = False
                data.questionIndex = 0
                data.hold = False
                data.holdTime = 0
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
                data.holdTime = 0
                data.hold = False
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.holdTime = 0
            data.hold = False
            
 
    #Control 2a
    if data.currQuestion == "Turn down brightness from control center." and data.swipeMousePressed == True:
        if 285 <= event.x <= 360 and data.height-300 <= event.y <= data.height-215:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            data.swipeMousePressed = False
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
            data.swipeMousePressed = False
        
        
    #Control 2b
    if data.currQuestion == "Turn down volume from control center." and data.swipeMousePressed == True:
        if 380 <= event.x <= 455 and data.height-300 <= event.y <= data.height-215:
            data.correctAnswer = True
            data.pause = False
            data.questionIndex = 0
            data.swipeMousePressed = False
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
            data.swipeMousePressed = False
            
    #Control 3a
    if data.currQuestion == "Go to network menu from control center." and data.hold == True:
        if 95 <= event.x <= 265 and data.height-570 <= event.y <= data.height-400:
            if data.holdTime >= 10:
                data.correctAnswer = True
                data.pause = False
                data.questionIndex = 0
                data.hold = False
                data.holdTime = 0
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
                data.holdTime = 0
                data.hold = False
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.holdTime = 0
            data.hold = False
            
            
    #Control 3b
    if data.currQuestion == "Go to music menu from control center." and data.hold == True:
        if 285 <= event.x <= 455 and data.height-570 <= event.y <= data.height-400:
            if data.holdTime >= 10:
                data.correctAnswer = True
                data.pause = False
                data.questionIndex = 0
                data.hold = False
                data.holdTime = 0
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
                data.holdTime = 0
                data.hold = False
        else:
            data.correctAnswer = False
            data.questionIndex = 0
            data.pause = True
            data.tries += 1
            data.holdTime = 0
            data.hold = False