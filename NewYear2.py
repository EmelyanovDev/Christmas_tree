from time import sleep
from random import randint
from colorama import Fore
import os
sleep(1)
def randcolor(text):
    rand = randint(1, 10)
    if(rand == 3):
        return(Fore.BLUE + text + Fore.RESET)
    if(rand == 1):
        return(Fore.RED + text + Fore.RESET)
    if(rand == 2):
        return(Fore.YELLOW + text + Fore.RESET)
    return(Fore.GREEN + text + Fore.RESET)
clear = lambda: os.system('cls')
clear()
symbol = "0"
width = 11
offset = 25
textoffset = 7
trunk = 2
work = True
print(Fore.YELLOW + " " * offset + "*")
for i in range(1, width):
    sleep(0.2)
    print(Fore.RESET + ' ' * (offset-i) + '/' + Fore.GREEN + symbol * (2*i-1) + Fore.RESET +  '\\')
for i in range(trunk):
    sleep(0.2)
    print(" " * (offset-2), "|-|")
print('')
print(" " * (offset-textoffset) +"С Новым Годом!")

while True:
    sleep(0.5)
    clear()
    if(work):
        print(Fore.YELLOW + " " * offset + "*" + Fore.RESET)
    else:
        print(" " * offset + "*")
    work = not work
    for i in range(1, width):
        text = ''
        for _ in range(2*i-1):
            text += randcolor(symbol)
        print(' ' * (offset-i) + '/' + text +  '\\')
    for i in range(trunk):
        print(" " * (offset-2), "|-|")
    print('')
    print(" " * (offset-textoffset) +"С Новым Годом!")

