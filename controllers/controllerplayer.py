#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.joueur import Player
from tinydb import TinyDB

class PlayerController:
    """
    All player controlles
    """
    
    def __init__(self, menu):
        """ constructor controller player"""
        self.menu = menu
        self.playerdb = TinyDB('players.json')
        self.player_table = self.playerdb.table('players')
        self.player_menu()
    
    def player_menu(self):
        """ start the player menu"""
        self.menu.menu_player()
        input_choice = input()
        input_check_list = ["1", "2", "3", "M"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [self.new_player, self.modif_player, self.report]
        menu_list[menu]()
    
    '''
    def player_menu(self):
        """ start the player menu"""
        self.menu.menu_player()        
        input_dict = {
            "1": self.new_player(),
            "2": self.modif_player(),
            "3": self.report(),
            "4": "Au revoir",
        }
        input = 0
        while (input != 4):
            input =int(input())
            if (input >=0 and input <4):
                input_dict[input]()
    '''    

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

    def modif_player(self):
        """ modif player data"""
        pass

    def report(self):
        """ Create en report"""
        
        results = self.player_table.all()
        for player in results:
            self.menu.player_list(player)  