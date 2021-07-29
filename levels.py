from headerfile import *
from screen import Screen
from headerfile import END_C, START_C, START_R, BRICK_LENGTH

from colorama import init,Fore,Back,Style
init(autoreset=True)

import numpy as np
import random 

class Level:
    def __init__(self):
        self._score = 0
        self._lives = 2
        self._levelNum = 1
        self._numBricks = 0

    def getLives(self):
        return (str)(self._lives)
    def getScore(self):
        return self._score

class level1(Level):
    def __init__(self):
        super().__init__()
        self._levelNum = 1

# class level2()