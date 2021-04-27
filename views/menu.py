#!/usr/bin/python
# -*- coding: utf-8 -*-


class Menu:
    """
    doc string
    """
    
    def __init__(self):
        """ docting """
        pass
        
    def menu_start(self):
        """ print the start menu """
        print("welcome, please select your action and press Enter")
        print("1.New Tournament")
        print("2.Add player")
        print("3.Report")
        print("4.load Tournament")
        print("5.Modif player")
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
    
