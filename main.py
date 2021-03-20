import os
import time
import signal
import random

from headerfile import *
import headerfile
# from headerfile import NUM_BRICKS
from screen import Screen
from bricks import *
from paddle import *
from ball import *
from input import *
from powerup import *

# os.system("aplay -q sounds/DXBALL.wav &")
obj_Screen = Screen()
grid = obj_Screen.give_grid()

headerfile.NUM_BRICKS = generateBrick(grid)

levelNum = 1
fallingLimit = 10

obj_Paddle = Paddle()
obj_Paddle.placePaddle(grid)

obj_Ball = Ball()
obj_Ball.stickBall(grid,obj_Paddle)

os.system('clear')
starttime = time.time()
levelTime = time.time()
# prevTime = levelTime

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
    
    letter = input_to(inpChar)
    printBricks(grid)
    limitTime = round(time.time()) - round(levelTime)
    if limitTime > fallingLimit:
        obj_Ball.setFallBrick(True)

    if letter == "n" or headerfile.NUM_BRICKS == '0':
        levelNum += 1
        levelTime = time.time()

        headerfile.brickStructure = []
        headerfile.NUM_BRICKS = 0
        headerfile.NUM_BRICKS = generateBrick(grid)
        obj_Ball.setFallBrick(False)
        obj_Paddle.initialPos(0,grid)
        obj_Paddle.placePaddle(grid)
        obj_Ball.stickBall(grid,obj_Paddle)
        
    if levelNum == 4:
        os.system("killall aplay -q")
        inpChar.show_cursor()
        os.system('stty echo')
        os.system('clear')
        print("Game Over!!")
        os.system("aplay sounds/gameover.wav -q &")
        break

    if letter == "q":
        os.system("killall aplay -q")
        inpChar.show_cursor()
        os.system('stty echo')
        print("Quit!!")
        os.system("aplay sounds/gameover.wav -q &")
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
    placePowerups(grid,obj_Paddle,obj_Ball)
    # print("\033[%d;%dH" % (0, 0))

    # checkBricksPaddle(grid)

    print("\033[0;0H")
    print()
    print(Fore.WHITE + Back.MAGENTA + "SCORE: " + (str)(obj_Ball.getScore()), end = "\t\t\t")
    print(Fore.WHITE + Back.MAGENTA + "LevelTime: " + (str)(round(time.time()) - round(levelTime)), end = "\t\t\t")
    print(Fore.WHITE + Back.MAGENTA + "TIME: " + (str)(round(time.time()) - round(starttime)),end = "\t\t\t")
    print(Fore.WHITE + Back.MAGENTA + "LIVES: " +(str)(obj_Ball.getLives()), end = "\t\t\t" )
    print(Fore.WHITE + Back.MAGENTA + "LEVEL: " +(str)(levelNum))
    print()
    live = obj_Ball.getLives()

    if live == '0':
        # print("yeahyeah")
        os.system("killall aplay -q")
        inpChar.show_cursor()
        os.system('stty echo')
        os.system('clear')
        print("Lives Over!!")
        os.system("aplay sounds/gameover.wav -q &")
        break
    
    obj_Screen.create_bg(grid)
    # print("NUM_BRICKS", headerfile.NUM_BRICKS)
    # time.sleep(0.03)
inpChar.show_cursor()

# for brick in brickComplex:
#     print(brick.getRownum(), end=' ')
#     print(brick.getColnum())

   
