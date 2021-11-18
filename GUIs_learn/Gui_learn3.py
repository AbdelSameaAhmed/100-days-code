import tkinter
from tkinter import *
# launch window
window = tkinter.Tk()
window.title("ASA")
window.geometry("450x350")
window.config(bg='#ff00ff')
window.resizable(0,0)
window.iconbitmap('Social-Media-Icons-Glossy-Social-Flickr.ico')
name_lable=tkinter.Label(window, text="ASAHMED")
name_lable.pack(padx=10, pady= 5)

name_button=tkinter.Button(window,text="click")

name_button.pack(anchor='center')
window.mainloop()
