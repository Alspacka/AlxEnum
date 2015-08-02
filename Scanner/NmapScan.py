'''
Created on Aug 2, 2015

@author: Alex
'''
from Scanner.BaseScanner import BaseScanner
import subprocess
from Common.AlxConfiguration import AlxConfiguration
from libnmap.process import NmapProcess
from time import sleep
from pyparsing import ParseResults
import threading
from Queue import Queue

class NmapScan(BaseScanner):
    '''
    Nmap scanning class, perform a couple of nmap scans of varying intensity on the specified target and reports this back in the form of ServiceResults and a SystemResult
    '''

    def __init__(self, ip, directory):
        '''
        set params, config, etc
        '''
        super(self.__class__, self).__init__(ip.strip())
        
        if(directory.endswith("/")):
            outputfile = directory + ip + "."
        else:
            outputfile = directory + "/" + ip + "."
        self.FileBase = outputfile
        c = AlxConfiguration()
        self.currentScan = None
        self.interval = 5
        self.timer = None
        self.running= False
        self.hasQuit = False
        q = Queue()
        q.put(c.getQuickScanOpts())
        q.put(c.getIntermediateScanOpts())
        q.put(c.getUdpScanOpts())
        q.put(c.getFullScanOpts())
        
        self.scanQueue = q
        
    
    def Execute(self):
        #Start nmap in different thread
        if not self.running:
            self.timer = threading.Timer(self.interval, self._run)
            self.timer.start()
            self.running = True
 
    def Quit(self):
        print("Quitting scan against {0}...").format(self.getIP())
        self.timer.cancel()
        self.running = False
        self.timer = None
        self.hasQuit = True
    
    def _run(self):
        if(self.running):
            self.running = False
            self.runNmap()
            if(not self.hasQuit):
                self.Execute()
    
    def runNmap(self):
        #gets executed every x seconds
        #check current nmap scan -> if finished then parse results and start new one, otherwise wait and report status
        
        if not self.currentScan:
            #create new scan
            self.createNewScan()
        else:
            #report current scan status
            if(self.currentScan.is_running()):
                print("Nmap scan for {0} ({2}) progress: {1}%").format(self.getIP(), self.currentScan.progress, self.currentScan.options)
                pass
            else:
                if(self.currentScan.is_successful()):
                    print("RECEIVED NMAP RESULTS!")
                    self.currentScan = None
                self.createNewScan()
            pass
        
        
    def createNewScan(self):
        if self.scanQueue and not self.scanQueue.empty():
            opt = self.scanQueue.get()
            ip = self.getIP()
            print("Starting Nmap scan against {0} with options {1}").format(ip,opt)
            self.currentScan = NmapProcess(targets=ip, options=opt, event_callback=ParseResults, safe_mode=False)
            self.currentScan.run_background()
        else:
            self.Quit()

    
    def ParseResults(self, results):
        print("RECEIVED NMAP RESULTS!")
    
    