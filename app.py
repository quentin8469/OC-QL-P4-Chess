#!/usr/bin/python
# -*- coding: utf-8 -*-
from controllers.controller import Controller
from controllers.controllerplayer import PlayerController
from controllers.controllertournament import TournamentController
from views.menu import Menu



if __name__ == "__main__":
    view = Menu()
    #start = Controller(view)
    #player = PlayerController(view)
    tournament= TournamentController(view)