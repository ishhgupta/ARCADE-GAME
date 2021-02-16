from screen import Screen
from headerfile import END_C, START_C, START_R
from headerfile import *
import random

class Brick:

    def __init__(self,strength,posY, posX) :
        self.__brick = ' '                          # taking base of brick to be ' '
        self.__length = 6                           # taking length of brick to be 6
        # self.__length = len(self.__brick)
        self.__y = posY
        self.__x = posX
        self.__strength = strength

    def getBrick(self):
        if self.__strength == 4:
            return np.tile(Back.MAGENTA + ' ',6)
        elif self.__strength == 3:
            return np.tile(Back.BLUE + ' ',6)
            # return Back.BLUE + self.__brick
        elif self.__strength == 2:
            return Back.GREEN + self.__brick
        elif self.__strength == 1:
            return Back.YELLOW + self.__brick
        else:
            return Back.RED + self.__brick
    
    def getLen(self):
        return self.__length
        # print(self.__length)
    # def placeBrick(self):
        
        
obj = Brick(1,2,3)
# obj.getLen()

# def generateBricks():

obj_Screen = Screen()
grid = obj_Screen.give_grid()

length = obj.getLen()


for i in range (20):
    for j in range(START_C, END_C, length):
        # print(grid[START_R+i, j:j+length])
        grid[START_R+i, j:j+length] = Brick(random.randint(1,5),2,3).getBrick()

obj_Screen.create_bg(grid)

