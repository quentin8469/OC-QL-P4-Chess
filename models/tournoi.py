#!/usr/bin/python
# -*- coding: utf-8 -*-


class Tournament:
    """
    All tournament informations
    """
    
    def __init__(self, name, location, st_date, end_date, description):
        """ initilisation of a tournament"""
        self.name = name
        self.location = location
        self.start_date = st_date
        self.end_date = end_date
        self.rondes = 4
        self.tournees_list = ()
        self.players = []
        self.time_control = []
        self.description = description
        
    def serialized_tournament(self):
        """" serialization for save in TinyDB """
        serialized_tournament = {
            'Tournament_name': self.name, 
            'Tournament_location': self.location,
            'Tournament_start_date': self.start_date,
            'Tournament_end_date': self.end_date,
            'Tournament_rondes': self.rondes,
            'Tournament_tournees': self.tournees_list,
            'Tournament_players' : self.players
            'Tournament_Tcontrol' : self.time_control
            'Tournament_description' : self.description,
        }
        return serialized_tournament