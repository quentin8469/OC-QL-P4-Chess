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
        self.score = 0.0
    
    
    def serialized_player(self):
        """" serialization for save in TinyDB """
        serialized_player = {
            'Last_name': self.lastname, 
            'First_name': self.firstname,
            'Birth_date': self.birth_date,
            'Gender': self.gender,
            'Elo' : self.elo,
            'Score' : self.score
        }
        return serialized_player