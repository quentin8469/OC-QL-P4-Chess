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
    
    def player_menu(self):
       """ start the player menu"""
       self.menu.menu_player()
    
    def tournament_menu(self):
       """ start the player menu"""
       self.menu.menu_tournament()

    def report_menu(self):
       """ start the player menu"""
       self.menu.menu_report()
    	   
    def choice_menu(self):
       """ doc string"""
       choice = start.menu_start()
       start.menu_start()
       test = input("Your choice: ")
       if test == 1:
           start.menu_player()
    