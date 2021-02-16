from headerfile import *
import numpy as np

class Screen:
    def __init__(self):
        self.__grid = np.zeros((HEIGHT,WIDTH),dtype = '<U20')
        self.__grid[:] = ' '

    def give_grid(self):
        return self.__grid

    def create_bg(self,grid):
        print("\n")
        # print("\n")
        
        self.__grid = grid
        for i in range(HEIGHT):
            for j in range(WIDTH):
                print(Back.BLACK + self.__grid[i][j], end = '')
                # print(grid[i][j], end = '')
            print()

    # def change_grid(self,ch,x,y):





        # grid[0][0]
# obj_Screen = Screen()
# obj_Screen.create_bg()
