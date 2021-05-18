#!/usr/bin/python
# -*- coding: utf-8 -*-
#from controllers.controller import Controller
from controllers.controllerv2 import Controllerv2
from controllers.controllerv3 import Controllerv3
from controllers.controllerplayer import PlayerController
#from controllers.controllertournament import TournamentController
from controllers.controllerv4 import ControllerChess




if __name__ == "__main__":
	start = Controllerv3()
    #start = ControllerChess()
    #player = PlayerController(view)
    #tournament= TournamentController(view)