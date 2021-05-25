#!/usr/bin/env/python3


from controllers.controllerplayer import PlayerController
from controllers.controllertournament import TournamentController
from controllers.controllerchess import ControllerChess

if __name__ == "__main__":
    players = PlayerController()
    tournoi = TournamentController()
    start = ControllerChess(players, tournoi)
