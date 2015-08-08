'''
Created on Jun 18, 2015

@author: Alexander Van Daele
'''

from ScanModules import *
from Common import *
import imp
import os
from Common import AlxConfiguration
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
        Config = AlxConfiguration.AlxConfiguration()
        
        for ip in ips:
            directory = Config.getResultDir() + "/Alx_Result_" + ip + "/"
            if not os.path.exists(directory):
                os.makedirs(directory)
            ns = NmapScan(ip, directory)
            ns.SubscribeObserver(self)
            self.Scanners.append(ns)
        
    def Execute(self):
        for s in self.Scanners:
            print("[*] Starting vulnerability scan against {0}").format(s.getIP())
            s.Execute()
    
    def Quit(self):
        for s in self.Scanners:
            print("[-] Stopping scan against {0}").format(s.getIP())
            s.Quit()
    
    def UpdateListener(self, scanResults):
        '''
        Received some scanning results, pass to individual scanning modules
        '''
        print("Received an update from internal scanner")
        for s in scanResults:
            print("Incoming scan results for host {0} containing {1} open services".format(s.getAddress(), len(s.getServices())))
    
    