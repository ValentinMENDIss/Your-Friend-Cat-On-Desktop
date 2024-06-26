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
CAT_IDLE = pygame.image.load(os.path.join("graphics", "orange_cat_idle(128x128).png"))

CAT_SLEEPING = pygame.image.load(os.path.join("graphics", "orange_cat_sleeping.png"))


## COLOURS ## 
transparency_color = (255, 0, 128)
dark_red = (139, 0, 0)

####################################################################

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency_color), 0, win32con.LWA_COLORKEY)


# Clock Varibable ( is being created from pygame module)
clock = pygame.time.Clock()


## VARIABLES ##

# Coordinates
X_COORDINATES = 0
Y_COORDINATES = 0

# Other
action = random.randint(1, 100)     # Generate Random Number ( you can see this as percentage % ), needed for giving an action to the cat :)
Clock = time()

LEFT = 0                    # DEGREES DOESN'T MATTER ( THEY ARE THERE TO GIVE NEW VARIABLE FOR CAT_DIRECTION :) )
RIGHT = 90
CAT_DIRECTION = LEFT

CAT_SLEEPS = False
CAT_IDLE_OR_MOVING = True

## MAIN LOOP ##
while run:

    MOUSE_POS = pyautogui.position()

    for event in pygame.event.get():                                                # For every Event in Pygame: 
        if event.type == pygame.QUIT:                                               # If event QUIT was used(if button quit was pressed):
            run = False

    window = pyautogui.getWindowsWithTitle("Cat")[0]
    rect = window._rect
    

    if action in range(1, 70):       
        CAT_IDLE_OR_MOVING = True
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
            pygame.time.wait(time_wait)
            X_COORDINATES = random.randint(0, DISPLAY_X)
            Y_COORDINATES = random.randint(0, DISPLAY_Y)
            action = random.randint(1, 100)

    

    # accessing tuples ( x, y coordinates of the cursor)
    MOUSE_X = MOUSE_POS[0]
    MOUSE_Y = MOUSE_POS[1]

    if action in range(81, 100):
        CAT_IDLE_OR_MOVING = True

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
            pygame.time.wait(time_wait)
            action = random.randint(1, 100)

     
    if action in range(70, 81):
        
        CAT_SLEEPS = True
        CAT_IDLE_OR_MOVING = False

        if time() - Clock > random.randint(45, 300):    # random number would be generated for how long does it need to wait / perform an action ( numbers are in range of  ( 45s - 300s ( 5min )  )
            action = random.randint(1, 100)
            CAT_SLEEPS = False



    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)    
    # win32gui.MoveWindow(hwnd, 0, 0, 128, 128, True)

    SCREEN.fill(transparency_color)
        
    if CAT_IDLE_OR_MOVING == True:
        if CAT_DIRECTION == RIGHT:
            CAT_IDLE_COPY = CAT_IDLE.copy()

            CAT_RIGHT = pygame.transform.flip(CAT_IDLE_COPY, True, False)
            SCREEN.blit(CAT_RIGHT, (0, 0))


        if CAT_DIRECTION == LEFT:
            SCREEN.blit(CAT_IDLE, (0, 0))

    if CAT_SLEEPS == True:
        SCREEN.blit(CAT_SLEEPING, (0, 0))


    clock.tick(60)
    pygame.display.update()
    
    
