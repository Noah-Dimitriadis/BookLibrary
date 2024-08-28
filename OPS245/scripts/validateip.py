import os
import ipaddress


# Function to check IP address is valid or not
def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid.\n".format(address))

    except ValueError:
        print("IP address {} is not valid.\n".format(address))
        print("Enter valid IP address!!!")


#Enter the name of the interface
device_name = input("Make sure you enter the correct Device name NIC(ex: eth0). \nEnter Device name: ")

#Enter static IP address
ip_add = input("Enter IP address: ")
validate_ip_address(ip_add.strip())

#Enter Network Prefix
net_prefix = input("Enter Net PREFIX: ")

#Enter default gateway
gateway = input("Enter Gateway: ")
validate_ip_address(gateway.strip())

#Enter the interface's MAC Address
mac_add = input("Enter MAC Address: ")

#Enter the Primary DNS server
pri_dns = input("Enter Primary DNS server: ")
validate_ip_address(pri_dns.strip())

#Decide if interface should automatically turn on when the machine boots
var_boot = input("NIC automatically turn on?(yes or no): ")
    
#Print result
print("\nDevice name=%s" %(device_name.strip()))
print("New IP address=%s" %(ip_add.strip()))
print("MAC Address=%s" %(mac_add.strip()))
print("ONBOOT=%s" %(var_boot.strip()))
print("Network Prefix=%s" %(net_prefix))
print("Default Gateway=%s" %(gateway))
print("Primary DNS server=%s" %(pri_dns))

# Save to file
# Saving file to bin folder for now
# using demofile.txt instead of overwriting /etc/sysconfig/network-scripts/ifcfg-eth0 
f = open("demofile.txt", "w")
f.write("DEVICE=%s" %(device_name.strip()))
f.write("\nIPADDR=%s" %(ip_add.strip()))
f.write("\nPREFIX=%s" %(net_prefix))
f.write("\nGATEWAY=%s" %(gateway))
f.write("\nHWADDR=%s" %(mac_add.strip()))
f.write("\nDNS=%s" %(pri_dns))
f.write("\nONBOOT=%s" %(var_boot.strip()))
f.write("\nBOOTPROTO=static")
f.write("\nNM_CONTROLLED=yes")
f.write("\nIPV6INIT=no")
        
f.close()





#y = 1
#n = 2
#if var_boot == 1:
#    on_boot = "on"
#    print("ONBOOT $s" %(on_boot))
#elif var_boot == 2:
#    on_boot = "off"
#    print("ONBOOT %s" %(on_boot))
