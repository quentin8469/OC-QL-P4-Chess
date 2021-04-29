#!/usr/bin/python
# -*- coding: utf-8 -*-


class Controller:
    """
    doc string
    """
    
    def __init__(self, menu):
        """ docting """
        self.menu = menu
        self.start_menu()
    
    def start_menu(self):
        """ start the view menu_start"""
        self.menu.menu_start()       
        input_choice = input("Your choice: ")
        self.choice_menu(input_choice)
    
    def player_menu(self):
       """ start the player menu"""
       self.menu.menu_player()
    
    def tournament_menu(self):
       """ start the player menu"""
       self.menu.menu_tournament()

    def report_menu(self):
       """ start the player menu"""
       self.menu.menu_report()
           
    def choice_menu(self, input_choice):
       """ navigate in the view menu_start"""
       if input_choice == "1":
           self.tournament_menu()          
       if input_choice == "2":
           self.player_menu()
       if input_choice == "3":
           self.report_menu()
       if input_choice == "Q":
           pass 