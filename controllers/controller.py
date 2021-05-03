#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.joueur import Player
from models.tournoi import Tournament
from tinydb import TinyDB


class Controller:
    """
    This class control the menu views
    """

    def __init__(self, menu):
        """ constructor initialisation """
        self.menu = menu
        self.playerdb = TinyDB('players.json')
        self.player_table = self.playerdb.table('players')
        self.tournamentdb = TinyDB('tournament.json')
        self.tournament_table = self.tournamentdb.table('tournament')
        self.start_menu()
        
    def start_menu(self):
        """ start the view menu_start"""
        self.menu.menu_start()
        input_choice = input()
        input_check_list = ["1", "2", "3", "Q"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [self.tournament_menu, self.player_menu, self.report_menu, "Kiss"]
        menu_list[menu]()

    def player_menu(self):
        """ start the player menu"""
        self.menu.menu_player()
        input_choice = input()
        input_check_list = ["1", "2", "3", "M"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [self.new_player, self.modif_player, self.report, self.start_menu]
        menu_list[menu]()

    def tournament_menu(self):
        """ start the tournament menu"""
        self.menu.menu_tournament()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "M"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [self.new_tournament, self.start_menu, self.start_menu, 
                                               self.start_menu, self.start_menu]
        menu_list[menu]()

    def report_menu(self):
        """ start the report menu"""
        self.menu.menu_report()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "5", "6", "7", "M"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [self.start_menu, self.start_menu, self.start_menu, 
             self.start_menu, self.start_menu, self.start_menu, self.start_menu]
        menu_list[menu]()

    def new_player(self):
        """ Create a new player"""
        self.menu.new_player_lname()
        lastname = input()
        self.menu.new_player_fname()
        firstname = input()
        self.menu.new_player_bdate()
        birth_date = input()
        self.menu.new_player_gender()
        gender = input()
        self.menu.new_player_elo()
        elo = input()
        new_player = Player(lastname, firstname, birth_date, gender, elo)
        self.player_table.insert(new_player.serialized_player())
        self.menu.menu_start()

    def modif_player(self):
        """ modif player data"""
        pass

    def report():
        """ Create en report"""
        pass

    def new_tournament(self):
        """ Create a new player"""
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
        new_tournament = Tournament(name, location, date, rondes, tournees, description)
