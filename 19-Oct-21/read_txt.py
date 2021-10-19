# Exercise :
# Create program can read txt files
# these program take a file from user and reading these file,
# in order to be listened by user

# loading the required modules
from gtts import *
import os
# define variable recieving  file from user

fileName= input("Please enter your file name: ")

f = open(fileName)
x = f.read()

language = 'en'

audio = gTTS(text =x, lang = language, slow = False)

audio.save("read.wav")

os.system("read.wav")