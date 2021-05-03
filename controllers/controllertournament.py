#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.tournoi import Tournament
from models.match import Match
from models.ronde import Ronde
from tinydb import TinyDB

class TournamentController:
    """
    All tt controlles
    """
	
	def __init__(self, menu):
	    """ constructor controller tt"""
		self.menu = menu
        self.tournamentdb = TinyDB('tournament.json')
        self.tournament_table = self.tournamentdb.table('tournament')