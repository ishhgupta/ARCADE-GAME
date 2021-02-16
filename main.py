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
from input import *

obj_Screen = Screen()
grid = obj_Screen.give_grid()
generateBrick(grid)
obj_Paddle = Paddle(PADDLE_ROW,0)
obj_Paddle.placePaddle(grid)

# obj_Screen.create_bg(grid)
# while True:
# cnt = 0
os.system('clear')
while True:
   
    # os.system('clear')
    print("\033[0;0H")
    # clear()
    obj_Screen.create_bg(grid)
    letter = input_to(Get())
    if letter == "q":
        print("Quit!!")
        break
    elif letter == "a" or letter == "A":
        obj_Paddle.movePaddle(-1,grid)
    elif letter == "d" or letter == "D":
        obj_Paddle.movePaddle(1,grid)
    # print(letter)
    # cnt+=1
    # sleep(10)
# obj_Screen.create_bg(grid)
# letter = input_to(Get())
# if letter == "a" or letter == "A":
#     obj_Paddle.movePaddle(-1,grid)
