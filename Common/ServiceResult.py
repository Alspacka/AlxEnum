'''
Created on Jun 18, 2015

@author: Alex
'''

class ServiceResult(object):
    '''
    Class for the services found on a host
    '''


    def __init__(self, port, protocol, reason, servicename, state, banner):
        '''
        Constructor
        '''
        self.port = port
        self.protocol = protocol
        self.reason = reason
        self.servicename = servicename
        self.banner = banner
        self.state = state