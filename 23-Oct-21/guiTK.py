# ---------------------------------
# GUI -----------------------------

# exercise_1
# ----------------------------------
# Write a Python GUI program
#  to import Tkinter package and create 
# a window and set its title.
# solution
# --------------------------
import tkinter as tk
# cretae instance
parent = tk.Tk()
# add title
parent.title("ASA")
parent.mainloop()
# ----------------------------
print("*" * 80)
# exercise_2
# ----------------------------------
# Write a Python GUI program to import 
# Tkinter package and create a window.
# Set its title and add a label to the window

# import tkinter as tk
# cretae instance
roo = tk.Tk()
# create title
roo.title("ASA")
# roo.Label()
mylable = tk.Label(roo, text = "this is tkinter gui")
mylable.grid(column = 0, row = 0)
roo.mainloop()
tk.Label(roo, "this is 1st gui").grid(column = 0, row = 0)
roo.mainloop()


print("*" * 80)
# exercise_3
# ----------------------------------
# Using tkinter module Write a Python GUI program to create a label and 
# change the label font style (font name, bold, size)
# -----------------------
# solution
# import tkinter
import tkinter as tk
# create instance
parent = tk.Tk()
# create titel
parent.title("ASA")
# create lable
myLable = tk.Label(parent, text="I love Python", font=("Arial", 20))
myLable.grid(column = 0, row = 0)

parent.mainloop()

# print("*" * 80)
# exercise_3
# ----------------------------------
# Write a Python GUI program to
# create a window and set the default window size using tkinter module
# -----------------------
# solution

import tkinter as tk
scre = tk.Tk()
scre.title("ASA")
mylable = tk.Label(scre, text="I love PYTHON" , font=("Arial", 20))
mylable.grid(column=0, row=0)
scre.geometry('200x100')

scre.mainloop()


# exercise_4
# ----------------------------------------------
print("*" * 80)
# ------------------------------------------------
# ---------------------------------
# tkinter widgits -----------------------------

#  Write a Python GUI program to add a button in 
#  your application using tkinter module

# -----------------------
# solution

import tkinter as tk
parent = tk.Tk()
parent.title("ASA")
myLable = tk.Label(parent, text="I love Python", font=("Arial", 10))
# myLable.grid(column = 4, row=2)
# parent.geometry("200x100")
myButton = tk.Button(parent, text="Quit", height =4, width =35,command=parent.destroy)
myButton.pack()
parent.mainloop()

# exercise_4
# ----------------------------------------------
print("*" * 80)
#  Write a Python GUI program to add a 
# canvas in your application using tkinter module

import tkinter as tk 
parent = tk.Tk() 

canvas_width = 100
canvas_height = 80
w = tk.Canvas(parent, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#ff00f0")
parent.mainloop()
