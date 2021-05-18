#!/usr/bin/python
# -*- coding: utf-8 -*-


class Menu:
    """
    In this class we find all the views
    """

    def __init__(self):
        """ docting """
        pass

    # -------------------view start---------------------------------------------
    def menu_start(self):
        """ print the start menu """
        print("--------- Start Menu ---------")
        print("welcome, please select your action and press Enter")
        print("1.Manage Tournament")
        print("2.Manage Player")
        print("3.Start Tournament")
        print("4.Report")
        print("Q.Quit the application")
        print("Choose your action please")
        print("------------------------------")

    # --------------------- view player-----------------------------------------
    def menu_player(self):
        """ print the Player menu """
        print("--------- Player Menu ---------")
        print("welcome, please select your action and press Enter")
        print("1.New player")
        print("2.Edit player Elo")
        print("3.Player list")
        print("4.Player search")
        print("5.Return to start menu")
        print("-------------------------------")

    def new_player_number(self):
        """ give number of player you want add"""
        print("Number of players you want add: ")

    def new_player_lname(self):
        """ get the player last name """
        print("Last Name: ")

    def new_player_fname(self):
        """ get the player firt name """
        print("First Name: ")

    def new_player_bdate(self):
        """ get the player Birth date """
        print("Birth date: ")

    def new_player_gender(self):
        """ get the player gender """
        print("Gender: ")

    def new_player_elo(self):
        """ get the player Elo """
        print("Elo: ")

    def player_list(self, player):
        """ give the liste of the players"""

        print("---------------------------------")
        print("doc_id:", player.doc_id)
        print("Last_name:", player["Last_name"])
        print("First_name:", player["First_name"])
        print("Birth_date:", player["Birth_date"])
        print("Gender:", player["Gender"])
        print("Elo:", player["Elo"])
        print("Score:", player["Score"])
        print("---------------------------------")

    def player_search(self, player):
        """ give the search of the players"""

        print("-------Your research-------------")
        print("doc_id:", player.doc_id)
        print("Last_name:", player["Last_name"])
        print("First_name:", player["First_name"])
        print("Birth_date:", player["Birth_date"])
        print("Gender:", player["Gender"])
        print("Elo:", player["Elo"])
        print("---------------------------------")

    # -------------------------- view Tournament -------------------------------
    def menu_tournament(self):
        """ print the Tournament menu """
        print("--------- Tournament Menu ---------")
        print("welcome, please select your action and press Enter")
        print("1.Create Tournament")
        print("2.Edit Tournament")
        print("3.List of Tournament")
        print("4.load Tournament")
        print("5.Return to start menu")
        print("-----------------------------------")

    def new_tournament_name(self):
        """ get the tournament name"""
        print("Tournament name: ")

    def new_tournament_location(self):
        """ get the tournament location"""
        print("Tournament location: ")

    def new_tournament_date(self):
        """ get the tournament date"""
        print("Tournament date: ")

    def new_tournament_rondes(self):
        """ get the tournament rondes"""
        print("Tournament rondes: ")

    def new_tournament_tournees(self):
        """ get the tournament tournees"""
        print("Tournament tournees: ")

    def new_tournament_player(self):
        """ get the tournament player"""
        print("Tournament player: ")

    def new_tournament_timer(self):
        """ get the tournament timer"""
        print("Tournament timer: ")

    def new_tournament_description(self):
        """ get the tournament location"""
        print("Tournament description: ")

    def tournament_list(self, tournament):
        """ give the liste of the tournament"""

        print("--------Liste des tournoi--------")
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

    # ---------------------------- view report ---------------------------------

    def menu_report(self):
        """ print the report menu """
        print("--------- Report Menu ---------")
        print("welcome, please select your action and press Enter")
        print("List of all actors:")
        print("    1. Alphabetique order")
        print("    2. Classement order")
        print("List of all player for one tournament:")
        print("    3. Alphabetique order")
        print("    4. Classement order")
        print("5.List of all tournaments")
        print("6.List of all rondes in a tournament")
        print("7.List of all matchs in a tournament")
        print("8.Return to start menu")
        print("-------------------------------")

    # ----------------------- view Round ---------------------------------------
    def start_view(self):
        """ start tournament view """
        print("1. Select tournament by id")


    def f_round(self, p, c):
        """ give the view player vs player """
        print("----- Round players classement-----")
        print("P1:",p[0].lastname,p[0].elo,"vs","P2:",c[0].lastname,c[0].elo)
        print("P3:",p[1].lastname,p[1].elo,"vs","P4:",c[1].lastname,c[1].elo)
        print("P5:",p[2].lastname,p[2].elo,"vs","P6:",c[2].lastname,c[2].elo)
        print("P7:",p[3].lastname,p[3].elo,"vs","P8:",c[3].lastname,c[3].elo)

    def frist_round(self, p, c):
        """ view to say who is the winner"""
        print("--------- Choose the winner or draw -----------")
        print("Winner:", p[0]["Last_name"], "[1]", "or", c[0]["Last_name"], "[2]")
        print("Draw: [3)")
        print("Winner:", p[1]["Last_name"], "[1]", "or", c[1]["Last_name"], "[2]")
        print("Draw: [3)")
        print("Winner:", p[2]["Last_name"], "[1]", "or", c[2]["Last_name"], "[2]")
        print("Draw: [3)")
        print("Winner:", p[3]["Last_name"], "[1]", "or", c[3]["Last_name"], "[2]")
        print("Draw: [3)")
        print("The round is finish, enter results:")

    def new_round(self):
        """ view to choose to start a other round"""
        #print("Results correctly added")
        print("Start the round? y/n")

    def other_round(self, player):
        """ view of the player liste for the score management """
        print("----- Round players classement-----")
        print(
            "P1:",
            player[0]["Last_name"],
            player[0]["Score"],
            "vs",
            "P2:",
            player[1]["Last_name"],
            player[1]["Score"],
        )
        print(
            "P3:",
            player[2]["Last_name"],
            player[2]["Score"],
            "vs",
            "P4:",
            player[3]["Last_name"],
            player[3]["Score"],
        )
        print(
            "P5:",
            player[4]["Last_name"],
            player[4]["Score"],
            "vs",
            "P6:",
            player[5]["Last_name"],
            player[5]["Score"],
        )
        print(
            "P7:",
            player[6]["Last_name"],
            player[6]["Score"],
            "vs",
            "P8:",
            player[7]["Last_name"],
            player[7]["Score"],
        )

    def oth_round(self, player):
        """ view for choose the winner """
        print("Choose the winner or draw")
        print(
            "Winner:",
            player[0]["Last_name"],
            "[1]",
            "or",
            player[1]["Last_name"],
            "[2]",
        )
        print("Draw: [3)")
        print(
            "Winner:",
            player[2]["Last_name"],
            "[1]",
            "or",
            player[3]["Last_name"],
            "[2]",
        )
        print("Draw: [3)")
        print(
            "Winner:",
            player[4]["Last_name"],
            "[1]",
            "or",
            player[5]["Last_name"],
            "[2]",
        )
        print("Draw: [3)")
        print(
            "Winner:",
            player[6]["Last_name"],
            "[1]",
            "or",
            player[7]["Last_name"],
            "[2]",
        )
        print("Draw: [3)")
        print("The round is finish, start a other round? y/n")
