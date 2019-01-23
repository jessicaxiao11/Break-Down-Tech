from tkinter import *
import math
import string
import random
import re
import decisionTree
import playGameJustifyText

####################################
# playGame mode, redrawAll
####################################

def playGameRedrawAll(canvas, data):
    #background color
    canvas.create_rectangle(0,0, data.width, data.height, fill = "old lace", outline = "old lace")
    
    
    #iphone display
    x1,y1,x2,y2,r = 50,25, 500, data.height-25, 100
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
    #black screen
    canvas.create_rectangle(75, 100, 475, data.height-100, fill = "black")
    #long camera buttons
    camx1,camy1,camx2,camy2,r = 240,60, 315, 69, 9
    camPoints = (camx1+r, camy1, camx1+r, camy1, camx2-r, camy1, camx2-r, camy1, camx2, camy1, camx2, camy1+r, camx2, camy1+r, camx2, camy2-r, camx2, camy2-r, camx2, camy2, camx2-r, camy2, camx2-r, camy2, camx1+r, camy2, camx1+r, camy2, camx1, camy2, camx1, camy2-r, camx1, camy2-r, camx1, camy1+r, camx1, camy1+r, camx1, camy1)
    canvas.create_polygon(camPoints, fill = "black", smooth=True, outline = "white", width = 3)
    #small circle camera button
    canvas.create_oval(190, 60, 200, 70, fill = "black")
    
    
    #flashing colors
    if data.currMessage == 1 and data.flash:
        if data.flashTime % 10 == 0:
            color = "IndianRed1"
        else:
            color = "peach puff"
    else:
        color = "peach puff"
    
    
    if data.flash and (data.currMessage == 1 or data.currMessage == 2):
        if data.flashTime % 10 == 0:
            color1 = "IndianRed1"
        else:
            color1 = "white"
    else:
        color1 = "white"
    
    #on button (right side)
    x1,y1,x2,y2,r = 500,150, 507, 215, 7
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = color, smooth=True, outline = "peach puff", width = 3)
    #volume button 1
    x1,y1,x2,y2,r = 43,160, 50, 210, 7
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = color, smooth=True, outline = "peach puff", width = 3)
    #volume button 2
    x1,y1,x2,y2,r = 43,230, 50, 280, 7
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = color, smooth=True, outline = "peach puff", width = 3)
    #home button
    canvas.create_oval(275-25, data.height-85, 275+25, data.height-35, fill = color1, outline = "peach puff", width = 2)
    
    #phone display
    if data.currMessage == 2:
        #background
        canvas.create_rectangle(75, 100, 475, data.height-100, fill = "light cyan", outline = "CadetBlue3")
        #service symbol
        canvas.create_rectangle(80, 115, 85, 120, fill = "black")
        canvas.create_rectangle(88, 110, 93, 120, fill = "black")
        canvas.create_rectangle(96, 105, 101, 120, fill = "black")
        #battery symbol
        canvas.create_rectangle(445, 105, 467, 120, fill = "light cyan", outline = "black")
        canvas.create_rectangle(467, 110, 470, 115, fill = "light cyan", outline = "black")
        canvas.create_rectangle(445, 105, 460, 120, fill = "green2")
        #clock
        canvas.create_text(275, 250, text = "11:11", font = "Avenir 80")
        #date
        canvas.create_text(275, 300, text = "Saturday, January 1", font = "Avenir 25")
        #bottom unlock
        canvas.create_text(275, data.height-120, text = "Press home to unlock", font = "Avenir 20")
        
    if data.currMessage == 3 and data.correctAnswer == True or data.currMessage == 4:
        #background
        canvas.create_rectangle(75, 100, 475, data.height-100, fill = "light cyan", outline = "CadetBlue3")
        #service symbol
        canvas.create_rectangle(80, 115, 85, 120, fill = "black")
        canvas.create_rectangle(88, 110, 93, 120, fill = "black")
        canvas.create_rectangle(96, 105, 101, 120, fill = "black")
        #battery symbol
        canvas.create_rectangle(445, 105, 467, 120, fill = "light cyan", outline = "black")
        canvas.create_rectangle(467, 110, 470, 115, fill = "light cyan", outline = "black")
        canvas.create_rectangle(445, 105, 460, 120, fill = "green2")
        
        #time
        canvas.create_text(275, 115, text = "11:11", font = "Avenir 15")
        if data.currQuestion in data.controlQuestions:
            #flashlight button
            x1,y1,x2,y2,r = 95,data.height-195, 170, data.height-120, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            
            #calculator button
            x1,y1,x2,y2,r = 190,data.height-195, 265, data.height-120, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            
            #timer button
            x1,y1,x2,y2,r = 285,data.height-195, 360, data.height-120, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            
            #battery button
            x1,y1,x2,y2,r = 380,data.height-195, 455, data.height-120, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            
            #screen mirroring button
            x1,y1,x2,y2,r = 95,data.height-285, 265, data.height-215, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            
            #brightness button
            x1,y1,x2,y2,r = 285,data.height-385, 360, data.height-215, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            canvas.create_oval(310, data.height-260, 335, data.height-235, fill = "gray80", outline = "gray80")
            cx, cy, r = 322, data.height-245, 14
            for i in range(8):
                x = 2*r*math.cos(2*math.pi/8*i)
                y = 2*r*math.sin(2*math.pi/8*i)
                canvas.create_line(cx, cy, cx+x, cy+y, fill = "gray80")
                
            canvas.create_line(285, data.height-300, 360, data.height-300, fill = "DodgerBlue2", width = 5)
            
            #volume button
            x1,y1,x2,y2,r = 380,data.height-385, 455, data.height-215, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            canvas.create_polygon(400, data.height-300, 415, data.height-300, 430, data.height-320, 430, data.height-250, 415, data.height-270, 400, data.height-270, fill = "gray80")
            canvas.create_line(380, data.height-350, 455, data.height-350, fill = "DodgerBlue2", width = 5)

            
            #screen rotation button
            x1,y1,x2,y2,r = 95,data.height-380, 170, data.height-305, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            canvas.create_oval(132 - 20, data.height-342-20, 132 + 20, data.height-342+20, fill = "red", outline = "red")
            canvas.create_oval(132 - 18, data.height-342-18, 132 + 18, data.height-342+18, fill = "white", outline = "white")
            canvas.create_rectangle(132-10, data.height-342-5, 132+10, data.height-342+10, fill = "red", outline = "red")
            canvas.create_oval(132-5, data.height-342-10-6, 132+5, data.height-342-10+6, fill = "red", outline = "red")
            canvas.create_oval(132-3, data.height-342-10-4, 132+3, data.height-342-10+4, fill = "white", outline = "white")
            
            #do not disturb button
            x1,y1,x2,y2,r = 190,data.height-380, 265, data.height-305, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            canvas.create_oval(227-20, data.height-342-20, 227+20, data.height-342+20,fill = "gray80", outline = "gray80")
            canvas.create_oval(227-20+15, data.height-342-20-15, 227+20+15, data.height-342+20-15,fill = "white", outline = "white")
            
            #network button
            x1,y1,x2,y2,r = 95,data.height-570, 265, data.height-400, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            canvas.create_oval(137-30, 247-30, 137+30, 247+30, fill = "gray80", outline = "gray80")
            canvas.create_oval(223-30, 247-30, 223+30, 247+30, fill = "green2", outline = "green2")
            canvas.create_oval(137-30, 333-30, 137+30, 333+30, fill = "DodgerBlue2", outline = "DodgerBlue2")
            canvas.create_oval(223-30, 333-30, 223+30, 333+30, fill = "DodgerBlue2", outline = "DodgerBlue2")

            
            #music button
            x1,y1,x2,y2,r = 285,data.height-570, 455, data.height-400, 30
            points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
            canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 3)
            canvas.create_polygon(350, 290-20, 350, 290+20, 390, 290, fill = "gray80", outline = "gray80")
        else:
            #home page
            #imessage
            if 100-data.sx >= 75 and 190-data.sx <= 475 and 160-data.sy >= 100 and 250-data.sy <= data.height-100:
                x1,y1,x2,y2,r = 100-data.sx, 160-data.sy, 190-data.sx, 250-data.sy, 20
                points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
                canvas.create_polygon(points, fill = "green2", smooth=True, outline = "green2")
                canvas.create_oval(110-data.sx, 175-data.sy, 180-data.sx, 235-data.sy, fill = "white", outline = "white")
                canvas.create_polygon(175-data.sx, 210-data.sy, 165-data.sx, 225-data.sy, 187-data.sx, 243-data.sy, fill = "white", outline = "white")
            
            #camera
            if 220-data.sx >= 75 and 310-data.sx <= 475 and 160-data.sy >= 100 and 250-data.sy <= data.height-100:
                x1,y1,x2,y2,r = 220-data.sx, 160-data.sy, 310-data.sx, 250-data.sy, 20
                points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
                canvas.create_polygon(points, fill = "gray70", smooth=True, outline = "gray70")
                canvas.create_rectangle(240-data.sx, 190-data.sy, 290-data.sx, 220-data.sy, fill = "black", outline = "black")
                canvas.create_oval(265-10-data.sx, 205-10-data.sy, 265+10-data.sx, 205+10-data.sy, fill = "black", outline = "gray70")
                canvas.create_rectangle(255-data.sx, 185-data.sy, 275-data.sx, 190-data.sy, fill = "black")
                
            #search box
            if data.currQuestion == "Swipe down in the middle of the screen to use search bar." and 100-data.sx >= 75 and 450-data.sx <= 475 and 60-data.sy >= 100 and 90-data.sy <= data.height-100:
                x1,y1,x2,y2,r = 100-data.sx, 60-data.sy, 450-data.sx, 90-data.sy, 20
                points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
                canvas.create_polygon(points, fill = "gray90", smooth=True, outline = "gray90")
                canvas.create_text(275-data.sx, 75-data.sy, text = "Search", font = "Courier 20")
            
            #control center box
            if data.height-100-data.sy < data.height-100:
                canvas.create_rectangle(75, data.height-100-data.sy, 475, data.height-100, fill = "gray90", outline = "gray90")
                
            #notifications
            if data.currQuestion == "Swipe down from the top to see notifications." and 100-data.sx >= 75 and 450-data.sx <= 475 and 60-data.sy >= 100 and 120-data.sy <= data.height-100:
                x1,y1,x2,y2,r = 100-data.sx, 60-data.sy, 450-data.sx, 120-data.sy, 20
                points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
                canvas.create_polygon(points, fill = "gray90", smooth=True, outline = "gray90")
                canvas.create_text(275-data.sx, 75-data.sy, text = "Notification", font = "Courier 20")
                
            #second page
            #reminder app
            if 500-data.sx >= 75 and 590-data.sx <= 475 and 160-data.sy >= 100 and 250-data.sy <= data.height-100:
                x1,y1,x2,y2,r = 500-data.sx, 160-data.sy, 590-data.sx, 250-data.sy, 20
                points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
                canvas.create_polygon(points, fill = "white", smooth=True, outline = "white")
                canvas.create_oval(510-data.sx, 170-data.sy, 525-data.sx, 185-data.sy, fill = "orange", outline = "orange")
                canvas.create_oval(510-data.sx, 195-data.sy, 525-data.sx, 210-data.sy, fill = "blue", outline = "blue")
                canvas.create_oval(510-data.sx, 220-data.sy, 525-data.sx, 235-data.sy, fill = "green", outline = "green")
                canvas.create_line(530-data.sx, 170-data.sy, 590-data.sx, 170-data.sy, fill = "grey")
                canvas.create_line(530-data.sx, 190-data.sy, 590-data.sx, 190-data.sy, fill = "grey")
                canvas.create_line(530-data.sx, 210-data.sy, 590-data.sx, 210-data.sy, fill = "grey")
                canvas.create_line(530-data.sx, 230-data.sy, 590-data.sx, 230-data.sy, fill = "grey")

                
            
            #facetime
            if 620-data.sx >= 75 and 710-data.sx <= 475 and 160-data.sy >= 100 and 250-data.sy <= data.height-100:
                x1,y1,x2,y2,r = 620-data.sx, 160-data.sy, 710-data.sx, 250-data.sy, 20
                points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
                canvas.create_polygon(points, fill = "green2", smooth=True, outline = "green2")
                canvas.create_rectangle(640-data.sx, 190-data.sy, 670-data.sx, 220-data.sy, fill = "white", outline = "white")
                canvas.create_polygon(673-data.sx, 200-data.sy, 690-data.sx, 195-data.sy, 690-data.sx, 215-data.sy, 673-data.sx, 210-data.sy, fill = "white", outline = "white")
                
            #widgets page
            if -300-data.sx >= 75 and 50-data.sx <= 475 and 160-data.sy >= 100 and 230-data.sy <= data.height-100:
                #search box
                x1,y1,x2,y2,r = -300-data.sx, 160-data.sy, 50-data.sx, 230-data.sy, 20
                points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
                canvas.create_polygon(points, fill = "gray90", smooth=True, outline = "gray90")
                canvas.create_text(-125-data.sx, 195-data.sy, text = "Search", font = "Courier 20")

            if -300-data.sx >= 75 and 50-data.sx <= 475 and 245-data.sy >= 100 and 345-data.sy <= data.height-100:
                #siri app suggestions
                x1,y1,x2,y2,r = -300-data.sx, 245-data.sy, 50-data.sx, 345-data.sy, 20
                points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
                canvas.create_polygon(points, fill = "gray90", smooth=True, outline = "gray90")
                canvas.create_text(-125-data.sx, 295-data.sy, text = "Siri App Suggestions", font = "Courier 20")


    
    #gameplay
    
    #textbox
    x1,y1,x2,y2,r = 700,25, data.width-50, data.height-100, 100
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = "white", smooth=True, outline = "peach puff", width = 10)
    
    #return to menu
    x1,y1,x2,y2,r = data.width-200,data.height-75, data.width-50, data.height-25, 20
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    canvas.create_polygon(points, fill = "coral1", smooth=True, outline = "coral1", width = 2)
    canvas.create_text(data.width-125, data.height-50, text = "Main Menu", font = "Courier 20", fill = "white")
    
    
    #text
    if data.newBadge == False:
        if data.currMessage != 4:
            for i in range(0,data.messageIndex):
                cx = (30*i % 650) + 725
                cy = (30*i // 650)*50 + 100
                message = playGameJustifyText.justify(data.messages[data.currMessage])
                canvas.create_text(cx, cy, text = str(message[i]), font = "Courier 50")
        else:
            for i in range(0,data.questionIndex):
                cx = (30*i % 650) + 725
                cy = (30*i // 650)*50 + 100
                question = playGameJustifyText.justify(data.currQuestion)
                canvas.create_text(cx, cy, text = str(question[i]), font = "Courier 50")
    else:
        for i in range(0,data.badgeIndex):
            cx = (30*i % 650) + 725
            cy = (30*i // 650)*50 + 100
            badge = playGameJustifyText.justify(data.currBadge)
            canvas.create_text(cx, cy, text = str(badge[i]), font = "Courier 50")
        
    #correct, incorrect message
    if data.answerQuestion:
        if data.correctAnswer == False:
            canvas.create_text(700+350, 100, text = "Sorry, try again!", font = "Courier 50")