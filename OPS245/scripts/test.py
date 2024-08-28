import os
import ipaddress

#def validate_ip_address(address):
#    try:
#        ip = ipaddress.ip_address(address)
#        print("IP address {} is valid.".format(address))
#
#    except ValueError:
#        print("IP address {} is not valid.".format(address))
#        print("Enter valid IP address!!!")
        


device_name = input("Make sure you enter the correct Device name NIC(ex: eth0). \nEnter Device name: ")

ip_add = input("Enter IP address: ")
try:
    print("IP address {} is valid.".format(ip_add))
    
except ValueError:
    print("IP address {} is not valid.".format(ip_add))
    print("Enter valid IP address!!!")

gateway = input("Enter IP address: ")
try:
    print("IP address {} is valid.".format(gateway))
    
except ValueError:
    print("IP address {} is not valid.".format(ip_add))
    print("Enter valid IP address!!!")




    


#print("Device name=%s" %(device_name.strip()))
#print("New IP address=%s" %(ip_add.strip()))
#print("MAC Address=%s" %(mac_add.strip()))
#print("ONBOOT=%s" %(var_boot.strip()))
#print("Network Prefix=%s" %(net_prefix))
#print("Default Gateway=%s" %(gateway))
#print("Primary DNS server=%s" %(pri_dns))

f = open("demofile.txt", "w")
f.write("Device name=%s" %(device_name.strip()))
f.write("\nNew IP address=%s" %(ip_add.strip()))
#f.write("\nMAC Address=%s" %(mac_add.strip()))
#f.write("\nONBOOT=%s" %(var_boot.strip()))
#f.write("\nNetwork Prefix=%s" %(net_prefix))
f.write("\nDefault Gateway=%s" %(gateway))
#f.write("\nPrimary DNS server=%s" %(pri_dns))
f.close()

f = open("demofile.txt", "r")
print(f.read())



    
   

#gateway = input("Enter gateway: ")
#validate_ip_address(gateway.strip())

#pri_dns = input("Enter Primary DNS server: ")
#validate_ip_address(pri_dns.strip())

#mac_add = input("Enter MAC address: ")
#net_prefix = input("Enter Net PREFIX: ")
#var_boot = input("NIC automatically turn on? Type yes or no: ")
    


#print("MAC Address=%s" %(mac_add.strip()))
#print("ONBOOT=%s" %(var_boot.strip()))
#print("Network Prefix=%s" %(net_prefix))
#print("Default Gateway=%s" %(gateway))
#print("Primary DNS server=%s" %(pri_dns))


#f.write("\nMAC Address=%s" %(mac_add.strip()))
#f.write("\nONBOOT=%s" %(var_boot.strip()))
#f.write("\nNetwork Prefix=%s" %(net_prefix))
#f.write("\nDefault Gateway=%s" %(gateway))
#f.write("\nPrimary DNS server=%s" %(pri_dns))
#f.close()






