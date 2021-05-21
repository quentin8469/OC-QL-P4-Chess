#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.joueur import Player
from models.tournoi import Tournament
from models.ronde import Ronde
from tinydb import TinyDB, Query
from views.menu import Menu


class Controllerv3:
    """
    This class control the application
    """

    def __init__(self):
        """ constructor initialisation """
        self.menu = Menu()
        self.tournamentdb = TinyDB("tournament3.json")
        self.playerdb = TinyDB("players1.json")
        self.tournamentquery = Query()
        self.playerquery = Query()
        self.tournament_table = self.tournamentdb.table("tournament3")
        self.player_table = self.playerdb.table("players1")
        self.start_menu()

    def start_menu(self):
        """ start the view menu_start"""
        self.menu.menu_start()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "Q"]
        while input_choice not in input_check_list:
            input_choice = input()
        index_menu = input_check_list.index(input_choice)
        menu_list = [
            self.tournament_menu,
            self.player_menu,
            self.game,
            self.report_menu,
            quit,
        ]
        menu_list[index_menu]()

    # -------------------tournament code ---------------------------------------
    def tournament_menu(self):
        """ start the tournament menu"""
        self.menu.menu_tournament()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4","5"]
        while input_choice not in input_check_list:
            input_choice = input()
        index_menu = input_check_list.index(input_choice)
        menu_list = [
            self.new_tt,
            self.edit_tt,
            self.tt_list,
            self.add_players_in_tt,
            self.start_menu,
        ]
        menu_list[index_menu]()

    def new_tt(self):
        """ doc """
        self.menu.new_tournament_name()
        name = input()
        self.menu.new_tournament_location()
        location = input()
        self.menu.new_tournament_date()
        st_date = input()
        e_date = ""
        rondes = 4
        tt_list = ()
        pl_list = []
        ttc = []
        self.menu.new_tournament_description()
        description = input()
        new_tournament = Tournament( name, location, st_date, e_date, rondes, tt_list, pl_list, ttc, description)
        self.tournament_table.insert(new_tournament.serialized_tournament())
        self.tournament_menu()

    def edit_tt(self):
        """ edit tournament """
        pass

    def tt_list(self):
        """ creat the list of all tournament """
        tournaments = self.tournament_table.all()
        for tournament in tournaments:
            self.menu.tournament_list(tournament)
        self.tournament_menu()

    def load_tt(self):
        """ load a tournament since a json """
        tt = []
        self.menu.new_tournament_name()
        Tournament_name = input()
        tournaments = self.tournament_table.search(
            self.tournamentquery.Tournament_name == f"{Tournament_name}"
        )
        for tournament in tournaments:
            tt.append(Tournament.deserializett(tournament))
        for tournoi in tt:
            self.menu.tournament_load(tournoi)
        return tt[0]
              
    def add_players_in_tt(self):
        """ add a list of player for the tournament"""
        tournoi = self.load_tt()
        pcount = 0
        
        while pcount < 8:
            players = self.search_player()
            self.menu.add_player_confirm()
            confirmation = input()
            if confirmation == "y":
                for player in players:
                    tournoi.add_player(Player.deserializeplayer(player))
                    self.menu.tournament_load(tournoi)
                    pcount += 1
            else:
                self.menu.tournament_load(tournoi)
                pcount +=0
                
        plist = []  
        for players in tournoi.tt_players:
            player = players.serialized_player()
            plist.append(player)
        self.tournament_table.update(
            {"Tournament_players": plist}, self.tournamentquery.Tournament_name == tournoi.name)
        self.tournament_menu()
        
    def add_round_bdd(self,round_list, tournoi):
        """ Add round in tournament bdd"""
        rlist =[]
        for round in round_list:
            ronde = round.serialized_rounds()
            rlist.append(ronde)
        self.tournament_table.update(
            {"Tournament_tournees": rlist}, self.tournamentquery.Tournament_name == tournoi.name)
        return rlist
        
    # ----------------------- Player code --------------------------------------
    def player_menu(self):
        """ start the player menu"""
        self.menu.menu_player()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4"]
        while input_choice not in input_check_list:
            input_choice = input()
        index_menu = input_check_list.index(input_choice)
        menu_list = [
            self.new_player,
            self.edit_player,
            self.players_list,
            self.start_menu,
        ]
        menu_list[index_menu]()

    def new_player(self):
        """ Create a new player"""
        self.menu.new_player_lname()
        lastname = input()
        self.menu.new_player_fname()
        firstname = input()
        self.menu.new_player_bdate()
        birth_date = input()
        self.menu.new_player_gender()
        gender = input()
        self.menu.new_player_elo()
        elo = int(input())
        new_player = Player(lastname, firstname, birth_date, gender, elo)
        self.player_table.insert(new_player.serialized_player())
        self.player_menu()

    def edit_player(self):
        """  edit player Elo"""
        self.menu.new_player_lname()
        input_player = input()
        self.menu.new_player_elo()
        input_elo = input()
        self.player_table.update(
            {"Elo": input_elo}, self.playerquery.Last_name == f"{input_player}"
        )
        self.player_menu()

    def players_list(self):
        """ Create a list of all players"""

        players = self.player_table.all()
        for player in players:
            self.menu.player_list(player)
        self.player_menu()

    def player_alpha_order(self):
        """ List of the player in alphabetique order"""

        players = self.player_table.all()
        alpha_order = sorted(players, key=lambda x: x["Last_name"])
        for alpha in alpha_order:
            self.menu.player_list(alpha)
        self.report_menu()

    def player_classement_order(self):
        """ List of the player in classement order"""
        players = self.player_table.all()
        elo_order = sorted(players, key=lambda x: x["Elo"], reverse=True)
        for elo in elo_order:
            self.menu.player_list(elo)
        self.report_menu()

    def search_player(self):
        """ serch player"""
        self.menu.new_player_lname()
        input_player = input()
        player = self.player_table.search(
            self.playerquery.Last_name == f"{input_player}"
        )
        for play in player:
            self.menu.player_search(play)
            return player

    def players_list_for_tt(self):
        """ add player in players tt list"""
        player_tt_list = []
        for players in self.player_table.all():

            player_tt_list.append(players)
        return player_tt_list

    # ----------------------- Report code --------------------------------------
    def report_menu(self):
        """ start the report menu"""
        self.menu.menu_report()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [
            self.player_alpha_order,
            self.player_classement_order,
            self.report_player_alpha_order_tt,
            self.report_player_rank_order_tt,
            self.report_tt_list,
            self.report_all_rondes,
            self.report_all_match,
            self.start_menu,
        ]
        menu_list[menu]()

    def report_tt_list(self):
        """ give the list of all tournament """
        tournaments = self.tournament_table.all()
        for tournament in tournaments:
            self.menu.tournament_list(tournament)
        self.report_menu()

    def report_player_alpha_order_tt(self):
        """ give all the player for one tournament in alphabetical order"""
        tt = self.load_tt()
        players = tt.tt_players
        alpha_order = sorted(players, key=lambda x: x["Last_name"])
        for alpha in alpha_order:
            self.menu.player_list(alpha)
        self.report_menu()

    def report_player_rank_order_tt(self):
        """ give all the player for one tournament in rank order"""
        tt = self.load_tt()
        players = tt.tt_players
        elo_order = sorted(players, key=lambda x: x["Elo"], reverse=True)
        for elo in elo_order:
            self.menu.player_list(elo)
        self.report_menu()

    def report_all_rondes(self):
        """ give all the ronde in a tournament"""
        tt = self.load_tt()
        rondes = tt.tournees_list
        print(rondes)
        self.report_menu()

    def report_all_match(self):
        """ give all matchs in a tournament"""
        tt = self.load_tt()
        rondes = tt.tournees_list
        for matchs in rondes:
            
            print(matchs['Matchs'])
        self.report_menu()

    # --------------------- Game -----------------------------------------------

    def first_round_by_elo(self, tournoi):
        """ tri de la p_list selon le elo de chaque joueur"""
        
        p_elo =[]
        for player in tournoi.tt_players:
            p_elo.append(Player.deserializeplayer(player))
        p_elo.sort(key=lambda x: x.elo, reverse=True)    
        middle_one = p_elo[:4]
        middle_two = p_elo[4:]
        return middle_one, middle_two

    def scoring_first_round(self, middle_one, middle_two):
        """ manage the scoring of the first round """

        p_score = []
        round = []
        self.menu.f_round(middle_one, middle_two)
        self.menu.new_round()
        start = input()
        check_start = ["y", "n"]
        while start not in check_start:
            start = input()
        if start == "y":
            self.menu.first_round(middle_one, middle_two)
            pcount = 0
            while pcount < 4:
                choice = input()
                check_choice = ["1", "2", "3"]
                while choice not in check_choice:
                    choice = input()
                if choice == "1":
                    middle_one[0].score += int(1)
                    match = ([middle_one[0].lastname,middle_one[0].score], [middle_two[0].lastname, middle_two[0].score])
                    round.append(match)
                    p_score.append(middle_one.pop(0))
                    p_score.append(middle_two.pop(0))                    
                if choice == "2":
                    middle_two[0].score += int(1)
                    match = ([middle_one[0].lastname,middle_one[0].score], [middle_two[0].lastname, middle_two[0].score])
                    round.append(match)
                    p_score.append(middle_one.pop(0))
                    p_score.append(middle_two.pop(0))                    
                if choice == "3":
                    middle_one[0].score += float(0.5)
                    middle_two[0].score += float(0.5)
                    match = ([middle_one[0].lastname,middle_one[0].score], [middle_two[0].lastname, middle_two[0].score])
                    round.append(match)
                    p_score.append(middle_one.pop(0))
                    p_score.append(middle_two.pop(0))
                pcount += 1        
        if start == "n":
            self.start_menu()
        return p_score, round

    def next_round_by_score(self, next_pscore):
        """ tri de la liste de joueur celon le score """

        new_player_score_list = []
        round = []
        next_pscore.sort(key=lambda x: (x.score, x.elo), reverse=True)
        self.menu.other_round(next_pscore)
        self.menu.new_round()
        start = input()
        check_start = ["y", "n"]
        while start not in check_start:
            start = input()
        if start == "y":
            self.menu.oth_round(next_pscore)
            pcount = 0
            while pcount < 4:
                choice = input()
                check_choice = ["1", "2", "3"]
                while choice not in check_choice:
                    choice = input()
                if choice == "1":
                    next_pscore[0].score += int(1)
                    match = ([next_pscore[0].lastname, next_pscore[0].score], [next_pscore[1].lastname, next_pscore[1].score])
                    round.append(match)
                    new_player_score_list.append(next_pscore[0])
                    new_player_score_list.append(next_pscore[1])
                    next_pscore.pop(0)
                    next_pscore.pop(0)
                if choice == "2":
                    next_pscore[1].score += int(1)
                    match = ([next_pscore[0].lastname, next_pscore[0].score], [next_pscore[1].lastname, next_pscore[1].score])
                    round.append(match)
                    new_player_score_list.append(next_pscore[0])
                    new_player_score_list.append(next_pscore[1])
                    next_pscore.pop(0)
                    next_pscore.pop(0)
                if choice == "3":
                    next_pscore[0].score += float(0.5)
                    next_pscore[1].score += float(0.5)
                    match = ([next_pscore[0].lastname, next_pscore[0].score], [next_pscore[1].lastname, next_pscore[1].score])
                    round.append(match)
                    new_player_score_list.append(next_pscore[0])
                    new_player_score_list.append(next_pscore[1])
                    next_pscore.pop(0)
                    next_pscore.pop(0)
                pcount += 1
        if start == "n":
            self.start_menu()
        return new_player_score_list, round

    def game(self):
        """ Run chess game"""
        tournoi = self.load_tt()
        p_score =[]
        round_list = []
        rcount = 0     
        while rcount < 4:
            if rcount < 1:
                r1_order, r2_order = self.first_round_by_elo(tournoi)
                scores, round1 = self.scoring_first_round(r1_order, r2_order)
                round_list.append(Ronde(rcount+1,round1))
                for score in scores:
                    p_score.append(score)
            else:
                other_round, round = self.next_round_by_score(p_score)
                round_list.append(Ronde(rcount+1,round))
                for score in other_round:
                    p_score.append(score)
 
            rcount += 1
        
        rlist = self.add_round_bdd(round_list, tournoi)
        for round in rlist:
            tournoi.add_tournees(round)
        p_score.sort(key=lambda x: (x.score, x.elo), reverse=True)
        self.menu.end_tournament(p_score)
        self.start_menu()