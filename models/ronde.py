#!/usr/bin/env/python3


class Ronde:
    """
    Rondes informations
    """

    def __init__(self, name, lmatch, sttime, endtime):
        """ initialisation of a ronde """
        self.name = name
        self.lmatch = lmatch
        self.sttime = sttime
        self.endtime = endtime

    def serialized_rounds(self):
        """" serialization for save in TinyDB """
        serialized_rounds = {
            "Ronde": self.name,
            "Start_time": self.sttime,
            "End_time": self.endtime,
            "Matchs": self.lmatch,
        }
        return serialized_rounds

    @classmethod
    def deserializeplayer(cls, rondes):
        """ deserialized rondes from bdd"""
        name = rondes["Ronde"]
        lmatch = rondes["Matchs"]
        sttime = rondes["Start_time"]
        endtime = rondes["End_time"]
        rounds = Ronde(name, lmatch, sttime, endtime)
        return rounds
