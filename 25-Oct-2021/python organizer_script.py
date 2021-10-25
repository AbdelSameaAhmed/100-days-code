# --------------------------------------
# ----File's Organizer Application -----
# --------------------------------------
"""
This Application organizes the files according its extension and
create a new folders for each extension.
"""
# -------------- import required modules --------------
import os
import time
import shutil

# -------------- Folder abs path -------------------------
# determin the current working directory 
# for start organize its files by one of the following three methodes:
# a- use the os module
#---------
currentDire = os.path.dirname(os.path.realpath(__file__))
print(currentDire)
# b- use the os module
# ---------
dir2 = os.path.abspath(os.path.dirname(__file__))
print(dir2)
# c- recieve the folder from user
# ---------
dir3 = input("please enter the folder abs path to start organize: ")

# ----------------- Welcome statement -----------------------
print("*" * 56)
print(f"{'*' * 15} welcome to Organizer App {'*' * 15}")
print("*" * 56)

# ---------------- start organize files extentions -----------

# Images
