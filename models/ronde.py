#!/usr/bin/python
# -*- coding: utf-8 -*-
#

class Ronde:
    """
    doc string
    """
    #ROUND_MAX = 4
    def __init__(self, name, lmatch):
        """ docting """
        self.name = name
        self.sttime = ""
        self.endtime = ""
        self.lmatch = lmatch
        
        
    def serialized_rounds(self):
        """" serialization for save in TinyDB """
        serialized_rounds = {
            'Ronde': self.name, 
            'Start_time': self.sttime,
            'End_time': self.endtime,
            'Matchs': self.lmatch,
        }
        return serialized_rounds
    '''    
    @classmethod
    def deserializeplayer(cls, rondes):
        """ deserialized rondes from bdd"""
        name = rondes['Ronde']
        "" = rondes ['Start_time']
        "" = rondes ['End_time']
        lmatch = rondes ['Matchs']
        rounds = Ronde(name, lmatch)
        return rounds
    '''