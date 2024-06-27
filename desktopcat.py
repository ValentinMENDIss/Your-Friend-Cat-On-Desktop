#### YOUR-FRIEND-CAT-ON-DESKTOP 
#### MADE BY VALENTIN AND PUBLISHED ON GITHUB PAGE OF MY ACCOUNT ( ValentinMENDIss )
#### LAST TIME EDITED ON:  26.06.2024
### I Hope you would enjoy. And DO NOT hurt a cat, pls. ... :)
## Have Fun :) 
#


import pygame
import os
import win32gui, win32api, win32con
import random
import subprocess
import pyautogui


from win32api import GetSystemMetrics
from time import sleep, time
from pygame import mixer 



pygame.init()                                                   # Initialize Pygame Engine
 
SCREEN = pygame.display.set_mode((128, 128), pygame.NOFRAME) 
pygame.display.set_caption('Cat')


### VARIABLES ###

# Coordinates
x_pos = 0 
y_pos = 0

# Generate random numbers
random_pos = random.randint(0, 500)
time_wait = random.randint(4500, 30000)        # Time to wait ( clock variable ) is being generated in range of numbers ( 4.5 seconds and 30 seconds )     ( in ms )


## GET COORDINATES: ##
# Display Resolution ( Gets Resolution of your Monitor / Display  Automaticly )
DISPLAY_X = GetSystemMetrics(0)
DISPLAY_Y = GetSystemMetrics(1)
#MOUSE_POS = pyautogui.position()

# Loop Variable
run = True

# Cat's Variables 
velocity = 1


## SPRITES ( IMAGES FOR CERTAIN ACTIONS ) ##
CAT_IDLE_IMG = pygame.image.load(os.path.join("graphics", "orange_cat_idle(128x128).png"))

CAT_MOVING_IMG = [pygame.image.load(os.path.join("graphics", "orange_cat_walking1.png")),
              pygame.image.load(os.path.join("graphics", "orange_cat_walking2.png"))]

CAT_MOVING_RIGHT_IMG = [pygame.image.load(os.path.join("graphics", "orange_cat_walking1_right.png")),
                        pygame.image.load(os.path.join("graphics", "orange_cat_walking2_right.png"))]

CAT_SLEEPING_IMG = pygame.image.load(os.path.join("graphics", "orange_cat_sleeping.png"))


CAT_IDLE_RECT = CAT_IDLE_IMG.get_rect()
CAT_SLEEPING_RECT = CAT_SLEEPING_IMG.get_rect()

## COLOURS ## 
transparency_color = (255, 0, 128)
dark_red = (139, 0, 0)

## SFXs / MUSIC ##
mixer.init()
mixer.music.set_volume(0.7)
####################################################################

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency_color), 0, win32con.LWA_COLORKEY)


# Clock Varibable ( is being created from pygame module)
clock = pygame.time.Clock()


## VARIABLES ##

# Coordinates #
X_COORDINATES = random.randint(0, DISPLAY_X)
Y_COORDINATES = random.randint(0, DISPLAY_Y)

# Other #
action = random.randint(1, 100)     # Generate Random Number ( you can see this as percentage % ), needed for giving an action to the cat :)
Clock = time()

LEFT = 0                    # DEGREES DOESN'T MATTER ( THEY ARE THERE TO GIVE NEW VARIABLE FOR CAT_DIRECTION :) )
RIGHT = 90
CAT_DIRECTION = LEFT
ACTION = True

# Cat actions #
CAT_SLEEPS = False
CAT_MOVING = True
CAT_IDLE = False

# SFXs / Music #
SFX_MEOW = False




## Timer ( for Animation ) ##

fps = 0
timer_in_seconds = 0

## MAIN LOOP ##
while run:

    ## TIMER FOR ANIMATION,  MADE BY MYSELF :)   ( because I couldn't figure out the other ways, they haven't worked for me.) ( NEEDED FOR ANIMATION )  ##
    
    fps += 2                                        # TWEAKED: to make images change faster
    if fps == 60:
        fps = 0
        timer_in_seconds += 1
    

    if timer_in_seconds >= 2:                       # If it have been more than 1 second than, ...
        timer_in_seconds = 0                        # Resetting the timer
    
