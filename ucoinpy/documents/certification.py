'''
Created on 2 déc. 2014

@author: inso
'''
from . import Document


class SelfCertification(Document):
    '''
    A document discribing a self certification.
    '''

    def __init__(self, identifier):
        self.identifier = identifier
        self.timestamp = timestamp
        
    @classmethod
    def from_raw(cls, raw):
        #TODO : Parsing
        return cls()

     def ts(self):
        return "META:TS:{0}".format(self.timestamp)
        
    def uid(self):
        return "UID:{0}".format(self.identifier)

    def content(self):
        return "{0}\n{1}".format(self.uid(), self.ts())


class Certification(Document):
    '''
    classdocs
    '''

    def __init__(self, selfcert, blockid):
        '''
        Constructor
        '''
        self.selfcert = selfcert
        self.blockid = blockid

        
    @classmethod
    def from_raw(cls, raw):
        #TODO : Parsing
        return cls()

    def ts(self):
        return "META:TS:{0}".format(self.blockid)

    def content(self):
        return "{0}\n{1}".format(self.selfcert.content(), self.ts())