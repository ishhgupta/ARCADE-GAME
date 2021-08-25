# from _typeshed import WriteableBuffer
from headerfile import *
import headerfile
import random
from paddle import *
from bricks import *
from powerup import *

import os

bombs = []

class Boss:
    def __init__(self):
        a = np.zeros((5, 20), dtype='<U20')
        a[:] = ' '
        y = 0
        with open("UFO.txt") as obj:
            for line in obj:
                x = 0
                for char in line:
                    if char == '\n':
                        break
                    else:
                        a[y][x] = char+Fore.RESET
                    x += 1
                y += 1
        self._body = a
        self._rowRange = 5
        self._colRange = 20
        self._rownum = 1
        self._colnum = 0
    
    def placeBoss(self,grid):
        grid[self._rownum:self._rownum+self._rowRange,
             self._colnum:self._colnum+self._colRange] = self._body
    
    def moveBoss(self,grid,obj_Paddle):
        grid[self._rownum:self._rownum+self._rowRange,
            self._colnum:self._colnum+self._colRange][:] = Back.RESET + ' '
        
        self._colnum = obj_Paddle.getColnum()
        if self._colnum >= WIDTH - self._colRange - 1:
            self._colnum = WIDTH - self._colRange - 1
        grid[self._rownum:self._rownum+self._rowRange,
             self._colnum:self._colnum+self._colRange] = self._body
    
    def addBomb(self):
        obj_bomb = Bomb(self._colnum, self._rowRange)
        bombs.append(obj_bomb)

class Bomb:
    def __init__(self, x, y):
       self.__rownum = y
       self.__colnum = x
       self.__shape = Back.RED + '='
       self.__caught = False
    
    def placeBomb(self,grid,obj_Paddle):
        grid[self.__rownum, self.__colnum]  = Back.RESET + ' '
        temp_row = self.__rownum + 2

        
        if temp_row > HEIGHT -3:
            # print("hit wall")
            return 0

        ''' check if caught by paddle'''
        stInd = obj_Paddle.getColnum()
        endInd = stInd + PADDLE_LENGTH -1
        if temp_row >= PADDLE_ROW and self.__colnum >= stInd and self._colnum <= endInd:
            # print("hit paddle")
            self.__caught = True
            # self.time = time.time()
            return 2

        self.__rownum = temp_row
        grid[self.__rownum, self.__colnum] = self.__shape
        return 1

def placeBombs(grid,obj_Paddle):
    for bomb in bombs:
        res = bomb.placeBomb(grid,obj_Paddle)
        if res==0:
            bombs.remove(bomb)
        if res == 2:
            return 1
        else: 
            return 0


# addBomb()


