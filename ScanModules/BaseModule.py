'''
Created on Jun 18, 2015

@author: Alex
'''

class BaseModule(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def getPorts(self):
        NotImplementedError("Class %s doesn't implement getPorts()" % (self.__class__.__name__))