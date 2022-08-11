# MacSpoofing-Linux
Linux pentest tool to change temporally the MAC Address of a network interface. 

College work done in April/May for programming logic and python modules learning, so it has low optimization and some "bad habits" on the programming logic. Basically my first "true" software.

-i or --interface=  : network interface
-m or --mac=        : new mac address

# Features
# [1] Format the input MAC if doesnt have any special characters after each 2 digits
# [2] Format the input MAC if the special characters after each 2 digits is not ":"
# [3] Mistakes generate a output with available network interfaces and their current MAC Addresses
# [4] "Error Handling" if doesnt work

# Future Improvements 
# [1] Check if root, because you need it to change the MAC.
# [2] Random MAC Generator so user doesnt need to input it.
# [3] Programming Logic improvements.
