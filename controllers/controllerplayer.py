#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.joueur import Player
from tinydb import TinyDB, Query


class PlayerController:
    """
    All player controlles
    """

    def __init__(self, menu):
        """ constructor controller player"""
        self.menu = menu
        self.playerdb = TinyDB("players2.json")
        self.playerquery = Query()
        self.player_table = self.playerdb.table("players2")
        self.player_menu()
        #self.dict_choice()
    '''
    def player_menu(self):
        """ start the player menu"""
        self.menu.menu_player()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "5"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [
            self.new_player,
            self.edit_player,
            self.players_list,
            self.search_player,
            self.start_menu,
        ]
        menu_list[menu]()
    '''
        
    def player_menu(self):
        """ start the player menu"""
        #print("test")
        self.menu.menu_player()
        input_choice = input()        
        bob = {
            "1": self.new_player(),
            "2": self.edit_player(),
            "3": self.players_list(),
            "4": self.search_player(),
            "5": self.update_player(),
            "6": self.menu.menu_start(),
        }
        #bob.get(input_choice, 0)
        bob[input_choice]()
    

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
        self.player_menu()

    def edit_player(self):
        """  edit player Elo"""
        self.menu.new_player_lname()
        input_player = input()
        self.menu.new_player_elo()
        input_elo = input()
        self.player_table.update({'Elo': input_elo},
                                self.playerquery.Last_name == f'{input_player}')
        self.player_menu()

    def players_list(self):
        """ Create a list of all players"""

        players = self.player_table.all()
        for player in players:
            self.menu.player_list(player)
        self.player_menu()

    def player_alpha_order(self):
        """ List of the player in alphabetique order"""
        
        players = self.player_table.all()
        alpha_order = sorted(players,key=lambda x:x['Last_name'])
        for alpha in alpha_order:
            self.menu.player_list(alpha)
        self.report_menu()        

    def player_classement_order(self):
        """ List of the player in classement order"""
        players = self.player_table.all()
        classe_order = sorted(players,key=lambda x:x['Elo'], reverse=True)
        for classse in classe_order:
            self.menu.player_list(classse)
        self.report_menu()

    def search_player(self):
        """ serch player"""
        self.menu.new_player_lname()
        input_player = input()
        player = self.player_table.search(self.playerquery.Last_name 
                                                           == f'{input_player}')
        for play in player:
            self.menu.player_search(play)
        self.player_menu()
        
