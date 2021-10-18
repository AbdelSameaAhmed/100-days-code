# --------- socket ---------
# --------------------------
# ---------urllib ----------
# --------------------------

# -------------------- Intro ---------------- #
# --------------------------------------------#

"""
Definition An API
(short for Application Programming Interface)
API is a set of URLsand parameters
that is designed to be called by programs across the Internet.
"""

import os

# print(os.getcwd())
import urllib.request
connection = urllib.request.urlopen("https://www.nasdaq.com/market-activity/stocks/aapl")
response_string = connection.read().decode()
for line in response_string:
    print(line)
# file_u = open('fileurl01.txt', 'w')
# file_u.write(response_string)

# -------------------------------
# -------- Socket ---------------
# -------------------------------
# import socket
# # get machien name using python
# machien_name = socket.gethostname()
# print(f"The machien name is : {machien_name}")
# # get ip_adress using python
# ip_address = socket.gethostbyname(socket.gethostname())
# print(f"The ip address is: {ip_address}")