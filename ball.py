import random
from headerfile import *
from paddle import *
from bricks import *
from powerup import *

class Ball:
    def __init__(self):
        self.__rownum = PADDLE_ROW - 1
        self.__colnum = 0
        self.__ball = Fore.YELLOW + Back.RESET + 'O'
        self.__xspeed = 1
        self.__yspeed = -1
        self.__lives = 3
        self.__stuck = True
        self.__initial = random.randint(0,PADDLE_LENGTH-1)          ## gives random value for determining inital pos on paddle
    
    def stickBall(self,grid,obj_Paddle):
        
        grid[self.__rownum,self.__colnum] = ' '
        # self.__colnum = random.randint(obj_Paddle.getColnum(),obj_Paddle.getColnum() + PADDLE_LENGTH - 1)
        self.__colnum = obj_Paddle.getColnum() +self.__initial
        grid[self.__rownum,self.__colnum] = self.__ball

    def ifStuck(self):
        return self.__stuck
    def release(self,val):
        self.__stuck = val

    def checkCollision(self,ball_y,ball_x,brick):
        flag = False
        bsy = brick.getRownum()
        bsx1 = brick.getColnum()
        bsx2 = bsx1 + BRICK_LENGTH -1
        ''' brick collision up and below'''
        minVal = min(self.__colnum, ball_x)
        maxVal = max(self.__colnum, ball_x)
        if maxVal == ball_x:
            maxVal = maxVal +1
        else :
            minVal = minVal -1

        # if minVal == maxVal:
        #     bx = minVal
        #     if ball_y == bsy and bx>=bsx1 and bx <= bsx2:
        #         flag = True
        for bx in range(minVal,maxVal):
            if ball_y == bsy and bx>=bsx1 and bx <= bsx2:
                flag = True
        return flag


    def ballBrickCollision(self,temp_row,temp_col):
        for brick in brickStructure:
            if brick.getStrength() == 0:
                continue
            
            if self.checkCollision(temp_row,temp_col,brick):
                if brick.getStrength()==-1:
                    explosion()
                brick.changeColor()
                # if brick.getStrength() == 0 or brick.getStrength()==1:
                if brick.getStrength() == 0 :
                    addPowerups(self.__rownum,self.__colnum)
                    # brickStructure.remove(brick)
                # print(activePowerups)   
                self.__yspeed = -1*(self.__yspeed)
                break
        
    def moveBall(self,grid,obj_Paddle):
        grid[self.__rownum,self.__colnum] = ' '
        temp_row = self.__rownum + self.__yspeed
        temp_col = self.__colnum + self.__xspeed
        
        ''' handling collision with wall'''
        if temp_col < 0 or temp_col > WIDTH -1:
            self.__xspeed = -1*(self.__xspeed)
        if temp_row < 0 or temp_row > HEIGHT - 3:        # subject to change
            self.__yspeed = -1*(self.__yspeed)
    

        ''' handle collision with paddle'''
        stInd = obj_Paddle.getColnum()
        endInd = stInd + PADDLE_LENGTH -1
        midInd = (int)((stInd + endInd)/2)
        if temp_row == PADDLE_ROW and temp_col >= stInd and temp_col <= endInd:
            self.__xspeed += (temp_col-midInd)
            self.__yspeed = -1*(self.__yspeed)

        ''' handle collision with bricks'''
        self.ballBrickCollision(temp_row,temp_col)


        self.__rownum += self.__yspeed
        self.__colnum += self.__xspeed
        grid[self.__rownum,self.__colnum] = self.__ball
    
        
