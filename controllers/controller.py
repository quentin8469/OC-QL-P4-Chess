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
        return start.menu_start()