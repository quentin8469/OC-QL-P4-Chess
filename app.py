#!/usr/bin/python
# -*- coding: utf-8 -*-
#from controllers.controller import Controller
from controllers.controllerv2 import Controllerv2
from controllers.controllerv3 import Controllerv3
#from controllers.controllerplayer import PlayerController
#from controllers.controllertournament import TournamentController
from views.menu import Menu



if __name__ == "__main__":
    view = Menu()
    start = Controllerv3(view)
    #player = PlayerController(view)
    #tournament= TournamentController(view)