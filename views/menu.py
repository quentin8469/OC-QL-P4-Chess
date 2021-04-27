#!/usr/bin/python
# -*- coding: utf-8 -*-


class Menu:
    """
    In this class we find all the views
    """
    
    def __init__(self):
        """ docting """
        pass
        
    def menu_start(self):
        """ print the start menu """
        print("welcome, please select your action and press Enter")
        print("1.Tournament")
        print("2.player")
        print("3.Report")
        print("Q.Quit the application")
        return input("Your choice: ")
    
    def menu_player(self):
        """ print the Player menu """
        print("welcome, please select your action and press Enter")
        print("1.New player")
        print("2.Modif player")
        print("3.Report")
        print("Q.Return to start menu")
        return input("Your choice: ")
    
    def menu_tournament(self):
        """ print the Tournament menu """
        print("welcome, please select your action and press Enter")
        print("1.New Tournament")
        print("2.Modif Tournament")
        print("3.load Tournament")
        print("4.Report")
        print("Q.Return to start menu")
        return input("Your choice: ")
    
    def new_player_lname(self):
        """ get the player last name """
        return input("Last Name: ")
    
    def new_player_fname(self):
        """ get the player firt name """
        return input("First Name: ")
    
    def new_player_bdate(self):
        """ get the player Birth date """
        return input("Birth date: ")
        
    def new_player_gender(self):
        """ get the player gender """
        return input("Gender: ")
    
    def new_player_elo(self):
        """ get the player Elo """
        return input("Elo: ")