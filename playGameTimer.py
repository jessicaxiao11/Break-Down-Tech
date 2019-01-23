from tkinter import *
import math
import string
import random
import re
import decisionTree
import playGameJustifyText



####################################
# playGame mode, timerFired
####################################

def playGameTimerFired(data):
    if not data.newBadge:
        #loops through current message to be shown on screen letter by letter
        if not data.pause and data.currMessage < len(data.messages): 
            message = playGameJustifyText.justify(data.messages[data.currMessage])
            if data.messageIndex < len(message):
                data.messageIndex += 1
                data.correctAnswer = None
                #after reaching end of message
                if data.messageIndex == len(message):
                    #proceeds to next message if first prompt
                    if data.currMessage != 1 and data.currMessage != 2 and data.currMessage != 3:
                        data.pause = True
                    #waits for user to answer question for other prompts
                    else:
                        data.flash = True
                        data.answerQuestion = True
        #allows for some pause time between first prompt and second
        if data.pause == True and data.currMessage == 0:
            data.pauseTime += 1
            if data.pauseTime == 20:
                data.pause = False
                data.pauseTime = 0
                data.currMessage += 1
                data.messageIndex = 0
        #buttons change colors depending on flash time
        if data.flash:
            data.flashTime += 1
        #stops flashing after question answered
        if data.correctAnswer:
            if data.currMessage == 2:
                data.flash = False
            #awards beginner's badge
            elif data.currMessage == 3 and data.score == 2 and data.badScore == 0 and data.numBadges == 0 and data.badges[0] not in data.seenBadges:
                data.pause = False
                data.newBadge = True
                data.currBadge = data.badges[0]
                data.seenBadges.add(data.badges[0])
    else:
        #loops through current badge message to be shown on screen letter by letter
        badge = playGameJustifyText.justify(data.currBadge)
        if data.badgeIndex < len(badge):
            data.badgeIndex += 1
            #after reaching end of message
            if data.badgeIndex == len(badge):
                data.pause = True
        if data.pause == True and data.newBadge == True:
            data.pauseTime += 1
            if data.pauseTime == 20:
                data.pause = False
                data.pauseTime = 0
                data.newBadge = False
                data.numBadges += 1
    if data.newBadge == False and data.currMessage == 3:
        data.currMessage += 1
    #all beginning prompts are finished, dynamically generated questions should start now
    if data.currMessage == 4 and data.displayAction == False:
        # data.correctAnswer = None
    #increase question index and set current question, record point value of current question along with data.tries
        #starts out with random level 1 question
        if data.questionIndex == 0 and data.pause == False:
            if data.numQuestions == 0:
                data.currQuestion = retrieveFirstQuestion(data)
            else:
                data.currQuestion = retrieveNextQuestion(data)
            if data.currQuestion != None:
                data.currQValue = data.allPrompts[data.currQuestion][0]
                data.currGroup = data.allPrompts[data.currQuestion][2]
                data.allPrompts[data.currQuestion] = (data.currQValue, True, data.currGroup)
                data.numQuestions += 1
                data.tries = 0
                if data.currQuestion == "Go to the left most page with widgets (you are two pages away).":
                    data.sx = 400
                else:
                    data.sy = 0
            else:
                data.currQuestion = "You have finished!"
        if not data.pause:
            if not data.newBadge:
                question = playGameJustifyText.justify(data.currQuestion)
                if data.questionIndex < len(question):
                    data.questionIndex += 1
                    #after reaching end of message
                    if data.questionIndex == len(question):
                            data.answerQuestion = True
        #consecutive tries badge
        if data.consecTries == 5 and data.badges[2] not in data.seenBadges:
            data.pause = False
            data.newBadge = True
            data.currBadge = data.badges[2]
            data.seenBadges.add(data.badges[2])
            data.numBadges += 1
        #no mistakes for entire category badge
        groupCounts = {"Swipe":0, "Button":0, "Control":0}
        for prompt in data.promptTries:
            if data.promptTries[prompt] == 0:
                group = prompt[0]
                groupCounts[group] += 1
        for i in groupCounts:
            if groupCounts[i] == 3 and data.badges[1] not in data.seenBadges:
                data.pause = False
                data.newBadge = True
                data.currBadge = data.badges[1]
                data.seenBadges.add(data.badges[1])
                data.numBadges += 1
    if data.currQuestion in {"Use button to shut down phone.", "Use home button to call siri.", "Go to music menu from control center.", "Go to network menu from control center."} and data.hold == True:
        data.holdTime += 1
    if data.displayAction == True:
        #increasing sx = swiping right 
        #increasing sy = swiping up
        if data.currQuestion == "Go to the page on the right.":
            data.sy = 0
            data.sx += 10
            if data.sx % 400 == 0:
                data.displayAction = False
        elif data.currQuestion == "Go to the page on the left.":
            data.sy = 0
            data.sx -= 10
            if data.sx % 400 == 0:
                data.displayAction = False
        elif data.currQuestion == "Go to the left most page with widgets (you are two pages away).":
            data.sy = 0
            data.sx -= 20
            if data.sx == -400:
                data.displayAction = False
        elif data.currQuestion == "Swipe down in the middle of the screen to use search bar.":
            data.sx = 0
            data.sy -= 10
            if data.sy == -100:
                data.displayAction = False
        elif data.currQuestion == "Swipe down from the top to see notifications.":
            data.sx = 0
            data.sy -= 10
            if data.sy == -100:
                data.displayAction = False
        elif data.currQuestion == "Swipe up from bottom to see control center.":
            data.sx = 0
            data.sy += 10
            if data.sy % 200 == 0:
                data.displayAction = False

 
