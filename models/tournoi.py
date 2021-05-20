#!/usr/bin/python
# -*- coding: utf-8 -*-


class Tournament:
    """
    All tournament informations
    """
    
    def __init__(self, name, location, st_date, e_date, rondes, tt_list, pl_list, ttc, description):
        """ initilisation of a tournament"""
        self.name = name
        self.location = location
        self.start_date = st_date
        self.end_date = e_date
        self.rondes = rondes
        self.tournees_list = tt_list
        self.tt_players = pl_list
        self.time_control = ttc
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
            'Tournament_players' : self.tt_players,
            'Tournament_Tcontrol' : self.time_control,
            'Tournament_description' : self.description,
        }
        return serialized_tournament
        
    @classmethod
    def deserializett(cls, tt):
        """ deserialized tournament from bdd"""
        name = tt['Tournament_name']
        location = tt['Tournament_location']
        st_date = tt['Tournament_start_date']
        e_date = tt['Tournament_end_date']
        rondes = tt['Tournament_rondes']
        tt_list = tt['Tournament_tournees']
        pl_list = tt['Tournament_players']
        ttc = tt['Tournament_Tcontrol']
        description = tt['Tournament_description']
       
        tournament = Tournament(name, location, st_date, e_date,rondes, tt_list, pl_list, ttc, description)
        
        return tournament
    
    def add_player(self, player):
        """ add player in tt_players """
        self.tt_players.append(player)