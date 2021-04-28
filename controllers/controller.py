#!/usr/bin/python
# -*- coding: utf-8 -*-

from views.menu import Menu
# from ..models import joueur, match, ronde, tournoi


class Controller:
    """
    doc string
    """
    
    def __init__(self):
        """ docting """
        pass
    
    def start(self):
        """ start the view menu_start"""
        start = Menu()
        start.menu_start()
        test = input("Your choice: ")
        if test == "1":
           start.menu_tournament()
        if test == "2":
           start.menu_player()
        if test == "3":
           start.menu_report()
        if test == "M":
           start.menu_start()
        
    '''    
    def choice_menu(self):
       """ doc string"""
       choice = start.menu_start()
       start.menu_start()
       test = input("Your choice: ")
       if test == 1:
           start.menu_player()
    '''