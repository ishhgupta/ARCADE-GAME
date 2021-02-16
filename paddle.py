from numpy.lib.function_base import select
# from myGame.headerfile import PADDLE_ROW
from headerfile import *
from headerfile import PADDLE_LENGTH
import numpy as np

class Paddle:
    def __init__(self,r,c):
        self.__paddle = np.tile(Back.WHITE + ' ', PADDLE_LENGTH)
        self.__rownum = r
        self.__colnum = c
    
    def placePaddle(self,grid):
        grid[self.__rownum,self.__colnum:self.__colnum + PADDLE_LENGTH] = self.__paddle

    def movePaddle(self,dirn,grid):
        grid[PADDLE_ROW, self.__colnum + dirn:self.__colnum+dirn+PADDLE_LENGTH] = self.__paddle
        self.__colnum = self.__colnum + dirn