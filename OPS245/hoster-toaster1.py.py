#!/usr/bin/env python3
# hoster-toaster.py
# Purpose: Alter the machine's /etc/hosts file
#
# USAGE: ./hoster-toaster.py
#
# Author: *** Oliver Chan***
# Date: *** July 25 2022 ***

# Make sure script is being run with elevated permissions
# currentuser = os.popen('whoami')
# if currentuser.read().strip() != 'root':
# print("You must be root" ) 
# exit()

import os

print("1. Current working directory: {0}" .format(os.getcwd()) )
var1 = input("\nEnter the full path of file: ")
path1 = os.path.join(var1)
print('\nPath you entered is: ', path1)


# change directory
try:
    os.chdir(var1)
    # checking current directory
    print("\n2. Current working directory: {0}\n" .format(os.getcwd()) )
    print("This is the content of the file that will be copied to the /etc/hosts\n")
    # Open and read file
    f = open("hosts.txt", "r")
    content1 = f.read()
    print(content1)
    f.close()
   
    # writing to /etc/hosts file(using C:\\folder2\\final.txt as a testing directory)
    f2 = open('C:\\folder2\\final.txt', "w")
    f2.write(content1)
    f2.close()

    # printing new content of final.txt
    print("\nNew content of /etc/hosts file\n**********************************")
    f2 = open('C:\\folder2\\final.txt', "r")
    print(f2.read())
    f2.close()

except FileNotFoundError:
    print("\nDirectory is not found! \nTry again...")




