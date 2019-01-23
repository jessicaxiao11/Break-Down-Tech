from tkinter import *
import math
import string
import random
import re
import decisionTree


#justifyText
#citation: functions justify, textByWidth, countMissingSpaces, spacesPerLine, moreSpaces, spacedLine coded from week three homework
def justify(text, width=22):
    spacedString = " ".join(text.split()) + " "
    widthString = textByWidth(spacedString, width)
    justifiedString, lineStartIndex = "", 0
    for c in range(len(widthString)):
        if widthString[c] == "\n":
            missingSpaces = countMissingSpaces(widthString[lineStartIndex:c], \
            width)
            if missingSpaces == 0:
                justifiedString += widthString[lineStartIndex:c + 1]
            else:
                spaceCount = spacesPerLine(widthString[lineStartIndex:c])
                x, y = moreSpaces(int(missingSpaces), int(spaceCount))
                justifiedString += spacedLine(widthString[lineStartIndex:c], \
                x, y) + "\n"
            lineStartIndex = c + 1
    # adding last line
    for c in range(lineStartIndex, len(widthString)):
        justifiedString += widthString[c]
    return justifiedString.replace("\n","")

#breaking string by width
def textByWidth(spacedString, width):
    widthString, lastSpace = "", 0
    for c in range(len(spacedString)):
        if spacedString[c] == " ":
            if c + 1 >= len(spacedString): break
            else:
                for nextSpace in range(c + 1, len(spacedString)):
                    if spacedString[nextSpace] == " ":
                        if nextSpace - lastSpace > width:
                            widthString += "\n"
                            lastSpace = c + 1
                            break
                        else:
                            widthString += spacedString[c]
                            break
        elif spacedString[c] == "\n":
            widthString += " "
        else:
            widthString += spacedString[c]       
    return widthString
    
def countMissingSpaces (widthString, width):
    missingSpaces = width - len(widthString)
    return missingSpaces

def spacesPerLine (widthString):
    spaceCount = 0
    for c in range(len(widthString)):
        if widthString[c] == " ":
            spaceCount += 1
    return spaceCount
    
def moreSpaces (missingSpaces, spaceCount):
    addSpaces = missingSpaces // spaceCount
    extraSpaces = missingSpaces % spaceCount
    return addSpaces, extraSpaces
    

def spacedLine (widthString, x, y):
    currentSpaceCount = 0
    spacedString = ""
    for c in range(len(widthString)):
        if widthString[c] == " ":
            currentSpaceCount += 1
            if currentSpaceCount <= y:
                spacedString += x* " " + 2* " "
            else:
                spacedString += x* " " + " "
        else:
            spacedString += widthString[c]
    return spacedString