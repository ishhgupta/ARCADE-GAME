from headerfile import *
from paddle import *

class Ball:
    # def __init__(self,r,c):
    def __init__(self):
        self.__rownum = PADDLE_ROW - 1
        self.__colnum = (int)((Paddle().getColnum() + PADDLE_LENGTH)/2)
        self.__ball = Fore.WHITE + Back.RESET + '0'
        self.__xspeed = 1
        self.__yspeed = -1
        self.__lives = 3
        self.__stuck = True
    
    def stickBall(self,grid,obj_Paddle):
        grid[self.__rownum,self.__colnum] = ' '
        self.__colnum = (int)(obj_Paddle.getColnum() + PADDLE_LENGTH/2)
        grid[self.__rownum,self.__colnum] = self.__ball

    # def ballWallcollision(self,grid,temp_row,temp_col):
    #     if self.__colnum < 0 or  self.__colnum > WIDTH - 1:
    #         self.__xspeed = -1*(self.__xspeed)

    # outside this class
    def ifStuck(self):
        return self.__stuck
    def release(self,val):
        self.__stuck = val

    def moveBall(self,grid,obj_Paddle):
        grid[self.__rownum,self.__colnum] = ' '
        temp_row = self.__rownum + self.__yspeed
        temp_col = self.__colnum + self.__xspeed
        
        ''' handling collision with wall'''
        if temp_col < 0 or temp_col > WIDTH -1:
            self.__xspeed = -1*(self.__xspeed)
        if temp_row < 0 or temp_row > HEIGHT -1:        # subject to change
            self.__yspeed = -1*(self.__yspeed)

        ''' handle collision with paddle'''
        # obj_Paddle.ballPaddleCollision(temp_col,temp_row,obj_Ball)
        stInd = obj_Paddle.getColnum()
        endInd = stInd + PADDLE_LENGTH -1
        midInd = (int)((stInd + endInd)/2)
        if temp_row == PADDLE_ROW and temp_col >= stInd and temp_col <= endInd:
            self.__xspeed += (temp_col-midInd)
            self.__yspeed = -1*(self.__yspeed)

        self.__rownum += self.__yspeed
        self.__colnum += self.__xspeed
        grid[self.__rownum,self.__colnum] = self.__ball
    
        
