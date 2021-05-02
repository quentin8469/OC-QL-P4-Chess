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
        
    def presentation():
        """ return the tournament infos """
        return
    
    def get_name(self):
        """ add tournament name """
        return self.name
        
    def get_location(self):
        """ add tournament location """
        return self.location

    def get_date(self):
        """ add tournament date """
        return self.date
        
    def get_ronde(self):
        """ add tournament rondes """
        return self.rondes
        
    def get_tournees(self):
        """ add tournament tournees """
        return self.tournees_list

    def get_players(self):
        """ add tournament players_list """
        return self.players_list
        
    def get_timer(self):
        """ add tournament timer """
        return self.timer

    def get_description(self):
        """ add tournament description """
        return self.description