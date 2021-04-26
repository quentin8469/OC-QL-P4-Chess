#!/usr/bin/python
# -*- coding: utf-8 -*-


class Joueur:
    """
    doc string
    """
    
    def __init__(self,lastname, firstname, birth_date, gender, elo):
        """ docting """
		self.lastname = lastname
		self.firstname = firstname
		self.birth_date = birth_date
		self.gender = gender
		self.elo = elo
        pass