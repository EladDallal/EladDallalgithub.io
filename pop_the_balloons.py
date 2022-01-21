#########################################
# Programmer: Mrs. G
# Date: 20/03/2014
# File Name: pop_the_balloons.py
# Description: This program is a template for a game. It demonstrates use of lists.
#########################################

import pygame
pygame.init()

from math import sqrt                   # only sqrt function is needed from the math module
from random import randint              # only randint function is needed from the random module

WIDTH = 800
HEIGHT  = 600

game_window=pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)                   #
BLACK = (  0,  0,  0)                   # used colours
RED = (255, 0, 0)


outline=0                               # thickness of the shapes' outline

x = 40
count = 0
missed = x

font = pygame.font.SysFont("Courier New Bold",36)
font2 = pygame.font.SysFont("Courier New Bold",50)

bg = pygame.image.load("Background1.png")
end = pygame.image.load("gameover1.png")
mouse = pygame.image.load("knifepopper1.png")


ending = False

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
    
    for i in range(x):
        if balloonVisible[i]:
            pygame.draw.circle(game_window, balloonClear[i], (balloonX[i], balloonY[i]), balloonR[i], outline)

    seconds = pygame.time.get_ticks() // 1000
    time = font.render ("Time: " + str(seconds), 10, WHITE)
    game_window.blit(time, (650,25))

    score = font.render ("Score: " + str(count), 10, WHITE)
    game_window.blit (score, (50,25))

    print("Time: ", seconds)
    print("Popped: ", count)
    print("Missed: ", missed)

    (cursorX, cursorY) = pygame.mouse.get_pos()
    game_window.blit(mouse, (cursorX-10, cursorY-10))
    
        
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings



def endPage():
    global missed

    pygame.mouse.set_visible(True)
    missed -= count


    game_window.blit(end, (0,0))
    score2 = font2.render("Score: " + str(count), 1, BLACK)
    miss = font2.render("Missed: " + str(missed), 1, BLACK)


    game_window.blit(score2, (643, 565))
    game_window.blit(miss, (7,565))


    pygame.display.update()

    
    
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
exit_flag = False                       #


balloonR = [0]*x                       # create lists of 20 items each
balloonX = [0]*x                       # for balloons' properties
balloonY = [0]*x                       #
balloonSPEED = [0]*x                   #
balloonVisible = [True]*x
balloonClear = [WHITE]*x
for i in range(x):
    balloonX[i] = randint(0, WIDTH)     # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(HEIGHT/2, HEIGHT)
    balloonR[i] = randint(20,50)
    balloonSPEED[i] = randint(3,7)
    balloonClear[i] = randint(1,255), randint(1,255), randint (1,255)


while not exit_flag:                    #
    pygame.display.update()
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            pygame.quit()            # Flag that we are done so we exit this loop

# act upon mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(x):
                pygame.mouse.set_visible(False)
                (cursorX,cursorY)=pygame.mouse.get_pos()
                if distance(cursorX, cursorY, balloonX[i], balloonY[i])< balloonR[i]:
                    balloonVisible[i] = False
                    count += 1
                    
# move the balloons
    for i in range(x):
        balloonY[i] = balloonY[i] - balloonSPEED[i]
        if balloonY[i]<-balloonR[i]:
            balloonVisible[i] = False

            
# update the screen    
    redraw_game_window()
    pygame.time.delay(1)

    if True not in balloonVisible:
        exit_flag = True

pygame.time.delay(500)
endPage()
game.time.delay(1000000)
    
pygame.quit()                           # always quit pygame when done!
