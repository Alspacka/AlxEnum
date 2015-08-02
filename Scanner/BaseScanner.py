'''
Created on Aug 2, 2015

@author: Alex
'''

class BaseScanner(object):
    '''
    Abstract class defining the interface to be used for scanning classes
    '''

    def __init__(self, ip):
        self.listeners = []
        self.ip = ip
        '''
        Constructor
        '''
        
    def SubscribeObserver(self, listener):
        self.listeners.append(listener)
    
    def UnsubscribeObserver(self, listener):
        self.listeners.remove(listener)
    
    def UpdateListeners(self, scanResults):
        for l in enumerate(self.listeners):
            l.UpdateListener(scanResults)
            
    def Execute(self):
        NotImplementedError("Class %s doesn't implement Execute()" % (self.__class__.__name__))
        
    def Quit(self):
        NotImplementedError("Class %s doesn't implement Quit()" % (self.__class__.__name__))
        
    def getIP(self):
        return self.ip