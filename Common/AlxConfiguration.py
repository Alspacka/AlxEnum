'''
Created on Jun 18, 2015

@author: Alex
'''

class AlxConfiguration(object):
    '''
    Singleton object responsible for reading/writing the configuration
    '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AlxConfiguration, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        '''
        Read XML file and set variables
        '''
        self.interface = "eth0"
        self.BasicBruteforceUSER = "/tmp/bla"
        self.BasicBruteforcePASS = "/tmp/bla"
        self.DeepBruteforceUSER = "/tmp/test"
        self.DeepBruteforcePASS = "/tmp/test"
        self.ResultDir = "/tmp/resulttest"
    
    def getInterface(self):
        return self.interface
    def setInterface(self, interface):
        self.interface = interface
        self.Save()
    def getBasicBruteforceUSER(self):
        return self.BasicBruteforceUSER
    def setBasicBruteforceUSER(self, filepath):
        self.BasicBruteforceUSER = filepath
        self.Save()
    def getBasicBruteforcePASS(self):
        return self.BasicBruteforcePASS
    def setBasicBruteforcePASS(self, filepath):
        self.BasicBruteforcePASS = filepath
        self.Save()
    def getDeepBruteforceUSER(self):
        return self.DeepBruteforceUSER
    def setDeepBruteforceUSER(self, filepath):
        self.DeepBruteforceUSER = filepath
        self.Save()
    def getDeepBruteforcePASS(self):
        return self.DeepBruteforcePASS
    def setDeepBruteforcePASS(self, filepath):
        self.DeepBruteforcePASS = filepath
        self.Save()
    def getResultDir(self):
        return self.ResultDir
    def setResultDir(self, directory):
        self.ResultDir = directory
        self.Save()
    def Save(self):
        pass