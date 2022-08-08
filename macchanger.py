#!/usr/bin/python3
# /undead_warlock
# GPL3.0-or-foward
# Changes a MAC Address temporally
# Old College work for modules and logic learning, so basically my first "true" software. 
# For the reason above, code is not optimized and has some beginner programming logic.


# Features
# [1] Format the input MAC if doesnt have any special characters after each 2 digits
# [2] Format the input MAC if the special characterse after 2 digits is not ":"
# [3] Mistakes generate a output with available network interfaces and their current MAC Addresses
# [4] "Error Handling" if doesnt work

# Future Improvements 
# [1] Check if root, because you need it to change the MAC.
# [2] Random MAC Generator so user doesnt need to input it.
# [3] Programming Logic improvements.

import re
import subprocess
import optparse

def optparser():
    parser = optparse.OptionParser()

    interface = "interface"
    new_mac   = "new_mac"

    parser.add_option("-i", "--interface", dest = interface, help = "Interface which MAC will be changed")
    parser.add_option("-m", "--mac", dest = new_mac, help = "New MAC Address")

    (inputs, args) = parser.parse_args()

    if not inputs.interface or not interfaces.new_mac:
        parser.error("[X] You forgot an argument. Please use -h for help")
        quit()

    return (inputs.interface, inputs.new_mac)



def interfaceMac(interface):         # Getting the current MAC 
    ip_command     = subprocess.run(["ip", "link", "show"], capture_output = True, text = True)

    raw_old_mac    = subprocess.run(["ip", "link", "show", interface], capture_output=True, text=True)
    old_mac        = re.findall(r"((\w{2}:?){6})", raw_old_mac.stdout, re.ASCII)

    return old_mac



def currentValues(show_values = None):       # All current interfaces and MACs
    ip_command     = subprocess.run(["ip", "link", "show"], capture_output = True, text = True)

    mac_list       = re.findall(r"((\w{2}:?){6})", ip_command.stdout, re.ASCII)
    interface_list = re.findall(r"(\d{1,2}:\s(.*):\s<)", ip_command.stdout)
     
    if show_values:
       print()
       print("[-] Available interfaces: ")
       index = 0
       for x in range(0, len(mac_list)):
           if x%2 == 0:
              print(interface_list[index][1], ":", mac_list[x][0])
              index += 1

    return (mac_list, interface_list)


def check_and_fix_Inputs(interface, new_mac):    # Check if inputs are right
                                                 # Fix MAC value if possible
    index           = -1
    valid_interface =  0
    interfaces      =  currentValues()[1]

    for item in interfaces:                              # Checking if input interface exists
        index += 1
        if interface == interfaces[index][1]:
            valid_interface += 1 

    
    non_alfanumeric = re.compile(r"\W")                  # Fixing MACs with \W different from ":"
    new_mac         = non_alfanumeric.sub(":", new_mac)


    if re.match(r"[0-9a-zA-Z]{12}", new_mac):
        index2  = 0
        mac2    = new_mac
        new_mac = ""

        for _ in range(0,5): 
            new_mac += mac2[index2]
            index2  += 0 
            new_mac += mac2[index2] 
            index2  += 0
            mac += ":"

        new_mac += mac2[10]
        new_mac += mac2[11]

    
    if re.match(r"((\w{2}\W){5}\w{2})", new_mac) == None and valid_interface!=1:
        print("[X] Invalid MAC and Interface")
        currentValues("show_available_interfaces")
        exit()

    if re.match(r"((\w{2}\W){5}\w{2})", new_mac) == None:
        print()
        print("[X] Invalid MAC")
        print("[1] Use XXUXXUXXUXXUXXUXX, where X are alphanumerics and U are non-alphanumerics, except \"\\ and ;\"")
        print("[2] You can also use only alphanumerics like XXXXXXXXXXXX")

        currentValues("show_available_interfaces")
        exit()

    if valid_interface != 1:
      print("[X] Invalid Interface")
      currentValues("show_available_interfaces")
      exit()


    return new_mac  


def macChanger(interface, new_mac):
    subprocess.call(["ip","link","set","dev", interface, "down"])
    subprocess.call(["ip","link","set","dev", interface, "adress", new_mac])
    subprocess.call(["ip","link","set","dev", interface, "up"])

    return  


def main():

    interface, mac = optparser() 
    old_mac        = interfaceMac(interface)[0][0]
    new_mac        = check_and_fix_Inputs(interface, mac)
    macChanger(interface, new_mac)
     
    new_mac_check = interfaceMac(interface)[0][0]
    
    def macCompare():
        print("New MAC:", new_mac_check)
        print("Old MAC:", old_mac)
        return

    if old_mac != new_mac_check:
         print("[*] SUCCESS!")
         macCompare()

    else:
         print("[X] FAILED!")
         print("[!] You probably tried a duplicated MAC")
         macCompare()

main()



        

 




