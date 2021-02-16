# from myGame.headerfile import PADDLE_ROW
# from myGame.input import input_to
import os
import time
import signal
import random
from time import sleep


from headerfile import *
from screen import Screen
from bricks import *
from paddle import *
from ball import *
from input import *


obj_Screen = Screen()
grid = obj_Screen.give_grid()

generateBrick(grid)

obj_Paddle = Paddle()
obj_Paddle.placePaddle(grid)

obj_Ball = Ball()
obj_Ball.placeBall(grid)


var = Get()
os.system('clear')
while True:
    # print("\033[0;0H")
    # print('\033c')
    # letter = input_to(Get())
    letter = input_to(var)
    if letter == "q":
        print("Quit!!")
        break
    elif letter == "a" or letter == "A":
        obj_Paddle.movePaddleLeft(grid)
    elif letter == "d" or letter == "D":
        obj_Paddle.movePaddleRight(grid)
    print("\033[%d;%dH" % (0, 0))
    obj_Screen.create_bg(grid)
   
