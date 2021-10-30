# urllib ---------
# ----------------
# -------- request// parse// --------

# -----------------------
# request
# -----------------------

import urllib.request
url1 = urllib.request.urlopen('https://www.google.com')
# print(url1.read())

# ----------------------
# parse
# -----------------------
import urllib.parse, urllib.request

url = 'http://pythonprogramming.net'
values = {'s': 'basic', 
            'submit': 'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()
# print(respData)

saveFile = open('readtxt.txt', 'w')
saveFile.write(respData)
saveFile.close()

