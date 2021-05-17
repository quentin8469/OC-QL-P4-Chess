#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.joueur import Player
from models.tournoi import Tournament
from tinydb import TinyDB, Query
from views.menu import Menu

class Controllerv3:
    """
    This class control the application
    """
    def __init__(self):
        """ constructor initialisation """
        self.menu = Menu()
        self.tournamentdb = TinyDB("tournament2.json")
        self.playerdb = TinyDB("players1.json")
        self.tournamentquery = Query()
        self.playerquery = Query()
        self.tournament_table = self.tournamentdb.table("tournament2")
        self.player_table = self.playerdb.table("players1")
        self.start_menu()
    
    def start_menu(self):
        """ start the view menu_start"""
        self.menu.menu_start()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "Q"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [self.tournament_menu, self.player_menu, self.first_round_by_elo, self.report_menu, "Kiss"]
        menu_list[menu]()
#-------------------tournament code --------------------------------------------    
    def tournament_menu(self):
        """ start the tournament menu"""
        self.menu.menu_tournament()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "5"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [
            self.new_tt,
            self.edit_tt,
            self.tt_list,
            self.load_tt,
            self.start_menu,
        ]
        menu_list[menu]()
        
    def new_tt(self):
        """ doc """
        self.menu.new_tournament_name()
        name = input()
        self.menu.new_tournament_location()
        location = input()
        self.menu.new_tournament_date()
        date = input()
        #self.menu.new_tournament_rondes()
        #rondes = input()
        #self.menu.new_tournament_tournees()
        #tournees = input()
        self.menu.new_tournament_description()
        description = input()
        new_tournament = Tournament(name, location, date, description)
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
        # deserialisation de la bdd, passer en liste, idem pour les players
        pass

    def add_players_tt(self):
        """ add a list of player for the tournament"""
        self.tt_players = self.player_list_for_tt()
        self.tournament_table.insert(self.tt_players)
        
# ----------------------- Player code ------------------------------------------
    def player_menu(self):
        """ start the player menu"""
        self.menu.menu_player()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "5"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [
            self.new_player,
            self.edit_player,
            self.players_list,
            self.search_player,
            self.start_menu,
        ]
        menu_list[menu]()

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
        self.player_table.update({'Elo': input_elo},
                                self.playerquery.Last_name == f'{input_player}')
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
        alpha_order = sorted(players,key=lambda x:x['Last_name'])
        for alpha in alpha_order:
            self.menu.player_list(alpha)
        self.report_menu()        

    def player_classement_order(self):
        """ List of the player in classement order"""
        players = self.player_table.all()
        classe_order = sorted(players,key=lambda x:x['Elo'], reverse=True)
        for elo in classe_order:
            self.menu.player_list(elo)
        self.report_menu()

    def search_player(self):
        """ serch player"""
        self.menu.new_player_lname()
        input_player = input()
        player = self.player_table.search(self.playerquery.Last_name 
                                                           == f'{input_player}')
        for play in player:
            self.menu.player_search(play)
        self.player_menu()
        
    def player_list_for_tt(self):
        """ add player in a tt list"""
        player_tt_list = []
        for players in self.player_table.all():
            player_tt_list.append(players)
        return play_tt_list
# ----------------------- Report code ------------------------------------------        
    def report_menu(self):
        """ start the report menu"""
        self.menu.menu_report()
        input_choice = input()
        input_check_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
        while input_choice not in input_check_list:
            input_choice = input()
        menu = input_check_list.index(input_choice)
        menu_list = [self.player_alpha_order, self.player_classement_order, self.start_menu, 
             self.start_menu, self.report_tt_list, self.start_menu, self.start_menu]
        menu_list[menu]()
    
    def report_tt_list(self):
        """ give the list of all tournament """
        tournaments = self.tournament_table.all()
        for tournament in tournaments:
            self.menu.tournament_list(tournament)
        self.report_menu()
    
    def report_player_alpha_order_tt(self):
        """ give all the player for one tournament in alphabetical order"""
        pass
    
    def report_player_rank_order_tt(self):
        """ give all the player for one tournament in rank order"""
        pass
    
    def report_all_rondes(self):
        """ give all the ronde in a tournament"""
        pass
    
    def report_all_match(self):
        """ give all matchs in a tournament"""
        pass
