#!/usr/bin/python
# -*- coding: utf-8 -*-


class Menu:
    """
    doc string
    """
    
    def __init__(self):
        """ docting """
        pass
        
    def menu_choice(self):
        """ print the menu choices """
        print("welcome, please select your action and press Enter")
        print("1.New Tournament")
        print("2.Add player")
        print("3.Report")
        print("4.load Tournament")
        print("5.Modif player")
        print("Q.Quit the application")
        return input("Your choice: ")