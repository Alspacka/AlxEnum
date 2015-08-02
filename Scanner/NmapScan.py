'''
Created on Aug 2, 2015

@author: Alex
'''
from Scanner.BaseScanner import BaseScanner
import subprocess
import multiprocessing
from multiprocessing import Process, Queue
import os
import time 
from Common.AlxConfiguration import AlxConfiguration

class NmapScan(BaseScanner):
    '''
    Nmap scanning class, perform a couple of nmap scans of varying intensity on the specified target and reports this back in the form of ServiceResults and a SystemResult
    '''
    #quickScan = "nmap -sT -A -Pn -p1-15000 -oX "
    quickScan = "nmap -sT -O -Pn -oX "
    #intermediateScan = "nmap -sT -A -Pn -p15001-30000 -T 4 -oX "
    intermediateScan = "nmap -sT -p15001-16000 -T 4 -oX "
    #fullScan = "nmap -sT -A -Pn -p30001-65535 -T 4 -oX "
    fullScan = "nmap -sT -p30001-31000 -T 4 -oX "
    #udpScan = "nmap -vv -Pn -A -sC -sU -T 4 --top-ports 200 -oX "
    udpScan = "nmap -sU -T 4 --top-ports 200 -oX "

    def __init__(self, ip):
        '''
        set params, config, etc
        '''
        super(self.__class__, self).__init__(ip.strip())
        self.config = AlxConfiguration()
        if(self.config.getResultDir().endswith("/")):
            outputfile = self.config.getResultDir() + ip + "."
        else:
            outputfile = self.config.getResultDir() + "/" + ip + "."
        self.FileBase = outputfile
    
    def Execute(self):
        ip = self.getIP()
        quickres = subprocess.check_output(self.quickScan + self.FileBase + "quick " + ip, shell=True)
        self.ParseResults(quickres)
        intres = subprocess.check_output(self.intermediateScan + self.FileBase + "intermediate " + ip, shell=True)
        self.ParseResults(intres)
        udpres= subprocess.check_output(self.udpScan + self.FileBase + "udp " + ip, shell=True)
        self.ParseResults(udpres)
        fullres = subprocess.check_output(self.fullScan + self.FileBase + "full " + ip, shell=True)
        self.ParseResults(fullres)
        pass 
    def Quit(self):
        print("Quitting...")
        pass
    
    def ParseResults(self, results):
        print(results)
        pass