#--------------------- Game ----------------------------------------------------

    def first_round_by_elo(self):
        """ tri de la p_list celon le elo de chaque joueur"""
        p_elo =[]
        p_score =[]
        players = self.player_table.all()
        classe_order = sorted(players,key=lambda x:x['Elo'], reverse=True)
        for elo in classe_order:
            p_elo.append(elo)
 
        middle_one = p_elo[0:4]
        middle_two = p_elo[4:8]
        self.menu.first_round(middle_one, middle_two)
        self.menu.new_round()
        start = input()
        if start == "y":
            self.menu.f_round(middle_one, middle_two)             
            choice = input()
            check_choise =["1", "2", "3"]
            while choice not in check_choise:
                    choice = input()
            if choice == "1":
                middle_one[0]["Score"] += int(1)
                p_score.append(middle_one[0])
                p_score.append(middle_two[0])
                
            
            if choice == "2":
                middle_two[0]["Score"] += int(1)
                p_score.append(middle_one[0])
                p_score.append(middle_two[0])
                
            if choice == "3":
                middle_one[0]["Score"] += float(0.5)
                middle_two[0]["Score"] += float(0.5)
                p_score.append(middle_one[0])
                p_score.append(middle_two[0])
                
            choice = input()
            check_choise =["1", "2", "3"]
            while choice not in check_choise:
                    choice = input()
            if choice == "1":
                middle_one[1]["Score"] += int(1)
                p_score.append(middle_one[1])
                p_score.append(middle_two[1])
                
            if choice == "2":
                middle_two[1]["Score"] += int(1)
                p_score.append(middle_one[1])
                p_score.append(middle_two[1])
                
            if choice == "3":
                middle_one[1]["Score"] += float(0.5)
                middle_two[1]["Score"] += float(0.5)
                p_score.append(middle_one[1])
                p_score.append(middle_two[1])
                
            choice = input()
            check_choise =["1", "2", "3"]
            while choice not in check_choise:
                    choice = input()
            if choice == "1":
                middle_one[2]["Score"] += int(1)
                p_score.append(middle_one[2])
                p_score.append(middle_two[2])
                
            if choice == "2":
                middle_two[2]["Score"] += int(1)
                p_score.append(middle_one[2])
                p_score.append(middle_two[2])
                
            if choice == "3":
                middle_one[2]["Score"] += float(0.5)
                middle_two[2]["Score"] += float(0.5)
                p_score.append(middle_one[2])
                p_score.append(middle_two[2])
                
            choice = input()
            check_choise =["1", "2", "3"]
            while choice not in check_choise:
                    choice = input()
            if choice == "1":
                middle_one[3]["Score"] += int(1)
                p_score.append(middle_one[3])
                p_score.append(middle_two[3])
                
            if choice == "2":
                middle_two[3]["Score"] += int(1)
                p_score.append(middle_one[3])
                p_score.append(middle_two[3])
                
            if choice == "3":
                middle_one[3]["Score"] += float(0.5)
                middle_two[3]["Score"] += float(0.5)
                p_score.append(middle_one[3])
                p_score.append(middle_two[3])
                
        self.menu.new_round()
        next_round = input()
        if next_round == "y":
            self.next_round_by_score(p_score)


 
    def next_round_by_score(self, p_score):
        """ tri de la liste de joueur celon le score """
        
        score_order = sorted(p_score, key=lambda x: (x["Score"], x["Elo"]), reverse=True)
        p_score_liste = []
        p_sl =[]
        for players in score_order:
            p_score_liste.append(players)
        self.menu.other_round(p_score_liste)
    
        self.menu.new_round()
        start = input()
        if start == "y":
            self.menu.oth_round(p_score_liste)
            #1
            choice = input()
            check_choise =["1", "2", "3"]
            while choice not in check_choise:
                    choice = input()
            if choice == "1":
                p_score_liste[0]["Score"] += int(1)
                p_sl.append(p_score_liste[0])
                p_sl.append(p_score_liste[1])
            if choice == "2":
                p_score_liste[1]["Score"] += int(1)
                p_sl.append(p_score_liste[0])
                p_sl.append(p_score_liste[1])
            if choice == "3":
                p_score_liste[0]["Score"] += float(0.5)
                p_score_liste[1]["Score"] += float(0.5)
                p_sl.append(p_score_liste[0])
                p_sl.append(p_score_liste[1])
            #2
            choice = input()
            check_choise =["1", "2", "3"]
            while choice not in check_choise:
                    choice = input()
            if choice == "1":
                p_score_liste[2]["Score"] += int(1)
                p_sl.append(p_score_liste[2])
                p_sl.append(p_score_liste[3])
            if choice == "2":
                p_score_liste[3]["Score"] += int(1)
                p_sl.append(p_score_liste[2])
                p_sl.append(p_score_liste[3])
            if choice == "3":
                p_score_liste[2]["Score"] += float(0.5)
                p_score_liste[3]["Score"] += float(0.5)
                p_sl.append(p_score_liste[2])
                p_sl.append(p_score_liste[3])
            #3  
            choice = input()
            check_choise =["1", "2", "3"]
            while choice not in check_choise:
                    choice = input()
            if choice == "1":
                p_score_liste[4]["Score"] += int(1)
                p_sl.append(p_score_liste[4])
                p_sl.append(p_score_liste[5])
            if choice == "2":
                p_score_liste[5]["Score"] += int(1)
                p_sl.append(p_score_liste[4])
                p_sl.append(p_score_liste[5])
            if choice == "3":
                p_score_liste[4]["Score"] += float(0.5)
                p_score_liste[5]["Score"] += float(0.5)
                p_sl.append(p_score_liste[4])
                p_sl.append(p_score_liste[5])
            #4  
            choice = input()
            check_choise =["1", "2", "3"]
            while choice not in check_choise:
                    choice = input()
            if choice == "1":
                p_score_liste[6]["Score"] += int(1)
                p_sl.append(p_score_liste[6])
                p_sl.append(p_score_liste[7])
            if choice == "2":
                p_score_liste[7]["Score"] += int(1)
                p_sl.append(p_score_liste[6])
                p_sl.append(p_score_liste[7])
            if choice == "3":
                p_score_liste[6]["Score"] += float(0.5)
                p_score_liste[7]["Score"] += float(0.5)
                p_sl.append(p_score_liste[6])
                p_sl.append(p_score_liste[7])
        print(p_sl)
        self.next_round_by_score(p_sl)
        else:
            pass