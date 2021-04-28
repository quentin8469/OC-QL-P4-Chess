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
        
    def get_winner(self):
        """ give the point to the winner of the match """
        return
        
    def get_looser(self):
        """ don't give point to the loser of the match """
        return
        
    def get_draw(self):
        """ in case of draw, give 1/2 point for the two player """
        return
        
    def get_result(self):
        """ give the result of the match """
        return