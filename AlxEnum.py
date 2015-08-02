#!/usr/bin/python
'''
Created on Dec 13, 2014

@author: Alexander Van Daele
'''

import Scanner.MainScanner
from Common import CheckRequirements

banner = """
**************************************************
* AlxEnum 0.1                                    
* Written by Alexander Van Daele                 
* Please use responsibly
**************************************************
"""

print(banner)

print("[!] Checking requirements...")
#CheckRequirements.CheckEnvironment(["nmap","hydra","dirb", "nikto","enum4linux","onesixtyone"])

#Setup scanner, read config etc

Scanner.MainScanner.MainScanner.execute()