from colorama import init,Fore,Back,Style
import numpy as np
init(autoreset=True)

# dimensions
HEIGHT = 40
WIDTH = 140
# WIDTH = 142
# HEIGHT = 35
BRICK_LENGTH = 6 
PADDLE_LENGTH = 7
PADDLE_ROW = HEIGHT - 3

START_R = (int)(HEIGHT/2 - 12)          # convention
START_C = (int)(WIDTH/4)
END_C = (int)(WIDTH - WIDTH/4) 

## global variables
# global NUM_BRICKS 

NUM_BRICKS =0
brickStructure = []  
# print("INN HEADER", NUM_BRICKS)
