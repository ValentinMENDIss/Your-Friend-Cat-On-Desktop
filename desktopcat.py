#### YOUR-FRIEND-CAT-ON-DESKTOP 
#### MADE BY VALENTIN AND PUBLISHED ON GITHUB PAGE OF MY ACCOUNT ( ValentinMENDIss )
#### LAST TIME EDITED ON:  24.06.2024
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



pygame.init()                                                   # Initialize Pygame Engine
 
SCREEN = pygame.display.set_mode((128, 128), pygame.NOFRAME) 
pygame.display.set_caption('Cat')


## VARIABLES ##

# Coordinates
x_pos = 0 
y_pos = 0

# Generate random numbers
random_pos = random.randint(0, 500)
time_wait = random.randint(4500, 30000)            # Time to wait ( clock variable ) is being generated in range of numbers ( 4.5 seconds and 30 seconds )     ( in ms )


# GET COORDINATES:
# Display Resolution ( Gets Resolution of your Monitor / Display  Automaticly )
DISPLAY_X = GetSystemMetrics(0)
DISPLAY_Y = GetSystemMetrics(1)
#MOUSE_POS = pyautogui.position()

# Loop Variable
run = True

# Cat's Variables 
velocity = 1

# SCREEN.position = (x_pos, y_pos)


CAT = pygame.image.load(os.path.join("graphics", "orange_cat_idle(128x128).png"))

transparency_color = (255, 0, 128)
dark_red = (139, 0, 0)

####################################################################

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency_color), 0, win32con.LWA_COLORKEY)


clock = pygame.time.Clock()


## VARIABLES ##
X_COORDINATES = 0
Y_COORDINATES = 0
action = random.randint(1, 100)     # Random Number ( see this as percentage % ), needed for giving an action to the cat :)


## MAIN LOOP ##
while run:
    



    MOUSE_POS = pyautogui.position()

    for event in pygame.event.get():                                                # For every Event in Pygame: 
        if event.type == pygame.QUIT:                                               # If event QUIT was used(if button quit was pressed):
            run = False

    window = pyautogui.getWindowsWithTitle("Cat")[0]
    rect = window._rect
    

    if action in range(1, 70):       
        if not abs(rect.x - X_COORDINATES) < velocity or not abs(X_COORDINATES - rect.x) < velocity:        # If rect.x coordinates - X_Coordinates is not smaller than velocity it self ( it means if it is bigger than velocity ):
            if rect.x >= X_COORDINATES: 
                rect.x -= velocity 
            elif rect.x <= X_COORDINATES:
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

    if action in range(71, 100):

        if rect.x != MOUSE_X:
            if rect.x >= MOUSE_X:
                rect.x -= velocity
            elif rect.x <= MOUSE_X:
                rect.x += velocity
        if rect.y != MOUSE_Y:
            if rect.y >= MOUSE_Y:
                rect.y -= velocity
            elif rect.y <= MOUSE_Y:
                rect.y += velocity
        if rect.x == MOUSE_X and rect.y == MOUSE_Y:
            action = random.randint(1, 100)

        print(MOUSE_X, MOUSE_Y)



    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)    
    # win32gui.MoveWindow(hwnd, 0, 0, 128, 128, True)

    SCREEN.fill(transparency_color)

    SCREEN.blit(CAT, (0, 0))


    clock.tick(60)
    pygame.display.update()
    
    
