# Author      : Kavish Gour
#
# Email       : kavishgr@protonmail.com // kavishgour1@gmail.com
#
# Description : Print the system's memory usage, and if usage is >= 90% print a warning. 
#               Can be executed as ad-hoc command for Ansible tasks.
#
# Usage       : python3 memusage.py
#               

#######################################################################################################
#                                         IMPORTS                                                     #
#######################################################################################################

import subprocess as sp
import psutil
import socket

mem = psutil.virtual_memory()
total = mem.total >> 20
available_mem = mem.available >> 20
percent_mem = str(mem.percent)

#######################################################################################################
#                                         FUNCTIONS                                                   #
#######################################################################################################

def host_id():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    print(f"Hostname: {hostname}")
    print(f"IP: {ip}")

    if psutil.OSX:
        osx = sp.getoutput("system_profiler SPSoftwareDataType | grep -e 'System Version'").lstrip().strip("System Version")
        print(f"Operating System{osx}")

    elif psutil.LINUX:
        linux = sp.getoutput('cat /etc/os-release | grep -i pretty | cut -d "=" -f 2').strip('"')
        print(f"Operating System: {linux}")

def mem_ok():
    print (str(available_mem) + " MB of memory available.")
    print (percent_mem + "% percent of memory in use.")

def mem_not_ok():
    print ('''WARNING!!!
              Memory is running OUT!
           ''')
    print (percent + "% percent of memory in use.")


host_id()
print(f"{total} MB of System Memory")

if mem.percent < 90:
    mem_ok()

elif mem.percent >= 90:
    mem_not_ok()
