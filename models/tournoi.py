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
            'Tournament_name': self.name, 
            'Tournament_location': self.location,
            'Tournament_date': self.date,
            'Tournament_rondes': self.rondes,
            'Tournament_tournees': self.tournees_list,
            'Tournament_description' : self.description,
        }
        return serialized_tournament