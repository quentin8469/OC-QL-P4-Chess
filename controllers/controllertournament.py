#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.tournoi import Tournament
from models.match import Match
from models.ronde import Ronde
from tinydb import TinyDB, Query

class TournamentController:
    """
    All tt controlles
    """
    
    def __init__(self, menu):
        """ constructor controller tt"""
        self.menu = menu
        self.tournamentdb = TinyDB('tournament1.json')
        self.tournamentquery = Query()
        self.tournament_table = self.tournamentdb.table('tournament1')
        self.tournament_menu()

    def tournament_menu(self):
        """ start the tournament menu"""
        self.menu.menu_tournament()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "5", "6"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [self.new_tt, self.edit_tt, self.tt_list, self.load_tt, 
                                           self.report_tt, self.menu.menu_start]
        menu_list[menu]()
    
    def new_tt(self):
        """ doc """
        self.menu.new_tournament_name()
        name = input()
        self.menu.new_tournament_location()
        location = input()
        self.menu.new_tournament_date()
        date = input()
        self.menu.new_tournament_rondes()
        rondes = input()
        self.menu.new_tournament_tournees()
        tournees = input()
        self.menu.new_tournament_description()
        description = input()
        new_tournament = Tournament(name, location, date, rondes, tournees, 
                                                                    description)
        self.tournament_table.insert(new_tournament.serialized_tournament())
        self.tournament_menu()
    
    def edit_tt(self):
        """ doc """
        pass
    
    def tt_list(self):
        """ doc """
        tournaments = self.tournament_table.all()
        for tournament in tournaments:
            self.menu.tournament_list(tournament)
        self.tournament_menu()
    
    def load_tt(self):
        """ doc """
        pass
    
    def report_tt(self):
        """ doc """
        pass
    
    
