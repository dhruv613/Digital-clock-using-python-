import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")


def clock():    
    string = strftime("Time\n%I:%M:%S\nDate\n%d/%m/%Y")
    label.config(text=string)
    label.after(1000, clock)

label = tk.Label(root, font=("ds-digital", 80), background="black", foreground="red")
label.pack(anchor="center")
clock()
root.mainloop()
