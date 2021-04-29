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
        self.choice_menu_start(input_choice)
    
    def player_menu(self):
       """ start the player menu"""
       self.menu.menu_player()
       input_choice = input("Your choice: ")
       self.choice_menu_player(input_choice)

    def tournament_menu(self):
       """ start the player menu"""
       self.menu.menu_tournament()
       input_choice = input("Your choice: ")
       self.choice_menu_tournament(input_choice)

    def report_menu(self):
       """ start the player menu"""
       self.menu.menu_report()
       input_choice = input("Your choice: ")
       self.choice_menu_report(input_choice)

    def choice_menu_start(self, input_choice):
       """ navigate in the view menu_start"""
       if input_choice == "1":
           self.tournament_menu()          
       if input_choice == "2":
           self.player_menu()
       if input_choice == "3":
           self.report_menu()
       if input_choice == "Q":
           pass
    
    def choice_menu_player(self, input_choice):
       """ navigate in the view menu_player"""
       if input_choice == "1":
           pass         
       if input_choice == "2":
           pass
       if input_choice == "3":
           pass
       if input_choice == "M":
           self.start_menu()
    
    def choice_menu_tournament(self, input_choice):
       """ navigate in the view menu_tournament"""
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
       """ navigate in the view menu_report"""
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