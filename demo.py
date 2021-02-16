from colorama import init,Fore,Back,Style
import numpy as np
init(autoreset = True)
print(Fore.RED + 'some red text')
brick = Back.RED+ ' '
print(brick)
print(Style.BRIGHT + 'and in dim text')
# print(Style.RESET_ALL)
print('back to normal now')

arr = np.zeros((5,6),dtype = '<U20')
arr[:] = ' '
arr1 = Back.BLUE + ' '
arr[2:4, 2:4] = np.tile(Back.BLUE + ' ',2)
# print("hey")

for i in range (5):
    for j in range(6):
        print(Back.GREEN + arr[i][j], end = '')
    print()

print('\n')

class Brick:
    def __init__(self,strength):
        self.__num = 2
        self.__strength = strength
    
    # def result(self):
    #     print(self.__num)
        # print(self.__strength)

class chotiBrick(Brick):
    def __init__(self, strength):
        super().__init__(strength)
        # self.__r = self.__num
        self.__strength = strength
        
    def result(self):
        # print(self.__r)
        print( self.__strength)

obj = chotiBrick(4)
obj.result()

print(Fore.BLACK + 'BLACK')
print(Fore.BLUE + 'BLUE')
print(Fore.CYAN + 'CYAN')
print(Fore.GREEN + 'GREEN')
print(Fore.LIGHTBLACK_EX + 'LIGHTBLACK_EX')
print(Fore.LIGHTBLUE_EX + 'LIGHTBLUE_EX')
print(Fore.LIGHTCYAN_EX + 'LIGHTCYAN_EX')
print(Fore.LIGHTGREEN_EX + 'LIGHTGREEN_EX')
print(Fore.LIGHTMAGENTA_EX + 'LIGHTMAGENTA_EX')
print(Fore.LIGHTRED_EX + 'LIGHTRED_EX')
print(Fore.LIGHTWHITE_EX + 'LIGHTWHITE_EX')
print(Fore.LIGHTYELLOW_EX + 'LIGHTYELLOW_EX')
print(Fore.MAGENTA + 'MAGENTA')
print(Fore.RED + 'RED')
print(Fore.RESET + 'RESET')
print(Fore.WHITE + 'WHITE')
print(Fore.YELLOW + 'YELLOW')

print('\n')
colors = dict(Back.__dict__.items())

for color in colors.keys():
    print(colors[color] + f"{color}")