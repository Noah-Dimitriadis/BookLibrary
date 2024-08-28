#!/usr/bin/env python3
# Author: *** Oliver Chan ***
# Date: *** May 20 2022 ***

# Purpose: Creates system info report
# USAGE: ./myreport.py

print("\n") # Add line space

# Display System Report in the Standard Output
print("System Report \n")

# Importing OS module to interact with our Linux Operating System
import os

# Display the current date into the Standard output
daytime = os.popen("date +'%A %B %d, %Y (%I:%M %p)'")
print("The current date:", daytime.read() )

# Dispaly the Hostname of the machine in the Standard Output
machine = os.popen ("hostname")
print("The Hostname of the machine: ", machine.read() )

# Display the kernel version into the Standard Output
krnl = os.popen("uname -r")
print("The kernel version: ", krnl.read() )

#Display the IP address into the Standard Output
ip = os.popen("ip address show")
print("The IP address: \n", ip.read() )

# Display the list of all processes into the Standard Output
ap = os.popen("ps aux")
print("The list of all processes: \n", ap.read() )









