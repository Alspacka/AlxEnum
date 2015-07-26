#!/usr/bin/python
'''
Created on Dec 13, 2014

@author: Alexander Van Daele
'''

import Scanner.MainScanner
from Common import CheckRequirements

CheckRequirements.CheckEnvironment(["nmap","hydra","dirb", "nikto","enum4linux","onesixtyone"])
Scanner.MainScanner.MainScanner.execute()