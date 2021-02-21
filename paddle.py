from numpy.lib.function_base import select
# from myGame.headerfile import PADDLE_ROW
from headerfile import *
from headerfile import PADDLE_LENGTH, PADDLE_ROW, WIDTH
import numpy as np

class Paddle:
    def __init__(self):
        self.__length = PADDLE_LENGTH
        self.__paddle = np.tile(Back.LIGHTCYAN_EX + ' ', self.__length)
        self.__rownum = PADDLE_ROW
        self.__colnum = 0
        self.__speed = 5
    
    def clear(self,grid):
        grid[self.__rownum,self.__colnum+PADDLE_LENGTH:self.__colnum+2*PADDLE_LENGTH] = ' '

    def placePaddle(self,grid):
        grid[self.__rownum,self.__colnum:self.__colnum + self.__length] = self.__paddle

    def movePaddleLeft(self,grid):
        grid[PADDLE_ROW,self.__colnum:self.__colnum + self.__length] = ' '
        if self.__colnum - self.__speed < 0:
            self.__colnum = 0
        else :
            self.__colnum -= self.__speed
        grid[PADDLE_ROW, self.__colnum:self.__colnum+self.__length] = self.__paddle

    def movePaddleRight(self,grid):
        grid[PADDLE_ROW,self.__colnum:self.__colnum + self.__length] = ' '
        if self.__colnum + self.__speed + self.__length > WIDTH -1 :
            self.__colnum = WIDTH - self.__length -1
            # print(self.__colnum)
        else :
            self.__colnum += self.__speed
        grid[PADDLE_ROW, self.__colnum:self.__colnum+self.__length] = self.__paddle
    
    def getColnum(self):
        return self.__colnum

    def changeLength(self,newLen):
        self.__length = newLen
        self.__paddle = np.tile(Back.LIGHTCYAN_EX + ' ', self.__length)


