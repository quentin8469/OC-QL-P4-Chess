#!/usr/bin/python
# -*- coding: utf-8 -*-


class Menu:
    """
    In this class we find all the views
    """
    
    def __init__(self):
        """ docting """
        pass
    # menu creation    
    def menu_start(self):
        """ print the start menu """
        print("--------- Start Menu ---------")
        print("welcome, please select your action and press Enter")
        print("1.Tournament")
        print("2.player")
        print("3.Report")
        print("Q.Quit the application")
        print("Choose your action please")
        print("------------------------------")
        
    
    def menu_player(self):
        """ print the Player menu """
        print("--------- Player Menu ---------")
        print("welcome, please select your action and press Enter")
        print("1.New player")
        print("2.Edit player")
        print("3.Player list")
        print("4.Player search")
        print("5.Player update")
        print("6.Return to start menu")
        print("-------------------------------")
        
    
    def menu_tournament(self):
        """ print the Tournament menu """
        print("--------- Tournament Menu ---------")
        print("welcome, please select your action and press Enter")
        print("1.New Tournament")
        print("2.Edit Tournament")
        print("3.List of Tournament")
        print("4.load Tournament")
        print("5.Report")
        print("6.Return to start menu")
        print("-----------------------------------")
        
    
    def menu_report(self):
        """ print the report menu """
        print("--------- Report Menu ---------")
        print("welcome, please select your action and press Enter")
        print("List of all actors:")
        print("    1. Alphabetique order")
        print("    2. Classement order")
        print("List of all player for one tournament:")
        print("    3. Alphabetique order")
        print("    4. Classement order")
        print("5.List of all tournaments")
        print("6.List of all rondes in a tournament")
        print("7.List of all matchs in a tournament")
        print("M.Return to start menu")
        print("-------------------------------")
        
    # Player creation actions

    def new_player_number(self):
        """ give number of player you want add"""
        print("Number of players you want add: ")
    
    def new_player_lname(self):
        """ get the player last name """
        print("Last Name: ")
    
    def new_player_fname(self):
        """ get the player firt name """
        print("First Name: ")
    
    def new_player_bdate(self):
        """ get the player Birth date """
        print("Birth date: ")
        
    def new_player_gender(self):
        """ get the player gender """
        print("Gender: ")
    
    def new_player_elo(self):
        """ get the player Elo """
        print("Elo: ")
    
    def player_list(self, player):
        """ give the liste of the players"""
        
        print("---------------------------------")
        print("doc_id:", player.doc_id)
        print("Last name:", player["Last name"])
        print("First name:", player["First name"])
        print("Birth date:", player["Birth date"])
        print("Gender:", player["Gender"])
        print("Elo:", player["Elo"])
        print("---------------------------------")
        
    def edit_player(self):
        """ menu to chioce the action editting player"""
        print("---------------------------------")
        print("1.Edit elo player")
        print("2.del player")
        print("3.Return to start menu")
        print("---------------------------------")
  
        
    # Tournament creation actions    
    def new_tournament_name(self):
        """ get the tournament name"""
        print("Tournament name: ")
    
    def new_tournament_location(self):
        """ get the tournament location"""
        print("Tournament location: ")
    
    def new_tournament_date(self):
        """ get the tournament date"""
        print("Tournament date: ")
    
    def new_tournament_rondes(self):
        """ get the tournament rondes"""
        print("Tournament rondes: ")
    
    def new_tournament_tournees(self):
        """ get the tournament tournees"""
        print("Tournament tournees: ")
    
    def new_tournament_player(self):
        """ get the tournament player"""
        print("Tournament player: ")
    
    def new_tournament_timer(self):
        """ get the tournament timer"""
        print("Tournament timer: ")
    
    def new_tournament_description(self):
        """ get the tournament location"""
        print("Tournament description: ")
    
    def tournament_list(self, tournament):
        """ give the liste of the tournament"""
        
        print("--------Liste des tournoi--------")
        print("doc_id:", tournament.doc_id)
        print("Tournament name:", tournament["Tournament name"])
        print("Tournament location:", tournament["Tournament location"])
        print("Tournament date:", tournament["Tournament date"])
        print("Tournament rondes:", tournament["Tournament rondes"])
        print("Tournament tournees:", tournament["Tournament tournees"])
        print("Tournament description:", tournament["Tournament description"])
        print("---------------------------------")
    # report action
    