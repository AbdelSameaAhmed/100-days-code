# --------- socket ---------
# --------------------------
# ---------urllib ----------
# --------------------------
"""Definition An API
(short for Application Programming Interface)
API is a set of URLsand parameters
 that is designed to be called by programs across the Internet.
"""
import os
print(os.getcwd())
import urllib.request
connection = urllib.request.urlopen("https://www.nasdaq.com/market-activity/stocks/aapl")
response_string = connection.read().decode()

file_u = open('file_1.txt')
file_u.write(response_string)