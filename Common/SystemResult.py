'''
Created on Jun 18, 2015

@author: Alex
'''

class SystemResult(object):
    '''
    classdocs
    '''
    

    def __init__(self, address, os, distance, status, mac):
        '''
        Constructor
        '''
        self.services = []
        self.address = address
        self.os = os
        self.distance = distance
        self.status = status
        self.mac = mac
        
    def addService(self, service):
        self.services.append(service)
    def getServices(self):
        return self.services
    def getAddress(self):
        return self.address