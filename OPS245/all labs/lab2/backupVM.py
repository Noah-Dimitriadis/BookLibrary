#!/usr/bin/env python3
# backupVM.py
# Purpose: Backs up virtual machines
#
# USAGE: ./backupVM/py
#
# Author: *** Oliver Chan ***
# Date: *** Jun 3 2022 ***

import os

# Make sure script is being run with elevated permissions
currentuser = os.popen('whoami')
if currentuser.read().strip() != 'root':
 print("You must be root" ) 
 exit()

else:
 print('\nSelect which VM to backup:')
 print(' centos1 = 1')
 print(' centos2 = 2')
 print(' centos3 = 3')
 print(' all VM  = 4')
 print(' E x i t = 5 \n')

val = input("Enter Value: ")
if val == '1': 
 print('Backing up centos1, please wait...')
 os.system('gzip < /var/lib/libvirt/images/centos1.qcow2 > ~ochan10/backups/centos1.qcow2.gz')

elif val == '2':
  print('Backing up centos2, please wait...')
#  os.system('pwd')
  os.system('gzip < /var/lib/libvirt/images/centos2.qcow2 > ~ochan10/backups/centos2.qcow2.gz')

elif val == '3':
 print('Backing up centos3, please wait...')
 os.system('gzip < /var/lib/libvirt/images/centos3.qcow2 > ~ochan10/backups/centos3.qcow2.gz')

elif val == '4':
 print('Backing up all VM, please wait...')
# os.system('gzip < /var/lib/libvirt/images/centos1.qcow2 > ~ochan10/backups/centos1.qcow2.gz')
# os.system('gzip < /var/lib/libvirt/images/centos2.qcow2 > ~ochan10/backups/centos2.qcow2.gz')
# os.system('gzip < /var/lib/libvirt/images/centos3.qcow2 > ~ochan10/backups/centos3.qcow2.gz')

elif val == '5':
 exit()



