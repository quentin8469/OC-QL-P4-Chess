#!/usr/bin/env/python3


from models.joueur import Player
from tinydb import TinyDB, Query
from views.playerviews import PlayerViews


class PlayerController:
    """
    All player controlles
    """

    def __init__(self):
        """ constructor controller player"""
        self.playerviews = PlayerViews()
        self.playerdb = TinyDB("players.json")
        self.playerquery = Query()
        self.player_table = self.playerdb.table("players")

    def player_menu(self):
        """ start the player menu"""
        self.playerviews.menu_player()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [
            self.new_player,
            self.edit_player,
            self.players_list,
        ]
        if menu == 3:
            pass
        else:
            menu_list[menu]()

    def new_player(self):
        """ Create a new player"""
        self.playerviews.new_player_lname()
        lastname = input()
        self.playerviews.new_player_fname()
        firstname = input()
        self.playerviews.new_player_bdate()
        birth_date = input()
        self.playerviews.new_player_gender()
        gender = input()
        self.playerviews.new_player_elo()
        elo = input()
        new_player = Player(lastname, firstname, birth_date, gender, elo)
        self.player_table.insert(new_player.serialized_player())
        self.player_menu()

    def edit_player(self):
        """  edit player Elo"""
        self.playerviews.new_player_lname()
        input_player = input()
        self.playerviews.change_player_elo()
        try:
            input_elo = int(input())
        except ValueError:
            self.playerviews.error_player_elo()
        else:
            self.player_table.update(
                {"Elo": input_elo}, self.playerquery.Last_name == f"{input_player}"
            )
        finally:
            self.player_menu()

    def players_list(self):
        """ Create a list of all players"""
        players = self.player_table.all()
        for player in players:
            self.playerviews.player_list(player)
        self.player_menu()

    def player_alpha_order(self):
        """ List of the player in alphabetique order"""
        players = self.player_table.all()
        alpha_order = sorted(players, key=lambda x: x["Last_name"])
        return alpha_order

    def player_classement_order(self):
        """ List of the player in classement order"""
        players = self.player_table.all()
        classe_order = sorted(players, key=lambda x: x["Elo"], reverse=True)
        return classe_order

    def search_player(self):
        """ serch player"""
        self.playerviews.new_player_lname()
        input_player = input()
        player = self.player_table.search(
            self.playerquery.Last_name == f"{input_player}"
        )
        if len(player) == 1:
            return player
        else:
            self.playerviews.error_add_player_lname()
        self.search_player
