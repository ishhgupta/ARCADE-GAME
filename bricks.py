# from myGame.headerfile import BRICK_LENGTH
from headerfile import *
from screen import Screen
from headerfile import END_C, START_C, START_R, BRICK_LENGTH

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
    
    def placeBrick(self,grid):
        grid[self._rownum, self._colnum : self._colnum + BRICK_LENGTH] = self._brick
    
    def getRownum(self):
        return self._rownum
    def getColnum(self):
        return self._colnum
    def getStrength (self):
        return self._strength
        
    def destroy(self):
        self._brick = np.tile(Back.RESET + ' ',BRICK_LENGTH)
        self._strength = 0

    def changeColor(self):
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

brickStructure = []  

def generateBrick(grid):
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
            brickStructure.append(obj_Brick)
    
    ''' special type of bricks for bonus'''
    for j in range(START_C, START_C + BRICK_LENGTH*6, BRICK_LENGTH):
        obj_Brick = special(-1,START_R + 15,j)
        brickStructure.append(obj_Brick)

def explosion():
    for brick in brickStructure:
        if brick.getRownum()==START_R+14 and brick.getColnum()<START_C + BRICK_LENGTH*7:
            brick.reset()
        if brick.getRownum()==START_R+15 and brick.getColnum()<=START_C + BRICK_LENGTH*6:
            brick.reset()

def printBricks(grid):
    for brick in brickStructure:
        brick.placeBrick(grid)


