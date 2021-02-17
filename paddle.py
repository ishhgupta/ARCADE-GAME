from numpy.lib.function_base import select
# from myGame.headerfile import PADDLE_ROW
from headerfile import *
from headerfile import PADDLE_LENGTH, PADDLE_ROW, WIDTH
import numpy as np

class Paddle:
    def __init__(self):
        self.__paddle = np.tile(Back.LIGHTCYAN_EX + ' ', PADDLE_LENGTH)
        self.__rownum = PADDLE_ROW
        self.__colnum = 0
        self.__speed = 5
    
    def placePaddle(self,grid):
        grid[self.__rownum,self.__colnum:self.__colnum + PADDLE_LENGTH] = self.__paddle

    def movePaddleLeft(self,grid):
        grid[PADDLE_ROW,self.__colnum:self.__colnum + PADDLE_LENGTH] = ' '
        if self.__colnum - self.__speed < 0:
            self.__colnum = 0
        else :
            self.__colnum -= self.__speed
        grid[PADDLE_ROW, self.__colnum:self.__colnum+PADDLE_LENGTH] = self.__paddle

    def movePaddleRight(self,grid):
        grid[PADDLE_ROW,self.__colnum:self.__colnum + PADDLE_LENGTH] = ' '
        if self.__colnum + self.__speed + PADDLE_LENGTH > WIDTH -1 :
            self.__colnum = WIDTH - PADDLE_LENGTH -1
            # print(self.__colnum)
        else :
            self.__colnum += self.__speed
        grid[PADDLE_ROW, self.__colnum:self.__colnum+PADDLE_LENGTH] = self.__paddle


    def getColnum(self):
        return self.__colnum