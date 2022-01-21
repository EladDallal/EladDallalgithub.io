#########################################
# Programmer: Roee Yehezkel
# Date: 21/09/2012
# File Name: snake_template.py
# Description: This program is a template for Snake Game.
#               It demonstrates how to move and lengthen the snake. 
#########################################

import pygame
pygame.init()

from math import sqrt

from random import randrange
from random import randint

HEIGHT = 600
WIDTH  = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,  0,  0)
HEAD = (255,255,255)        # The color of the head of the snake
BODY = (0,255,255)          # the color of the snakes body
outline=0

# the amount of apples that will be on screen at once
appleAmount = 3

startcursorX = 0
startcursorY = 0

#---------------------------------------#
# snake's properties                    #
#---------------------------------------#
BODY_SIZE = 8
HSPEED = 16
VSPEED = 16

# defining all snake related parts
speedX = 0
speedY = -VSPEED
segx = [int(WIDTH/2.)]*3
segy = [HEIGHT, HEIGHT+VSPEED, HEIGHT+2*VSPEED]

# the timer that counts down
countDown = 20

# amount of apples that have been eaten
appleCount = 0

# apple image
apple = pygame.image.load("apple.png")

# saw image
saw = pygame.image.load("saw.png")

# background image
bg = pygame.image.load("background2.png")

# start screen image (which is also just the start screen)
startScreen = pygame.image.load("startScreen2.png")

# end screen image (which is also just the end screen)
ending = pygame.image.load("endScreen2.png")

# first and second fonts for the timer and apple count
font = pygame.font.SysFont("Courier New Bold",50)
font2 = pygame.font.SysFont("Courier New Bold",50)

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#

#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#

# distance function to check the hit boxes on objects like apples and saw
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)    # Pythagorean theorem

# all drawing for the main loop
def redraw_screen():
    # background image
    screen.blit(bg, (0, 0))

    # text that shows the amount of apples eaten
    score = font.render("Apples Eaten: " + str(appleCount), 1, WHITE)
    screen.blit(score, (20, 20))

    # text that shows the timer counting down
    timer = font2.render("Timer: " + str(seconds),1 ,WHITE)
    screen.blit(timer, (600,20))

    # showing the apple image and making sure the apple will only show if the apple visible is True
    for i in range(appleAmount):
        if appleVisible[i] == True:
            screen.blit(apple, (appleX[i],appleY[i]))

    # showing the saw image and making sure the saw will only show if the saw visible is True
    if sawVisible == True:
        screen.blit(saw, (sawX,sawY))

    # checking for the body of the snake and the head
    # making the head of the snake a different color than the body
    for i in range(len(segx)):
        # making the color for the snake whatever the 'BODY' is
        segmentCLR = BODY
        # checks the head which would be index 0
        if i == 0:
            # when it found the head it makes it the color of whatever 'HEAD' is
            segmentCLR = HEAD

        # drawing the snake in the loop
        pygame.draw.circle(screen, segmentCLR, (segx[i], segy[i]), BODY_SIZE, outline)
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings

# defining everything related to the apple at the beginning

# making appleX anywhere on the screen
appleX = [randrange(0,WIDTH, VSPEED)]*appleAmount
# making appleY anywhere on the screen
appleY = [randrange(0,HEIGHT, HSPEED)]*appleAmount
# program draws apples at the beggining of the main loop
appleVisible = [True]*appleAmount
# size of apple
appleS = 25

# defining the apples inside a loop to make it a list that doesnt start with one apple
for i in range(appleAmount):
    appleX[i] = randrange(0,WIDTH, VSPEED)
    appleY[i] = randrange(0,HEIGHT, HSPEED)
    appleVisible[i] = True

# defining the saw and everything relating to the saw

# boolean checking when to draw saw
sawVisible = False
# size of the saw
sawS = 25
# the starting points for the saw are outside of the actual screen (will change later)
sawX = -100
sawY = -100
# the trigger for the saw to come
sawCount = 0

#---------------------------------------#
# the main program begins here          #
#---------------------------------------#

# boolean for start screen
begin = True
# boolean for end screen
endScreen = False

print ("Use the arrows and the space br.")

# intro music for start screen
pygame.mixer.music.load("marioWii.mp3")
pygame.mixer.music.play(-1)

# start screen function
def start():
    # start screen image
    screen.blit(startScreen, (0, 0))
    pygame.display.update()

# if the end screen is False and start screen is True then begin the start screen
while not endScreen and begin:
    # start function drawing the start screen
    start()

    # if mouse is pressed
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # on screen than start Screen is false (starting the main loop) and timer begins counting
            begin = False
            start_ticks = (pygame.time.get_ticks())

#####################################################################################
#################################### MAIN ###########################################
#####################################################################################

# main music for actual game
pygame.mixer.music.load("yoshi.mp3")
pygame.mixer.music.play(-1)

