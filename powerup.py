import os
import time
import signal
import random

from headerfile import *
from screen import Screen
from bricks import *
from paddle import *
from ball import *

class Powerup():
    types = ['@','#','$','%','*','&']
    def __init__(self,type,x,y) :
        self._type = type
        self._colnum = x
        self._rownum = y
        self._caught = False
    
    def place(self,grid,struct):
        grid[self._rownum,self._colnum] = ' '
        # grid[self._rownum,self._colnum] = Back.GREEN + self.types[self._type]
        self._rownum += 1
        grid[self._rownum,self._colnum] = struct
    
    def detect(self,grid,obj_Paddle,struct):
        print("move")
        grid[self._rownum,self._colnum] = ' '
        temp_row = self._rownum + 1
        if temp_row > HEIGHT -3:
            # grid[self._rownum,self._colnum] = ' '
            print("hit wall")
            return False
        stInd = obj_Paddle.getColnum()
        endInd = stInd + PADDLE_LENGTH -1
        if temp_row == PADDLE_ROW and self._colnum >= stInd and self._colnum <= endInd:
            print("hit paddle")
            self._caught = True
            return True
        self._rownum = temp_row
        grid[self._rownum,self._colnum] = struct
        return 1



class expandPaddle(Powerup):
    def __init__(self,type,x,y) :
        super().__init__(type, x, y)
        self._struct = Fore.GREEN + '@'

class shrinkPaddle(Powerup):
    def __init__(self,type,x,y) :
        super().__init__(type, x, y)
        self._struct = Fore.GREEN + '#'

class paddleGrab(Powerup):
    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        self._struct = Fore.GREEN + '$'

class fastBall(Powerup):
    def __init__(self,type,x,y) :
        super().__init__(type, x, y)
        self._struct = Fore.GREEN + '%'

class multipleBall(Powerup):
    def __init__(self,type,x,y) :
        super().__init__(type, x, y)
        self._struct = Fore.GREEN + '*'

class thruBall(Powerup):
    def __init__(self,type,x,y) :
        super().__init__(type, x, y)
        self._struct = Fore.GREEN + '&'

activePowerups = []

def addPowerups(y,x):
    # print("in add powerup")
    type = random.randint(1,6)
    if type == 1:
        obj_powerup = expandPaddle(type,x,y)
    elif type == 2:
        obj_powerup = shrinkPaddle(type,x,y)
    elif type == 3:
        obj_powerup = paddleGrab(type,x,y)
    elif type == 4:
        obj_powerup = fastBall(type,x,y)
    elif type == 5:
        obj_powerup = multipleBall(type,x,y)
    else:
        obj_powerup = thruBall(type,x,y)
    activePowerups.append(obj_powerup)

# print(activePowerups.)

def placePowerups(grid):
    for powerup in activePowerups:
        # print(powerup._struct)
        powerup.place(grid,powerup._struct)

def detectPowerups(grid,obj_Paddle):
    for powerup in activePowerups:
        val =  powerup.detect(grid,obj_Paddle,powerup._struct)
        if val == False:
            activePowerups.remove(powerup)
        if val == True:
            activePowerups.remove(powerup)

