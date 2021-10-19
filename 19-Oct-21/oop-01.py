# OOP

# object

stuff = [] # list object
stuff.append('python') # call append method of list
stuff.append('JS') # call append method of list
stuff.append('chunk') # call append method of list
stuff.sort() # call sort method of list
print(stuff) # print() stuff object
print(stuff[0]) # desplay first item of stuff object
print(stuff.__getitem__(0)) # <object>.__getitem__(index) --->> "call __getitem__()" retrieving the 0th item in the list.
print(stuff.__getitem__(1)) # <object>.__getitem__(index) --->> "call __getitem__()"retrieving the 1st item in the list.
print(list.__getitem__(stuff,0)) # <object>.__getitem__(index) --->> "call __getitem__()", retrieving the 0th item in the list.

# display methods of list()
dir(list)

#  Starting with programs
# --------------------- Program : ----------------------
# take input ------> do processing --------> give output
# ------------------------------------------------------
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))