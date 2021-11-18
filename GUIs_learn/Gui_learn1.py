# ---------------------------
# ------- GUI tkinter -------
# --------------------------


"""-1- import tkinter"""
import tkinter 
# -------------------------
"""-2- define window"""
# -------------------------
root = tkinter.Tk()

# -------------------------
"""-3- customize window"""
# -------------------------
root.title("ASA")
root.iconbitmap('Thesquid.ink-Free-Flat-Sample-Football.ico')
# window.geometry(widthxheight)
root.geometry("350x400")
# resizable x, y
root.resizable(1,1)
# root config(bg='', fg )
root.config(bg = '#01ffff')


#-------------------------------
#-------------------------------
# second window/
#  -----------------
# -------------------------

# top = tkinter.Tk()
# top.title('2ND')
# top.geometry("200x200+500+50")
# top.config(bg='#12345f')

"""last step- Run root window main loop"""
# -------------------------

root.mainloop()