#find a lowest level question such that the level in that category has not been seen
#category defaults to data based on global users
def retrieveFirstQuestion(data):
    category = predictCategory(data)
    for level in range(1,4):
        for prompt in data.allPrompts:
            if data.allPrompts[prompt][2] == category and data.allPrompts[prompt][0] == level and data.allPrompts[prompt][1] == False:
                #checks if level in category has been seen before
                if unseen(data, level, data.allPrompts[prompt][2]):
                    return prompt
    return nextQuestion(data,1,category)

def retrieveNextQuestion(data, depth = 0, level = None, seenGroups = None):
    #base case
    if depth == 0:
        if data.tries == 0:
            predictedLevel = data.currQValue + 1
            if predictedLevel > 4:
                predictedLevel = 4 
        else:
            predictedLevel = math.ceil(data.currQValue - data.tries/2)
            if predictedLevel < 1:
                predictedLevel = 1
        predictedGroup = data.currGroup
        if data.tries == 0 and data.currQValue == 3:
            return retrieveNextQuestion(data, depth = 1, level = predictedLevel, seenGroups = [predictedGroup])
        else:
            #stays in same category, it is guaranteed that each category has multiple of each level
            return nextQuestion(data,predictedLevel, predictedGroup)
    else:
        #fetch list of categories
        categories = set()
        for prompt in data.allPrompts:
            categories.add(data.allPrompts[prompt][2])
        #loop through possible categories
        for possibleGroup in categories:
            #if possibleGroup is not equal to seen groups (that do not work)
            if possibleGroup not in seenGroups:
                predictedGroup = possibleGroup
                for predictedLevel in range(1,4):
                    #level in new group cannot be seen yet (there's no point in repeating a seen level in a category)
                    if unseen(data, predictedLevel, predictedGroup):
                        return nextQuestion(data, predictedLevel, predictedGroup)
                #adds possible group to seen groups if doesn't work
                seenGroups.append(possibleGroup)
                retrieveNextQuestion(data, depth = 1, level = predictedLevel, seenGroups = seenGroups)
        #if all groups are seen, category defaults to data based on users' tries (global users)
        predictedGroup = predictCategory(data)
        if data.currGroup == predictedGroup:
            if data.currQValue != 3:
                predictedLevel = data.currQValue + 1
            else:
                predictedLevel = dta.currQValue
        else:
            predictedLevel = 1
        return nextQuestion(data,predictedLevel,predictedGroup)


def predictCategory(data):
    #totals tries across all users, except for current user
    swipeTries, buttonTries, controlTries = 0,0,0
    for user in data.allUsers:
        if user != data.currUser:
            swipeTries += data.allUsers[user][5]["Swipe"]
            buttonTries += data.allUsers[user][5]["Button"]
            controlTries += data.allUsers[user][5]["Control"]
    #current user's tries
    cSwipeTries = data.categoryTries["Swipe"]
    cButtonTries = data.categoryTries["Button"]
    cControlTries = data.categoryTries["Control"]
    currData = [[swipeTries, buttonTries, controlTries, cSwipeTries, cButtonTries, cControlTries]]
    #result will return in list format
    result = decisionTree.decisionTree(decisionTree.dataset, currData, 10, 1)
    return result[0]
    
def isValid(data, predictedLevel, predictedGroup):
    for prompt in data.allPrompts:
        if predictedLevel == data.allPrompts[prompt][0] and predictedGroup == data.allPrompts[prompt][2]:
            return True
    return False
    
def nextQuestion(data, predictedLevel, predictedGroup):
    prompts = []
    for prompt in data.allPrompts:
        if predictedLevel == data.allPrompts[prompt][0] and predictedGroup == data.allPrompts[prompt][2]:
            prompts.append(prompt)
    #randomly chooses a prompt, if unseen then returns it, or randomly chooses until an unseen prompt is chosen. if no unseen prompts (then the size of the set == 2) and it randomly chooses from prompt list
    difPrompts = set()
    while len(difPrompts) < 2:
        potentialPrompt = random.choice(prompts)
        if data.allPrompts[potentialPrompt][1] == False:
            return potentialPrompt
        difPrompts.add(potentialPrompt)
    return random.choice(prompts)
    
def unseen(data, predictedLevel, predictedGroup):
    if isValid(data,predictedLevel,predictedGroup):
        for prompt in data.allPrompts:
            if predictedLevel == data.allPrompts[prompt][0] and \
            predictedGroup == data.allPrompts[prompt][2]:
                if data.allPrompts[prompt][1] == True:
                    return False
    return True