########################################################
    
    MOUSE_POS = pyautogui.position()

    for event in pygame.event.get():                                                # For every Event in Pygame: 
        if event.type == pygame.QUIT:                                               # If event QUIT was used(if button quit was pressed):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if CAT_IDLE_RECT.collidepoint(event.pos) or CAT_SLEEPING_RECT.collidepoint(event.pos): 
                SFX_MEOW = True


    
    window = pyautogui.getWindowsWithTitle("Cat")[0]
    rect = window._rect
    

    if action in range(1, 70):       
        CAT_IDLE = False
        CAT_MOVING = True
        
        
        if ACTION == True:       
            if not abs(rect.x - X_COORDINATES) < velocity or not abs(X_COORDINATES - rect.x) < velocity:        # If rect.x coordinates - X_Coordinates is not smaller than velocity it self ( it means if it is bigger than velocity ):
                if rect.x >= X_COORDINATES: 
                    CAT_DIRECTION = LEFT
                    rect.x -= velocity 
                elif rect.x <= X_COORDINATES:
                    CAT_DIRECTION = RIGHT
                    rect.x += velocity

            if not abs(rect.y - Y_COORDINATES) < velocity or not abs(Y_COORDINATES - rect.y) < velocity:
                if rect.y >= Y_COORDINATES:
                    rect.y -= velocity
                elif rect.y <= Y_COORDINATES:
                    rect.y += velocity
            if abs(rect.x - X_COORDINATES ) < velocity or abs(X_COORDINATES - rect.x ) < velocity and abs(rect.y - Y_COORDINATES) < velocity or abs(Y_COORDINATES - rect.y) < velocity:
                ACTION = False
                CAT_MOVING = False
                CAT_IDLE = True
        
        elif ACTION == False:
        
                pygame.time.wait(time_wait)
                X_COORDINATES = random.randint(0, DISPLAY_X)
                Y_COORDINATES = random.randint(0, DISPLAY_Y)
                
                ACTION = True
                action = random.randint(1, 100)

    

    # accessing tuples ( x, y coordinates of the cursor)
    MOUSE_X = MOUSE_POS[0]
    MOUSE_Y = MOUSE_POS[1]

    if action in range(81, 100):
        CAT_IDLE = False
        CAT_MOVING = True
        
        if ACTION == True:
            if rect.x != MOUSE_X:
                if rect.x >= MOUSE_X:
                    CAT_DIRECTION = LEFT

                    rect.x -= velocity
                elif rect.x <= MOUSE_X:
                    CAT_DIRECTION = RIGHT

                    rect.x += velocity
            if rect.y != MOUSE_Y:
                if rect.y >= MOUSE_Y:
                    rect.y -= velocity
                elif rect.y <= MOUSE_Y:
                    rect.y += velocity
            if rect.x == MOUSE_X and rect.y == MOUSE_Y:
                ACTION = False
                CAT_MOVING = False
                CAT_IDLE = True        
        
        elif ACTION == False:
            
            
            pygame.time.wait(time_wait)
            
            ACTION = True
            action = random.randint(1, 100)

     
    if action in range(70, 81):
        
        CAT_MOVING = False
        CAT_IDLE = False
        CAT_SLEEPS = True

        if pygame.time.get_ticks() - Clock > random.randint(45, 300):    # random number would be generated for how long does it need to wait / perform an action ( numbers are in range of  ( 45s - 300s ( 5min )  )
            action = random.randint(1, 100)
            CAT_SLEEPS = False



    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)    
    # win32gui.MoveWindow(hwnd, 0, 0, 128, 128, True)

    SCREEN.fill(transparency_color)
 
    ## CAT ANIMATION IMAGES ##
    CAT_MOVING_ANIM = CAT_MOVING_IMG[timer_in_seconds // 1] 
    CAT_MOVING_ANIM_RIGHT = CAT_MOVING_RIGHT_IMG[timer_in_seconds // 1]
    
    ## CAT ACTIONS ##
        
    if CAT_MOVING == True:
        if CAT_DIRECTION == RIGHT:
 
            SCREEN.blit(CAT_MOVING_ANIM_RIGHT, (0, 0))

        if CAT_DIRECTION == LEFT:  
            SCREEN.blit(CAT_MOVING_ANIM, (0, 0))

        
    if CAT_IDLE == True:
        SCREEN.blit(CAT_IDLE_IMG, (0, 0))

    if CAT_SLEEPS == True:
        SCREEN.blit(CAT_SLEEPING_IMG, (0, 0))

    ## SFXs / MUSIC ##

    if SFX_MEOW == True:
        mixer.music.load("cat-purring-and-meow.mp3")  
        mixer.music.play()
        SFX_MEOW = False

    clock.tick(60)
    pygame.display.update()
    
    
