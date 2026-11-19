import sys
import math
import random
import time
import webbrowser
from playsound3 import playsound
import tkinter as tk

# Globale Variablen
randomnum, val, count = random.randint(0, 999), 0, 0

# GUI Fenster erstellen
root = tk.Tk()
root.title("Random Number Roller")
root.geometry("600x400")
root.resizable(False, False)

# --------------------------------------------------
# GUI Elemente
# --------------------------------------------------

title_label = tk.Label(
    root,
    text="Random Number Roller",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=20)

info_label = tk.Label(
    root,
    text="Willkommen beim Random Number Roller!",
    font=("Arial", 13)
)
info_label.pack(pady=10)

number_label = tk.Label(
    root,
    text="???",
    font=("Arial", 48, "bold")
)
number_label.pack(pady=20)

status_label = tk.Label(
    root,
    text="Bereit...",
    font=("Arial", 13)
)
status_label.pack(pady=10)

count_label = tk.Label(
    root,
    text="Versuche: 0",
    font=("Arial", 12)
)
count_label.pack(pady=5)

start_button = tk.Button(
    root,
    text="Start",
    font=("Arial", 14, "bold"),
    width=15
)
start_button.pack(pady=20)


# --------------------------------------------------
# Funktionen Definition
# --------------------------------------------------

def print_the_things():

    print(sys.version, "\n")

    info_label.config(
        text="Welcome to the random number roller!!!"
    )

    status_label.config(
        text=f"The current random number which has to be rolled is: {randomnum}"
    )

    number_label.config(text="???")

    # Nach kurzer Zeit den Rolling-Prozess starten
    root.after(2000, start_rolling)


def rng_gambling():
    global val, count

    count += 1
    val = random.randint(0, 999)

    # Zahl in der GUI anzeigen
    number_label.config(text=str(val))

    # Versuchszähler aktualisieren
    count_label.config(
        text=f"Versuche: {count}"
    )

    print(val)

    if val == randomnum:

        number_label.config(
            text=str(val)
        )

        status_label.config(
            text="HOLEH MOLEHH YOU ROLLED THE NUMBER OMAGAHHHHHH!!!!"
        )

        info_label.config(
            text=f"Geschafft! Es hat {count} Versuche gebraucht."
        )

        print("HOLEH MOLEHH YOU ROLLED THE NUMBER OMAGAHHHHHH!!!!")
        print("It took", count, "tries to roll this number.")

        playsound("yayyy.mp3")

        start_button.config(
            state=tk.NORMAL,
            text="Nochmal starten"
        )

        return

    # Nach 10 ms den nächsten Roll durchführen
    root.after(10, rng_gambling)


def start_rolling():

    global count

    count = 0

    start_button.config(
        state=tk.DISABLED
    )

    status_label.config(
        text="Rolling process gestartet..."
    )

    count_label.config(
        text="Versuche: 0"
    )

    rng_gambling()


def reset_game():

    global randomnum, val, count

    randomnum = random.randint(0, 999)
    val = 0
    count = 0

    number_label.config(text="???")
    count_label.config(text="Versuche: 0")

    status_label.config(
        text="Neues Spiel wird vorbereitet..."
    )

    start_button.config(
        state=tk.DISABLED
    )

    root.after(1000, print_the_things)


# --------------------------------------------------
# Button
# --------------------------------------------------

start_button.config(command=print_the_things)


# --------------------------------------------------
# Programm starten
# --------------------------------------------------

root.mainloop()