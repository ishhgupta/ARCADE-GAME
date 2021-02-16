from headerfile import *
from paddle import *

class Ball:
    # def __init__(self,r,c):
    def __init__(self):
        self.__rownum = PADDLE_ROW - 1
        self.__colnum = (int)((Paddle().getColnum() + PADDLE_LENGTH)/2)
        self.__ball = Fore.RED + 'O'
        self.__xspeed = 1
        self.__yspeed = 1
    
    def placeBall(self,grid):
        grid[self.__rownum,self.__colnum] = self.__ball

    # def moveBall(self,grid):
    #     grid[self.__rownum,self.__colnum] = ' '
    #     self.__rownum += self.__yspeed
    #     self.__colnum += self.__xspeed
    #     grid[self.__rownum,self.__colnum] = self.__ball
        
