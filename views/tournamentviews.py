#!/usr/bin/env/python3


class TournamentViews:
    """
    In this class we find all the views
    """

    def menu_tournament(self):
        """ print the Tournament menu """
        print("----------- Tournament Menu -----------")
        print("welcome, please select your action and press Enter")
        print("1.Create Tournament")
        print("2.List of Tournament")
        print("3.Return to start menu")
        print("---------------------------------------")

    def new_tournament_name(self):
        """ get the tournament name"""
        print("Enter Tournament name: ")

    def new_tournament_location(self):
        """ get the tournament location"""
        print("Enter Tournament location: ")

    def new_tournament_date(self):
        """ get the tournament date"""
        print("Enter Tournament date: dd/mm/yyyy ")

    def new_tournament_timer(self):
        """ get the tournament timer"""
        print("Write Tournament type timer: ")
        print("Bullet")
        print("Blitz")
        print("Coup rapide")
        print("Enter your choice: ")

    def new_tournament_description(self):
        """ get the tournament location"""
        print("Enter Tournament description: ")

    def tournament_list(self, tournament):
        """ give the liste of the tournament"""
        print("-------- Liste des tournois --------")
        print("doc_id:", tournament.doc_id)
        print("Tournament_name:", tournament["Tournament_name"])
        print("Tournament_location:", tournament["Tournament_location"])
        print("Tournament_start_date:", tournament["Tournament_start_date"])
        print("Tournament_end_date:", tournament["Tournament_end_date"])
        print("Tournament_rondes:", tournament["Tournament_rondes"])
        print("Tournament_tournees:", tournament["Tournament_tournees"])
        print("Tournament_players:", tournament["Tournament_players"])
        print("Tournament_Tcontrol:", tournament["Tournament_Tcontrol"])
        print("Tournament_description:", tournament["Tournament_description"])
        print("---------------------------------")

    def tournament_load(self, tournament):
        """ give the liste of the tournament"""
        print("-------- Données du tournoi chargé ---------")
        print("Tournament_name:", tournament.name)
        print("Tournament_location:", tournament.location)
        print("Tournament_start_date:", tournament.start_date)
        print("Tournament_end_date:", tournament.end_date)
        print("Tournament_rondes:", tournament.rondes)
        print("Tournament_tournees:", tournament.tournees_list)
        print("Tournament_players:", tournament.tt_players)
        print("Tournament_Tcontrol:", tournament.time_control)
        print("Tournament_description:", tournament.description)
        print("--------------------------------------------")

    def add_player_confirm(self):
        """ get the tournament name"""
        print("Confirme player ? y/n ")

    def tt_adding_player(self):
        """ get the tournament name"""
        print("Your tournament is full of players")