# if both start and end are False then the main loop begins
while not endScreen and not begin:
# check for events
    pygame.event.get()
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:       # If user clicked close
                           # Flag that we are done so we exit this loop
            endScreen = True

    # checks if snake head touches snake body
    # checks the body of the snake and only the body
    for i in range(1, len(segx)):
        # seg[0] being the head if touches the body being seg[i]
        if segx[0] == segx[i] and segy[0] == segy[i]:
            # end screen starts
            endScreen = True

    keys = pygame.key.get_pressed()
# act upon key events

    # all controls
    # if left
    if keys[pygame.K_LEFT] and speedX != HSPEED:
        # move snakeX backwards
        speedX = -HSPEED
        speedY = 0
    # if right
    if keys[pygame.K_RIGHT] and speedX != -HSPEED:
        # move snakeX forwards
        speedX = HSPEED
        speedY = 0
    # if up
    if keys[pygame.K_UP] and speedY != VSPEED:
        # move snakeY up
        speedX = 0
        speedY = -VSPEED
    # if down
    if keys[pygame.K_DOWN] and speedY != -VSPEED:
        # move snakeY down
        speedX = 0
        speedY = VSPEED

    # puts timer in another variable
    seconds = countDown - ((pygame.time.get_ticks() - start_ticks) // 1000)

    # if timer is 0 then end screen starts and main loop stops
    if seconds <= 0:
        endScreen = True

    #pygame.mixer.music.load("point1.mp3")

    # checks for if the snake touches an apple
    for i in range(appleAmount):
        # distance function is used to check this
        if distance(segx[0], segy[0], appleX[i], appleY[i]) < appleS:
            # makes apple visible False (disapearing)
            appleVisible[i] = False
            # both segX and segY extend
            segx.append(segx[-1])           # assign the same x and y coordinates
            segy.append(segy[-1])           # as those of the last segment
            # appleX and appleY change coordinates (making the illusion of another apple apearing)
            appleX[i] = randrange(0, WIDTH, VSPEED)
            appleY[i] = randrange(0, HEIGHT, VSPEED)
            # after apple changes coordinates it becomes visible
            appleVisible[i] = True
            # restarts the timer so every apple eaten the timer goes back to the start
            start_ticks = (pygame.time.get_ticks())
            # adds another apple count which checks the amount of apples eaten
            appleCount += 1

            #pygame.mixer.music.play(-1)

    # when the snake "eats" 5 apples
    if appleCount == 5:
        # body size and speed of snake goes up
        BODY_SIZE = 10
        HSPEED = 20
        VSPEED = 20

    # making the saw count trigger start counting
    sawCount += 1
    # checks if saw count is bigger than 0 and divisible by 100
    # making a trigger for when the saw should be drawn and where
    if sawCount > 0 and sawCount % 100 == 0:
        # drawing the saw
        sawVisible = True
        # changing the coordinates from outside the screen to anywhere in the screen
        sawX = randrange(0, WIDTH, VSPEED)
        sawY = randrange(0, HEIGHT, HSPEED)

    # checks if snake head is touching saw
    if distance(segx[0], segy[0], sawX, sawY) < sawS:
        # drawing the end screen which will end the main loop
        endScreen = True


# move all segments
    # making the parameters and making the snake go from the other side when going out of screen
    for i in range(len(segx)):
        # if snake goes out the right side
        if segx[i] > WIDTH:
            # snake apears on left side
            segx[i] = 0
        # if snake goes left side
        if segx[i] < 0:
            # snake apears on right side
            segx[i] = WIDTH
        # if snake goes down
        if segy[i] > HEIGHT:
            # snake apears up
            segy[i] = 0
        # if snake goes up
        if segy[i] < 0:
            # snake apears down
            segy[i] = HEIGHT

    for i in range(len(segx)-1,0,-1):   # start from the tail, and go backwards:
        segx[i] = segx[i-1]               # every segment takes the coordinates
        segy[i] = segy[i-1]               # of the previous one

# move the head
    segx[0] = segx[0] + speedX
    segy[0] = segy[0] + speedY
# update the screen
    redraw_screen()
    pygame.time.delay(45)

# end screen function
def end():
    # drawing the endscreen and showing the score of how many apples were eaten
    screen.blit(ending, (0,0))
    score = font.render("Apples Eaten: " + str(appleCount), 1, BLACK)
    screen.blit(score, (WIDTH/2, HEIGHT/2-10))
    pygame.display.update()

# end screen music
pygame.mixer.music.load("kirby.mp3")
pygame.mixer.music.play(-1)

# while end screen is True and start screen is not then begin the end screen
while endScreen and not begin:
    # drawing the end screen function
    end()

    # if mouse pressed begin the main loop again
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            endScreen = False

pygame.quit()                           # always quit pygame when done!
