#!/usr/bin/python
# -*- coding: utf-8 -*-


class Tournament:
    """
    All tournament informations
    """
    
    def __init__(self, name, location, date, rondes, tournees, description):
        """ initilisation of a tournament"""
        self.name = name
        self.location = location
        self.date = date
        self.rondes = rondes
        self.tournees_list = tournees
        self.description = description
        
    def serialized_tournament(self):
        """" serialization for save in TinyDB """
        serialized_tournament = {
            'Tournament name': self.name, 
            'Tournament location': self.location,
            'Tournament date': self.date,
            'Tournament rondes': self.rondes,
            'Tournament tournees': self.tournees_list,
            'Tournament description' : self.description,
        }
        return serialized_tournament