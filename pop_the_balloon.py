#########################################
# Programmer: Mrs. G
# Date: 20/03/2014
# File Name: pop_the_balloon.py
# Description: This program is a template for a game.
#########################################

import pygame
pygame.init()

from math import sqrt                   # only sqrt function is needed from the math module
from random import randint              # only randint function is needed from the random module

HEIGHT = 600
WIDTH  = 800
game_window=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)                   #
BLACK = (  0,  0,  0)                   # used colours
outline=0                               # thickness of the shapes' outline

#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)# Pythagorean theorem    

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():
    game_window.fill(BLACK)
    pygame.draw.circle(game_window, balloonCLR, (balloonX, balloonY), balloonR, outline)
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings
       
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
exit_flag = False


balloonX = randint(0, WIDTH)            # initialize the coordinates and the size of the balloon
balloonY = randint(HEIGHT/2, HEIGHT)
balloonR = randint(20,50)
balloonSPEED = randint(1,5)
balloonCLR = WHITE

while not exit_flag:                    #
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exit_flag = True            # Flag that we are done so we exit this loop

# act upon mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            (cursorX,cursorY)=pygame.mouse.get_pos()
            if distance(cursorX, cursorY, balloonX, balloonY)< balloonR:
                balloonX, balloonY = 0,0
                
# move the balloon
    balloonY = balloonY - balloonSPEED
# update the screen    
    redraw_game_window()
    pygame.time.delay(100)
    
pygame.quit()                           # always quit pygame when done!
