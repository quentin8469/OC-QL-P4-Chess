#!/usr/bin/env/python3


from models.tournoi import Tournament
from models.joueur import Player
from views.tournamentviews import TournamentViews
from tinydb import TinyDB, Query


class TournamentController:
    """
    All tt controlles
    """

    def __init__(self):
        """ constructor controller tt"""
        self.ttviews = TournamentViews()
        self.tournamentdb = TinyDB("tournament.json")
        self.tournamentquery = Query()
        self.tournament_table = self.tournamentdb.table("tournament")

    def tournament_menu(self):
        """ start the tournament menu"""
        self.ttviews.menu_tournament()
        input_choice = input()
        input_check_list = ["1", "2", "3"]
        while input_choice not in input_check_list:
            input_choice = input()
        index_menu = input_check_list.index(input_choice)
        menu_list = [
            self.new_tt,
            self.tt_list,
        ]
        if index_menu == 2:
            pass
        else:
            menu_list[index_menu]()

    def new_tt(self):
        """ create new tournament object """
        self.ttviews.new_tournament_name()
        name = input()
        self.ttviews.new_tournament_location()
        location = input()
        self.ttviews.new_tournament_date()
        st_date = input()
        e_date = ""
        rondes = 4
        tt_list = ()
        pl_list = []
        self.ttviews.new_tournament_timer()
        ttc = input()
        ttc_check_list = ["Bullet", "Blitz", "Coup rapide"]
        while ttc not in ttc_check_list:
            ttc = input()
        self.ttviews.new_tournament_description()
        description = input()
        new_tournament = Tournament(
            name, location, st_date, e_date, rondes, tt_list, pl_list, ttc, description
        )
        self.tournament_table.insert(new_tournament.serialized_tournament())
        self.tournament_menu()

    def tt_list(self):
        """ creat the list of all tournament """
        tournaments = self.tournament_table.all()
        for tournament in tournaments:
            self.ttviews.tournament_list(tournament)
        self.tournament_menu()

    def load_tt(self):
        """ load a tournament since a json """
        tt = []
        self.ttviews.new_tournament_name()
        Tournament_name = input()
        tournaments = self.tournament_table.search(
            self.tournamentquery.Tournament_name == f"{Tournament_name}"
        )
        if len(tournaments) == 1:
            for tournament in tournaments:
                tt.append(Tournament.deserializett(tournament))
            for tournoi in tt:
                self.ttviews.tournament_load(tournoi)
            self.add_players_in_tt(tt[0])
        else:
            self.ttviews.error_tt_name()
            self.tournament_menu()

    def add_players_in_tt(self, tournois):
        """ add a list of player for the tournament"""
        tournoi = tournois
        if len(tournoi.tt_players) == 8:
            self.ttviews.tt_adding_player()
            self.tournament_menu()
        else:
            pcount = 0
            while pcount < 8:
                players = Player.search_player()
                self.ttviews.add_player_confirm()
                confirmation = input()
                if confirmation == "y":
                    for player in players:
                        tournoi.add_player(Player.deserializeplayer(player))
                        self.menu.tournament_load(tournoi)
                        pcount += 1
                else:
                    self.ttviews.tournament_load(tournoi)
                    pcount += 0
            plist = []
            for players in tournoi.tt_players:
                player = players.serialized_player()
                plist.append(player)
            self.tournament_table.update(
                {"Tournament_players": plist},
                self.tournamentquery.Tournament_name == tournoi.name,
            )
            self.tournament_menu()
