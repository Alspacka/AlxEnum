'''
Created on Jun 18, 2015

@author: Alexander Van Daele
'''

from ScanModules import *
from Common import *
import imp
import os
from Scanner.BaseListener import BaseListener
from Scanner.NmapScan import NmapScan

PluginFolder = "../ScanModules"

class MainScanner(BaseListener):
    '''
    Main scanner class, performs a scan and launches additional specific modules based on open ports found.
    '''

    def __init__(self, ips = []):
        '''
        Set scanner, set listener, import scan modules
        '''
        
        self.Scanners = []
        
        for ip in ips:
            ns = NmapScan(ip)
            ns.SubscribeObserver(self)
            self.Scanners.append(ns)
        
    def Execute(self):
        for s in self.Scanners:
            print("[*] Starting scan against {0}").format(s.getIP())
            s.Execute()
    
    def Quit(self):
        for s in self.Scanners:
            print("[-] Stopping scan against {0}").format(s.getIP())
            s.Quit()
    
    def UpdateListener(self, scanResults):
        '''
        Received some scanning results, pass to individual scanning modules
        '''
        pass
    
    