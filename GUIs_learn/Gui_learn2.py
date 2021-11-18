import tkinter

# launch window
root = tkinter.Tk()
root.title("ASA")
root.geometry("350x250")
root.iconbitmap('Elegantthemes-Beautiful-Flat-Barchart.ico')
root.config(bg="#1234ff")
from tkinter import BOTH
# create lable
name_lable1 = tkinter.Label(root,text = "This is lable for ASA", font=('Arial',16,'bold')).pack()
# name_lable1.pack(padx = 10, pady=5, fill = 'x')
# name_lable2 = tkinter.Label(root, text="Hi I'm Asahmed", font=('Arial', 12, 'bold'))
# name_lable2.pack(padx = 10, pady=10, anchor='sw', fill='y', expand=True)
# name_lable3 = tkinter.Label(root, text="Hi im SAM Again ", font=('Cambria', 12, 'bold'), bg='#ffffff')
# name_lable3.pack(padx = 10, pady = 10, ipadx=3, ipady=1, anchor='w')

name_button = tkinter.Button(root, text='click')
name_button.grid(row=0,column=0)


root.mainloop()