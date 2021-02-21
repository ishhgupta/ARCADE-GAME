import os
import time
import signal
import random

from headerfile import *
from screen import Screen
from bricks import *
from paddle import *
from ball import *
from input import *
from powerup import *


obj_Screen = Screen()
grid = obj_Screen.give_grid()

generateBrick(grid)

obj_Paddle = Paddle()
obj_Paddle.placePaddle(grid)

obj_Ball = Ball()
obj_Ball.stickBall(grid,obj_Paddle)

os.system('clear')

print()
for i in range(3):
    for j in range(WIDTH):
        print(Back.MAGENTA + ' ', end='')
    print()
print(Back.RESET)

inpChar = Get()
inpChar.hide_cursor()
os.system('stty -echo')
    
while True:
    # print('\033c')
    # letter = input_to(Get())
    printBricks(grid)
    letter = input_to(inpChar)
    if letter == "q":
        inpChar.show_cursor()
        os.system('stty echo')
        print("Quit!!")
        break
    elif letter == "a" or letter == "A":
        obj_Paddle.movePaddleLeft(grid)
    elif letter == "d" or letter == "D":
        obj_Paddle.movePaddleRight(grid)
    elif letter == "u"  or letter == "U":
        obj_Ball.release(False)
    if(obj_Ball.ifStuck() == False):
        obj_Ball.moveBall(grid,obj_Paddle)
    else:
        obj_Ball.stickBall(grid,obj_Paddle)
    placePowerups(grid)
    detectPowerups(grid,obj_Paddle)
    # print("\033[%d;%dH" % (0, 0))
    print("\033[0;0H")
    print()
    print(Fore.WHITE + Back.MAGENTA + "SCORE:" , end = "\t\t\t\t")
    print(Fore.WHITE + Back.MAGENTA + "TIME:",end = "\t\t\t\t")
    print(Fore.WHITE + Back.MAGENTA + "LIVES:")
    print()
    obj_Screen.create_bg(grid)
    time.sleep(0.03)
inpChar.show_cursor()

# for brick in brickComplex:
#     print(brick.getRownum(), end=' ')
#     print(brick.getColnum())

   
