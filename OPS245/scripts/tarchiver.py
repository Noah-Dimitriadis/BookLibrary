#!/usr/bin/env python3
# tarchiver.py
# Purpose: Creates a tar archive of a directory
#
# USAGE: ./tarchiver.py
#
# Author: *** Oliver Chan***
# Date: *** June 12 2022 ***
import os


print('Archiving folder content: ')

# Specify the full path of the folder to archive
source_path = input('\nEnter full path of the directory to Archive. \nDirectory Path:  ')

# Create New directory to save achive files
directory1 = input('\nType Directory Name to save archive: ')
path = '/home/ochan10/tarfiles/'

# Creating new folder to save archive files
if not os.path.exists(directory1):
 os.mkdir(os.path.join(path, directory1))
 new_folder = os.path.join(path, directory1)
 print("\nThe new directory is created in", new_folder )
 os.chdir(os.path.join(path, directory1))

 var = "y"
 var2 = "n" 

 print("Run with gzip compression: ")
 print("Yes(y) for gzip")
 print("Else (n) for no")


#Archiving files to the destination folder
# os.system('tar -cvzf %s/archive1.tar.gz %s/.' %(new_folder,source_path) )
 os.system('ls -l %s' %(new_folder) )
 print("\nTarfiles are saved in this folder: {0}" .format(os.getcwd()))






# os.system('ls -l')
# os.system('pwd')
# Archiving source directory to destination folder specified by user
#print("\nCurrent working directory: {0}" .format(os.getcwd()))
 
#print("Path: ", da
# os.system( 'ls -l %s' %(new) )
 

##path1 = '/home/ochan10/tarfiles/'
# Print the current working directory
##print("Current working directory: {0}".format(os.getcwd()))

# Change the current working directory
##os.chdir(os.path.join(path1, directory1))
# Print the current working directory
##print("Current working directory: {0}".format(os.getcwd()))




