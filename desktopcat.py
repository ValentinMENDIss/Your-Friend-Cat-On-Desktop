import pygame
import os
import win32gui, win32api, win32con
import random

pygame.init()  

#SCREEN_WIDTH =  128      
#SCREEN_HEIGHT = 128  
SCREEN = pygame.display.set_mode((128, 128), pygame.NOFRAME) 


run = True
x_pos = 0 
y_pos = 0
random_pos = random.randint(0, 500)



#SCREEN.position = (x_pos, y_pos)

CAT = pygame.image.load(os.path.join("graphics", "orange_cat_idle(128x128).png"))

transparency_color = (255, 0, 128)
dark_red = (139, 0, 0)

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency_color), 0, win32con.LWA_COLORKEY)

clock = pygame.time.Clock()
    

while run:
    
    for event in pygame.event.get():                                                # For every Event in Pygame: 
        if event.type == pygame.QUIT:                                               # If event QUIT was used(if button quit was pressed):
            run = False
     
    WINDOW_X_POSITION = 0
    WINDOW_Y_POSITION = 0

    WINDOW_2_X_POSITION = 0
    WINDOW_2_Y_POSITION = 0

    if WINDOW_X_POSITION == WINDOW_2_X_POSITION:
        WINDOW_X_POSITION = random.randint(0, 1800)
        WINDOW_Y_POSITION = random.randint(0, 1000)

        WINDOW_2_X_POSITION = random.randint(0, 1800)
        WINDOW_2_Y_POSITION = random.randint(0, 1000)

    elif WINDOW_X_POSITION != WINDOW_2_X_POSITION:
        WINDOW_X_POSITION -= WINDOW_2_X_POSITION
        



    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)    
    win32gui.MoveWindow(hwnd, WINDOW_X_POSITION, WINDOW_Y_POSITION, 128, 128, True)

    SCREEN.fill(transparency_color)
    
    
    
    SCREEN.blit(CAT, (0, 0))
    

    clock.tick(60)
    pygame.display.update()
    
    
