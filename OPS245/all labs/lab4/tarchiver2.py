#!/usr/bin/env python3
# tarchiver.py
# Purpose: Creates a tar archive of a directory
#
# USAGE: ./tarchiver2.py
#
# Author: *** Oliver Chan***
# Date: *** June 26 2022 ***
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dest",help="The name you would like to give the archive.")
parser.add_argument("source",help="The path of the folder to archive.")
parser.add_argument("gzip",help="Compress using gzip.")
args = parser.parse_args()

print('Archiving folder content: ')

# Specify the full path of the folder to archive
# source_path = input('\nEnter full path of the directory to Archive. \nDirectory Path:  ')
source_path = args.source

# Create New directory to save achive files
# directory1 = input('\nType Directory Name to save archive: ')
directory1 = args.dest 
path = '/home/ochan10/tarfiles/'

# Creating new folder to save archive files
if not os.path.exists(directory1):
 os.mkdir(os.path.join(path, directory1))
 new_folder = os.path.join(path, directory1)
 print("\nThe new directory is created in", new_folder )
 os.chdir(os.path.join(path, directory1))


# print("Do you want to compress the tar file? ")
# val = input("Enter(y/n): ")
# if val == 'y':
#  print("\nWhat type of compressing?")
#  print("1: gzip:")
#  print("2: bzip2:")
#  print("3: xzip:")

 print("Compressing using gzip.")  
#  val2 = input("\nEnter number for your selection: ")
 gzip = args.gzip
 if gzip == 'gzip':
  print("Creating compressed files using gzip (.tar.gz)")
  os.system('tar -cvzf %s/archive1.tar.gz %s/.' %(new_folder,source_path) )
  os.system('ls -l %s' %(new_folder) )
  print("\nTarfiles are saved in this folder: {0}" .format(os.getcwd()))
  
# elif val2 == '2':
#  print("Compressing using bzip2")
#  os.system('tar -cvjf %s/archive1.tar.bz2 %s/.' %(new_folder,source_path) )
#  os.system('ls -l %s' %(new_folder) )
#  print("\nTarfiles are saved in this folder: {0}" .format(os.getcwd()))

# elif val2 == '3':
#  print("Compressing using xzip")
  

# elif val == 'n':
#  print("Creating Uncompressed Tar file... (.tar) ")
#  os.system('tar -cvf %s/archive1.tar %s/.' %(new_folder,source_path) )
#  os.system('ls -l %s' %(new_folder) )
#  print("\nTarfiles are saved in this folder: {0}" .format(os.getcwd()))

 






