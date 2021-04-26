#!/usr/bin/python
# -*- coding: utf-8 -*-


class Match:
    """
    Create Match
    """
    
    def __init__(self, player1, player2):
        """ initialisation of a match """
        self.player1 = player1
        self.player2 = player2
    
    def get_color(self):
        """ give the color white or black to a player"""
        return