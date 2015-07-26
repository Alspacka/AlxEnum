'''
Created on Dec 13, 2014

@author: Alex
'''

from distutils.spawn import find_executable
import sys

def CheckEnvironment(requirements = []):
    for req in requirements:
        if not find_executable(req):
            print("[!] Requirement not found: " + req)
            sys.exit(1)
        else:
            pass