import subprocess
import os
import re
import sys
from colorama import Fore

def space():
    print("\n\n")

def print_logo():
    print(Fore.RED + """
     ____ ____                       _          _
    / ___/ ___|  ___ __ _ _ __      / \   _ __ (_)_  __
    \___ \___ \ / __/ _` | '_ \    / _ \ | '_ \| \ \/ /
     ___) |__) | (_| (_| | | | |  / ___ \| |_) | |>  <
    |____/____/ \___\__,_|_| |_| /_/   \_\ .__/|_/_/\_\ 
                                        |_|
    """ + Fore.RESET)

def input_IP():
    _check_flag = 0
    IP = ""
    while not _check_flag:
        print(Fore.CYAN + "A valid IP address contains 3 dots" + Fore.RESET)
        IP = input(Fore.CYAN + "Insert the IP: " + Fore.RESET)
        _check_flag = re.search("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", IP)
    
    return IP

def print_scan(scan_results):
    print(Fore.RED + "NMAP SCAN:" + Fore.RESET)
    for device in scan_results:
        print(device)


def select_device(_IPs):

        print(Fore.RED + "DEVICES:" + Fore.RESET)
        for ip in _IPs:
            print(ip)

        space()

        _device_nmb = -1
        while _device_nmb < 0 or _device_nmb > len(_IPs)-1:
            _device_nmb = int(input(Fore.CYAN + "Chose the device number [0-" + str(len(_IPs)-1) + "]: " + Fore.RESET))
        
        return _IPs[_device_nmb]



def __main__():

# Controls if the user is with root privileges.
    assert os.geteuid() == 0, Fore.RED + "\n\n[!] You have to run this script as root!\n[i] README.md for help" + Fore.RESET

    print_logo()

    IP = input_IP()

    CIDR = -1
    while CIDR < 0 or CIDR > 32:
        print(Fore.CYAN + "Insert 0 if you want to scan a single device")
        CIDR = int(input(Fore.CYAN + "Insert the CIDR number: " + Fore.RESET))

    if CIDR == 0:
        command = f"nmap -sn {IP}"
    else:
        command = f"nmap -sn {IP}/{CIDR}"

    space()

    _scan_result_str = subprocess.run(["sudo", "bash", "-c", command], capture_output=True, text=True)
    _filtered_result = _scan_result_str.stdout.split("\n")

    _gold = []
    _IPs = []

    for s in _filtered_result:
        if "MAC" in s:
            _gold.append(Fore.GREEN + s + "\n" + Fore.RESET)
        elif "Nmap scan report" in s:
            try:
                _IPs.append(str(len(_IPs)) + ": " + s.split(" ")[5].replace(")", "").replace("(", ""))
            except Exception as e:
                print("", end="") 
            _gold.append(Fore.BLUE + s + Fore.RESET)

    print_scan(_gold)

    space()

    if len(_IPs) == 0:
        print(Fore.RED + "No devices found... Closing..." + Fore.RESET)
        quit()

    if CIDR > 0:
        IP = select_device(_IPs)

if __name__ == "__main__":
    __main__()


