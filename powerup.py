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
    def __init__(self,type,x,y, xspeed, yspeed) :
        self._type = type
        self._colnum = x
        self._rownum = y
        self._xspeed = xspeed
        self._yspeed = yspeed
        self._caught = False
        self._time = None
        self._proj = 0

    def checkRemTime(self):
        if time.time() - self.time > 6.0:
            return 0
        return 1
    
    def place(self,grid,obj_Paddle,struct):
        grid[self._rownum,self._colnum] = ' '
        temp_row = self._rownum +self._yspeed
        temp_row += self._proj                        # gravity effect
        # grid[self._rownum,self._colnum] = Back.GREEN + self.types[self._type]
        if temp_row > HEIGHT -3:
            # print("hit wall")
            return 0
        stInd = obj_Paddle.getColnum()
        endInd = stInd + PADDLE_LENGTH -1
        if temp_row >= PADDLE_ROW and self._colnum >= stInd and self._colnum <= endInd:
            # print("hit paddle")
            self._caught = True
            self.time = time.time()
            return 2

        ''' powerup collision with wall'''
        temp_col = self._colnum + self._xspeed
        if temp_col < 0 or temp_col > WIDTH -1:
            # os.system("aplay sounds/hitWall.wav -q &")
            self._xspeed = -1*(self._xspeed)
        if temp_row < 0 :
            # os.system("aplay sounds/hitWall.wav -q &")
            self._yspeed = -1*(self._yspeed)
        
        self._rownum = temp_row     
        self._colnum = temp_col
        grid[self._rownum,self._colnum] = struct
        self._proj = 2
        return 1
    def activate(self):
        print("in parent class")
    def deactivate(self):
        print("in parent class")

class expandPaddle(Powerup):
    def __init__(self,type,x,y,xspeed, yspeed) :
        super().__init__(type, x, y, xspeed, yspeed)
        self._struct = Fore.GREEN + '@'
    def activate(self,obj_Paddle):
        obj_Paddle.changeLength(2*PADDLE_LENGTH)
    def deactivate(self,obj_Paddle,grid):
        obj_Paddle.clear(grid)
        obj_Paddle.changeLength(PADDLE_LENGTH)

class shrinkPaddle(Powerup):
    def __init__(self,type,x,y,xspeed, yspeed) :
        super().__init__(type, x, y,xspeed, yspeed)
        self._struct = Fore.GREEN + '#'
    def activate(self,obj_Paddle):
        obj_Paddle.changeLength(PADDLE_LENGTH-2)
    def deactivate(self,obj_Paddle):
        obj_Paddle.changeLength(PADDLE_LENGTH)

class paddleGrab(Powerup):
    def __init__(self, type, x, y,xspeed, yspeed):
        super().__init__(type, x, y,xspeed, yspeed)
        self._struct = Fore.GREEN + '$'
    def activate(self):
        print("in grab paddle  class")
    def deactivate(self):
        print("in grab paddle  class")

class fastBall(Powerup):
    def __init__(self,type,x,y,xspeed, yspeed) :
        super().__init__(type, x, y,xspeed, yspeed)
        self._struct = Fore.GREEN + '%'
    def activate(self,obj_Ball):
        obj_Ball.setSpeed(2*obj_Ball.getXspeed(),2*obj_Ball.getYspeed())
        # print("in fast paddle  class")
    def deactivate(self,obj_Ball):
        obj_Ball.setSpeed(1,-1)
        print("in fast paddle  class")

class multipleBall(Powerup):
    def __init__(self,type,x,y,xspeed, yspeed) :
        super().__init__(type, x, y,xspeed, yspeed)
        self._struct = Fore.GREEN + '*'
    def activate(self):
        print("in multiple  paddle  class")
    def deactivate(self):
        print("in multiple paddle  class")

class thruBall(Powerup):
    def __init__(self,type,x,y,xspeed, yspeed) :
        super().__init__(type, x, y,xspeed, yspeed)
        self._struct = Fore.GREEN + '&'
    def activate(self,obj_Ball):
        obj_Ball.setThru(True)
        
    def deactivate(self,obj_Ball):
        obj_Ball.setThru(False)
       

activePowerups = []
caughtPowerups = []

def addPowerups(y,x,xspeed, yspeed):
    if yspeed > 0 :
        yspeed -= 2
    # os.system("aplay sounds/powerup.wav -q &")
    type = random.randint(1,2)
    if type == 1:
        obj_powerup = expandPaddle(type,x,y, xspeed, yspeed)
    elif type == 2:
        obj_powerup = shrinkPaddle(type,x,y,xspeed, yspeed)
    elif type == 3:
        obj_powerup = paddleGrab(type,x,y,xspeed, yspeed)
    elif type == 4:
        obj_powerup = fastBall(type,x,y,xspeed, yspeed)
    elif type == 5:
        obj_powerup = multipleBall(type,x,y,xspeed, yspeed)
    else:
        obj_powerup = thruBall(type,x,y,xspeed, yspeed)
    activePowerups.append(obj_powerup)

def placePowerups(grid,obj_Paddle,obj_Ball):
    for powerup in activePowerups:
        val = powerup.place(grid,obj_Paddle,powerup._struct)
        
        if val == 0:
            activePowerups.remove(powerup)
        if val == 2:
            if powerup._type == 1 or powerup._type == 2:
                powerup.activate(obj_Paddle)
            elif powerup._type == 6 or powerup._type == 4:
                powerup.activate(obj_Ball)
            else:
                powerup.activate()
            activePowerups.remove(powerup)
            caughtPowerups.append(powerup)
    
    for powerup in caughtPowerups:
        res = powerup.checkRemTime()
        if res == 0:
            if powerup._type == 1: 
                powerup.deactivate(obj_Paddle,grid)
            elif powerup._type == 2:
                powerup.deactivate(obj_Paddle)
            elif powerup._type == 6 or powerup._type == 4:
                powerup.deactivate(obj_Ball)
            else:
                powerup.deactivate()
            caughtPowerups.remove(powerup)


