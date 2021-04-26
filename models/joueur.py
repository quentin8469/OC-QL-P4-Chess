#!/usr/bin/python
# -*- coding: utf-8 -*-


class Player:
    """
    All player informations
    """
    
    def __init__(self, lastname, firstname, birth_date, gender, elo):
        """ initilisation of a player """
        self.lastname = lastname
        self.firstname = firstname
        self.birth_date = birth_date
        self.gender = gender
        self.elo = elo
    
    def presentation(self):
        """ return the player infos """
        return
	
	def get_lname(self):
	    """ add last name """
		return self.lastname
	
	def get_fname(self):
	    """ add first name """
		return self.firstname