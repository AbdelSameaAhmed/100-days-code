# Exercise1: will the the following code return error??
"""show_version()
def show_version():
    print ('Version 1.0a')"""
# solution:
# Yess
# Exercise2: will the the following code return error??
def test():
    show_version()
def show_version():
    print('Version 1.0a')
test()
# solution:
# No

# Exercise3:

import sys
print(sys.maxint)