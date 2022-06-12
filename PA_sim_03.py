import random
import time
import math
import os
 
 
os.system('cls' if os.name == 'nt' else 'clear') # curata consola daca e mac sau windows
 
for i in ["a", "b", "c", "d", "e", "f", "g", "h"]:
    if i == "a":
        mm = "    "
        ww = "       "
    elif i == "b":
        mm = "     "
        ww = "      "
    elif i == "c":
        mm = "      "
        ww = "     "
    elif i == "d":
        mm = "       "
        ww = "    "
    elif i == "e":
        mm = "        "
        ww = "   "
    elif i == "f":
        mm = "         "
        ww = "  "
    elif i == "g":
        mm = "          "
        ww = " "
    elif i == "h":
        mm = "           "
        ww = ""
    os.system('cls' if os.name == 'nt' else 'clear') # curata consola
    print(mm, end='') # printeaza rand gol
    print(r"____/\____/\____:)", end='') # printeaza grafic
    print(ww, end='') # gol
    print(r"<>--^--<>") # grafic
    time.sleep(0.3) # intarzie 3 secunde
    os.system('cls' if os.name == 'nt' else 'clear') # curata consola
    print(mm, end='') # spatiu
    if i != "h": 
        print(r"_____/\____/\___:)", end='')
        print(ww, end='')
        print(r"<>--^--<>")
        time.sleep(0.5) # nu  face nimic fiindca i nu e accesat
    else:
        print(r"_____/\____/\___:o >--^--<>")

''' nu mi-am dat seama ce face programul de fapt si nici nu stiu sa 
il fac decat daca ma uit in hangman ca sa fiu sigura ca nu fac vreo prostie'''