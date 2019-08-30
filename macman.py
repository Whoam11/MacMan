#!/usr/bin/python

import os
import termcolor
import time


def change_mac(interf, mac):
#Sending commands to change the mac address
     
     os.system("ifconfig " + interf + " down")
     print "[+] Interface Down"
     os.system("ifconfig " + interf + " hw" + " ether " + mac )
     print "[+] Mac address got changed!"
     os.system("ifconfig " + interf + " up")
     print "[+] Interface Up!"




def main():

   print termcolor.colored("MacMan - Mac Address Changer", "green")
   time.sleep(2)
   print termcolor.colored("[!] Make sure to run it as root!", "red")
   getin = termcolor.colored("[*] Enter Interface To Change Mac Addres On: ", "blue")
   interface = raw_input(getin)
   mc = termcolor.colored("[*] Enter Mac Address To change To: ", "blue")
   new_mac_ad = raw_input(mc)
   
   

   bf = os.system("ifconfig " + interface)
   change_mac(interface,new_mac_ad)
   termcolor.colored("[*] Checking New Mac Address", "blue")
   after = os.system("ifconfig " + interface)
   
   
   if bf == after:
        termcolor.colored("[!] Failed To Change Mac Address", "blue")
   else:
        termcolor.colored("[+] Mac Address Got Change With New Mac " + new_mac + " Address!")
        
main()
   
