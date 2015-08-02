'''
Created on Aug 2, 2015

@author: Alex
'''

class BaseListener(object):
    '''
    Object listening for scanner results
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def UpdateListener(self, scanResults):
        NotImplementedError("Class %s doesn't implement UpdateListener(scanResults)" % (self.__class__.__name__))