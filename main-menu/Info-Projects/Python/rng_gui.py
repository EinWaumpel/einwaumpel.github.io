import threading
import time
import tkinter as tk
from tkinter import ttk

# Initialize Window
root = tk.Tk()
root.title("RNG Number Roller")
root.geometry('600x400+50+50')
root.resizable(False, False)
root.attributes("-topmost", 1)
root.iconbitmap("waumpel.ico")

# Functions
def btn_clkd():
    print("rahh")

def cycle_title():
    while True:
        root.title("RNG Number Roller")
        time.sleep(1)
        root.title("Made by EinWaumpel")
        time.sleep(1)
        root.title("Made in school rahh")
        time.sleep(1)

# constantly print rahh and reek in a 0.5 second interval in a seperate thread
background_thread = threading.Thread(target=cycle_title, daemon=True)
background_thread.start()

# Add Window Elements
ttk.Button(root, text="Roll Random Number", command=btn_clkd).pack(side="bottom", pady=20)

# Keep Window alive
root.mainloop()