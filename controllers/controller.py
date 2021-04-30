#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.joueur import Player

class Controller:
    """
    This class control the menu views
    """
    
    def __init__(self, menu):
        """ constructor initialisation """
        self.menu = menu
        self.start_menu()
    
    def start_menu(self):
        """ start the view menu_start"""
        self.menu.menu_start()       
        input_choice = input("Your choice: ")
        self.choice_menu_start(input_choice)
    
    def player_menu(self):
       """ start the player menu"""
       self.menu.menu_player()
       input_choice = input("Your choice: ")
       self.choice_menu_player(input_choice)

    def tournament_menu(self):
       """ start the tournament menu"""
       self.menu.menu_tournament()
       input_choice = input("Your choice: ")
       self.choice_menu_tournament(input_choice)

    def report_menu(self):
       """ start the report menu"""
       self.menu.menu_report()
       input_choice = input("Your choice: ")
       self.choice_menu_report(input_choice)

    def choice_menu_start(self, input_choice):
       """ navigate in the menu_start"""
       if input_choice == "1":
           self.tournament_menu()          
       if input_choice == "2":
           self.player_menu()
       if input_choice == "3":
           self.report_menu()
       if input_choice == "Q":
           pass
    
    def choice_menu_player(self, input_choice):
       """ navigate in the menu_player"""
       if input_choice == "1":
           # New player
           self.new_player()          
       if input_choice == "2":
           # Modif player
           #self.modif_player()
           pass
       if input_choice == "3":
           # Report
           #self.report()
           pass
       if input_choice == "M":
           # Return start menu
           self.start_menu()
    
    def choice_menu_tournament(self, input_choice):
       """ navigate in the menu_tournament"""
       if input_choice == "1":
           pass         
       if input_choice == "2":
           pass
       if input_choice == "3":
           pass
       if input_choice == "4":
           pass
       if input_choice == "M":
           self.start_menu()
           
    def choice_menu_report(self, input_choice):
       """ navigate in the menu_report"""
       if input_choice == "1":
           pass         
       if input_choice == "2":
           pass
       if input_choice == "3":
           pass
       if input_choice == "4":
           pass
       if input_choice == "5":
           pass
       if input_choice == "6":
           pass
       if input_choice == "7":
           pass
       if input_choice == "M":
           self.start_menu()
    
    def new_player(self):
        """ Create a new player"""
        lastname = self.menu.new_player_lname()
        firstname = self.menu.new_player_fname()
        birth_date = self.menu.new_player_bdate()
        gender = self.menu.new_player_gender()
        elo = self.menu.new_player_elo()
        new_player = Player(lastname, firstname, birth_date, gender,elo)
        
        
    
    def modif_player(self):
        """ modif player data"""
        pass
    
    def report():
        """ Create en report"""
        pass
    