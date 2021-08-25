# from myGame.headerfile import BRICK_LENGTH
from headerfile import *
from screen import Screen
from headerfile import END_C, START_C, START_R, BRICK_LENGTH
# from main import NUM_BRICKS
import headerfile

from colorama import init,Fore,Back,Style
init(autoreset=True)

import numpy as np
import random 

class Brick:
    def __init__(self,strength):
        self._length = BRICK_LENGTH
        self._strength = strength
        self._rownum = 0
        self._colnum = 0
        self._brick = ' '
        self._ifRainbow = False
    
    def fallBrick(self):
        # grid[self._rownum, self._colnum : self._colnum + BRICK_LENGTH] = np.tile(Back.RESET + ' ',BRICK_LENGTH)
        self._rownum += 1

    def erase(self,grid):
        grid[self._rownum, self._colnum : self._colnum + BRICK_LENGTH] = np.tile(Back.RESET + ' ',BRICK_LENGTH)
    
    def placeBrick(self,grid):
        
        ''' handling rainbow brick'''
        if self._ifRainbow == True:
            temp = random.randint(1,4)
            if temp == 3:
                self._brick = np.tile(Back.BLUE + ' ',BRICK_LENGTH)
            elif temp == 2:
                self._brick = np.tile(Back.YELLOW + ' ',BRICK_LENGTH)   
            elif temp == 1:
                self._brick = np.tile(Back.WHITE + ' ',BRICK_LENGTH)
            else:
                self._brick = np.tile(Back.RED + ' ',BRICK_LENGTH)
            self._strength = temp

        grid[self._rownum, self._colnum : self._colnum + BRICK_LENGTH] = self._brick
    
    def clear(self,grid):
        grid[self._rownum, self._colnum : self._colnum + BRICK_LENGTH] = np.tile(Back.RESET + ' ',BRICK_LENGTH)
    
    def checkBrick(self):
        # to check if brick is in the same row as paddle after continuosly falling
        if self._rownum >= PADDLE_ROW -1:
            return 0

    def getRownum(self):
        return self._rownum
    def getColnum(self):
        return self._colnum
    def getStrength (self):
        return self._strength
    
    def setIfRainbow(self,flag):
        self._ifRainbow = flag

    def destroy(self):
        self._brick = np.tile(Back.RESET + ' ',BRICK_LENGTH)
        self._strength = 0

    def changeColor(self):
        if self._ifRainbow == True:
            self._ifRainbow = False
        # print("change color")
        if self._strength == 3:
            self._brick = np.tile(Back.YELLOW + ' ',BRICK_LENGTH)
            self._strength -= 1
        elif self._strength == 2:
            self._brick = np.tile(Back.WHITE + ' ',BRICK_LENGTH)
            self._strength -= 1
        elif self._strength == 1:
            # print("strength is 1")
            self._brick = np.tile(Back.RESET + ' ',BRICK_LENGTH)
            self._strength -= 1
            headerfile.NUM_BRICKS -= 1
    
    def reset(self):
        self._brick = np.tile(Back.RESET + ' ',BRICK_LENGTH)
        self._strength = 0
    

class unbreakable(Brick):
    def __init__(self, strength,r,c):
        super().__init__(strength)
        self._rownum = r
        self._colnum = c
        self._brick = np.tile(Back.RED + ' ',BRICK_LENGTH)
    
class pow3(Brick):
    def __init__(self, strength,r,c):
        super().__init__(strength)
        self._rownum = r
        self._colnum = c
        self._brick = np.tile(Back.BLUE + ' ',BRICK_LENGTH)
  
class pow2(Brick):
    def __init__(self, strength,r,c):
        super().__init__(strength)
        self._rownum = r
        self._colnum = c
        self._brick = np.tile(Back.YELLOW + ' ',BRICK_LENGTH)
    

class pow1(Brick):
    def __init__(self, strength,r,c):
        super().__init__(strength)
        self._rownum = r
        self._colnum = c
        self._brick = np.tile(Back.WHITE + ' ',BRICK_LENGTH)

class special(Brick):
    def __init__(self, strength,r,c):
        super().__init__(strength)
        self._rownum = r
        self._colnum = c
        self._brick = np.tile(Back.GREEN + ' ',BRICK_LENGTH)

# brickStructure = []  

def generateBrick(grid):    
    # brickStructure = []  
    bricks = 0
    for i in range (15):
        for j in range(START_C, END_C, BRICK_LENGTH):
            strength = random.randint(1,4)
            if strength == 3:
                obj_Brick = pow3(strength, START_R+i,j)
            elif strength == 2:
                obj_Brick = pow2(strength , START_R+i,j)
            elif strength == 1:
                obj_Brick = pow1(strength , START_R+i,j)
            else:
                obj_Brick = unbreakable(strength , START_R+i,j)

            ''' for rainbow brick'''
            if i == 14 and j == START_C + BRICK_LENGTH*7:
                # obj_Brick = pow3(strength , START_R+i,j)
                obj_Brick._ifRainbow = True

            headerfile.brickStructure.append(obj_Brick)
            bricks= bricks + 1
    
    ''' special type of bricks for bonus'''
    for j in range(START_C, START_C + BRICK_LENGTH*6, BRICK_LENGTH):
        obj_Brick = special(-1,START_R + 15,j)
        headerfile.brickStructure.append(obj_Brick)
        bricks +=  1
    return bricks

def explosion():
    global NUM_BRICKS
    for brick in headerfile.brickStructure:
        if brick.getRownum()==START_R+14 and brick.getColnum()<START_C + BRICK_LENGTH*7:
            brick.reset()
            headerfile.NUM_BRICKS -= 1
            # print("in explosion", NUM_BRICKS)
        if brick.getRownum()==START_R+15 and brick.getColnum()<=START_C + BRICK_LENGTH*6:
            brick.reset()
            headerfile.NUM_BRICKS -= 1

def printBricks(grid):
    for brick in headerfile.brickStructure:
        brick.placeBrick(grid)

def fallBricks(grid):
    num = 1
    for brick in headerfile.brickStructure:
        if num < 13:
            brick.erase(grid)
        num += 1
        brick.fallBrick()

def resetBricks(grid):
    print("in reset")
    for brick in headerfile.brickStructure:
        brick.clear(grid)

def checkBricksPaddle(grid):
    for brick in headerfile.brickStructure:
        if brick.checkBrick() == 0:
            return 0
    return 1
