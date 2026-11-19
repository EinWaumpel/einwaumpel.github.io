import sys
import math
import random
import time
import webbrowser
from playsound3 import playsound
import tkinter as tk
import os
import subprocess

# Globale Variablen
randomnum, val, count = random.randint(0, 99), 0, 0


# Funktionen Definition
def startt():

    print(sys.version, "\n")

    print("Welcome to the random number roller!!!")
    time.sleep(2)
    print("The current random number which has to be rolled is: ", randomnum)
    time.sleep(2.5)
    print("The rolling process will start soon...")
    time.sleep(3)

    rng_gambling()

def rng_gambling():
    global val, count 
    
    while True:
        count += 1
        val = random.randint(0, 99)
        print(val)
        if val == randomnum:
            print("HOLEH MOLEHH YOU ROLLED THE NUMBER OMAGAHHHHHH!!!!")
            print("It took", count, "tries to roll this number.")
            playsound("yayyy.mp3")
            time.sleep(2)
            again_q()
        time.sleep(0.01)

def again_q():
    
    again = input("Do you want to roll again? (Y/N): ")

    if again.lower() == "y":
        clear_console()
        startt()
    else:
        print("okaii baiii!!")
        exit()

def clear_console():
    command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
    subprocess.run(command, check=False)

# Funktionen Anwendung
startt()

