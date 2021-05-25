#!/usr/bin/env/python3


class Player:
    """
    All player informations
    """

    def __init__(self, lastname, firstname, birth_date, gender, elo, score=0.0):
        """ initilisation of a player """
        self.lastname = lastname
        self.firstname = firstname
        self.birth_date = birth_date
        self.gender = gender
        self.elo = elo
        self.score = score

    def serialized_player(self):
        """" serialization for save in TinyDB """
        serialized_player = {
            "Last_name": self.lastname,
            "First_name": self.firstname,
            "Birth_date": self.birth_date,
            "Gender": self.gender,
            "Elo": self.elo,
            "Score": self.score,
        }
        return serialized_player

    @classmethod
    def deserializeplayer(cls, player):
        """ deserialized player from bdd"""
        lastname = player["Last_name"]
        firstname = player["First_name"]
        birth_date = player["Birth_date"]
        gender = player["Gender"]
        elo = player["Elo"]
        score = player["Score"]
        player = Player(lastname, firstname, birth_date, gender, elo, score)
        return player
