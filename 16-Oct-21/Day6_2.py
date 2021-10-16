# ---------------------------------------
# Chapter 12 (Book : Network with python)
# ---------------------------------------
# Network ---- socket -------------------
# ---------------------------------------

# ------------------------------
# start with intro to network
# ------------------------------
# introduction of computer network
""" network is network of networks"""
        # 1. a bilion of connected coputing deices
        # 2. links: wired or wirless
        # 3. Packet switches : routers, switches
""" internet provider"""
    # isp internet service provider
        #-regional ISPs #- glopal ISPs
""" protocol : controle sending and recieving message"""
        # TCP(be sure connection of tow devices), HTTPS,
        #  IP(be sure connection of tow routers)
        # wifi protocole or 802.11 
"""internet standards """
    # RFC "Request for comment" -------------------------
    # IETF "Internet Engineering sk Force" --------------


"""
Network structure
    - network edges
    - Access network : wired or wirless
    - network core : internconnected routers
"""
# ---------------------------------------------
""" How to connect to internet network"""
# residential : DSL : """Digital subscribrt line"""
# institutional
# Mobile
# socket 
# -----------------------------------------------


# the following paragaraph from :
# https://www.geeksforgeeks.org/socket-programming-python/

"""
Socket programming is a way of connecting two nodes on a network 
to communicate with each other.
One socket(node) listens on a particular port at an IP,
while the other socket reaches out to the other to form 
a connection. The server forms the listener socket
while the client reaches out to the server. 
They are the real backbones behind web browsing. 
In simpler terms, there is a server and a client.

Socket programming is started by importing the socket library and making a simple socket. 
import socket
>>> s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Here we made a socket instance and passed it two parameters.
The first parameter is AF_INET and the second one is SOCK_STREAM. 
AF_INET refers to the address-family ipv4.
The SOCK_STREAM means connection-oriented TCP protocol. 

if any error occured during creating socket,
error is thrown and we can only connect to a server by knowing its IP.
You can find the IP of the server by using this : 
>>> ping "www.google.com"
or using socket module.
>>> ip = socket.gethostname('www.google.com')
>>> print(ip)

""" 

# -----------------------------------------------------

    # the following paragarph from python for everyone book
"""
    socket is much like a file,
    except that a single socket provides a two-way connection
    between two programs.
    You can both read from and write to the same socket.
    - If you write something to a socket, it is sent to the application at the other end
    of the socket.
    - If you read from the socket, you are given the data which the other
    application has sent.
"""
# Perhaps the easiest way to show how the HTTP protocol works is to write a very
# simple Python program that makes a connection to a web server and follows the
# rules of the HTTP protocol to request a document and display what the server
# sends back.


# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
# mysock.close()

print("*" * 70)

# --------------------------------------------------------------------
# ----------------------------- time of code -------------------------
# --------------------------------------------------------------------

# generate the ip address and machine name

import socket
# get the ip address of local host
machine_name = socket.gethostname()
print(machine_name)
ip_address = socket.gethostbyname(machine_name)
print(ip_address)

print("*" * 70)
# get the ip address of google

ip_google = socket.gethostbyaddr('google.com')
print(ip_google)


print("*" * 70)

# -------------------------------------------------
# get service Name

port = 21
sevice_name = socket.getservbyport(port)
print(sevice_name)

# get port for specific service
service  = "https"
port_name = socket.getservbyname(service)
print(port_name)
