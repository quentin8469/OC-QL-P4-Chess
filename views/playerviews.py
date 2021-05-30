#!/usr/bin/env/python3


class PlayerViews:
    """
    In this class we find all the views
    """


    def menu_player(self):
        """ print the Player menu """
        print("--------- Player Menu ---------")
        print("welcome, please select your action and press Enter")
        print("1.New player")
        print("2.Edit player Elo")
        print("3.Player list")
        print("4.Return to start menu")
        print("-------------------------------")

    def new_player_lname(self):
        """ get the player last name """
        print("Enter player Last Name: ")

    def new_player_fname(self):
        """ get the player firt name """
        print("Enter player First Name: ")

    def new_player_bdate(self):
        """ get the player Birth date """
        print("Enter player Birth date: dd/mm/yyyy")

    def new_player_gender(self):
        """ get the player gender """
        print("Enter player Gender: Male /Femelle / Autre")

    def new_player_elo(self):
        """ get the player Elo """
        print("Enter player Elo number: ")

    def error_player_lname(self):
        """ ask the correct player last name """
        print("Please enter the correct player Last name: ")
    
    def error_add_player_lname(self):
        """ ask the correct player last name """
        print("Player don't exist, please select 'n' for the confirmation")

    def player_list(self, player):
        """ give the liste of the players"""
        print("---------------------------------")
        print("Last_name:", player["Last_name"])
        print("First_name:", player["First_name"])
        print("Birth_date:", player["Birth_date"])
        print("Gender:", player["Gender"])
        print("Elo:", player["Elo"])
        print("Score:", player["Score"])
        print("---------------------------------")

    def player_search(self, player):
        """ give the search of the players"""
        print("-------Your research result------------")
        print("doc_id:", player.doc_id)
        print("Last_name:", player["Last_name"])
        print("First_name:", player["First_name"])
        print("Birth_date:", player["Birth_date"])
        print("Gender:", player["Gender"])
        print("Elo:", player["Elo"])
        print("Score:", player["Score"])
        print("---------------------------------------")
