#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.joueur import Player
from models.tournoi import Tournament
from tinydb import TinyDB, Query

class Controllerv3:
	"""
	This class control the application
	"""
	def __init__(self, menu):
		""" constructor initialisation """
		self.menu = menu
		self.tournamentdb = TinyDB("tournament1.json")
		self.playerdb = TinyDB("players1.json")
		self.tournamentquery = Query()
		self.playerquery = Query()
		self.tournament_table = self.tournamentdb.table("tournament1")
		self.player_table = self.playerdb.table("players1")
		self.start_menu()
	
	def start_menu(self):
		""" start the view menu_start"""
		self.menu.menu_start()
		input_choice = input()
		input_check_list = ["1", "2", "3", "Q"]
		while input_choice not in input_check_list:
			input_choice = input()
		menu = input_check_list.index(input_choice)
		menu_list = [self.tournament_menu, self.player_menu, self.report_menu, "Kiss"]
		menu_list[menu]()
#-------------------tournament code --------------------------------------------	
	def tournament_menu(self):
		""" start the tournament menu"""
		self.menu.menu_tournament()
		input_choice = input()
		input_check_list = ["1", "2", "3", "4", "5", "6"]
		while input_choice not in input_check_list:
			input_choice = input()
		menu = input_check_list.index(input_choice)
		menu_list = [
			self.new_tt,
			self.edit_tt,
			self.tt_list,
			self.load_tt,
			self.report_tt,
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
		self.menu.new_tournament_rondes()
		rondes = input()
		self.menu.new_tournament_tournees()
		tournees = input()
		self.menu.new_tournament_description()
		description = input()
		new_tournament = Tournament(name, location, date, rondes, tournees, 
																	description)
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
		pass

	def report_tt(self):
		""" doc """
		# a effacer
		pass
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
		elo = input()
		new_player = Player(lastname, firstname, birth_date, gender, elo)
		self.player_table.insert(new_player.serialized_player())
		self.player_menu()

	def edit_player(self):
		"""	 edit player Elo"""
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
		for classse in classe_order:
			self.menu.player_list(classse)
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
	
	def repoart_all_match(self):
		""" give all matchs in a tournament"""
		pass