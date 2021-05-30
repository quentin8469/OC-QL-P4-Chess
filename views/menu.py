#!/usr/bin/env/python3


class Menu:
    """
    In this class we find all the views
    """


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

    def new_tournament_name(self):
        """ get the tournament name"""
        print("Enter Tournament name: ")

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

    def error_tt_name(self):
        """ ask the correct player last name """
        print("Please enter the correct tournament name: ")

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

    def tt_add_player(self):
        """ get the tournament name"""
        print("Please add player in your tournament")

    def round_view(self, rounds):
        """ view all rounds for a tournament"""
        print("---------------------------------")
        print("Ronde:", rounds["Ronde"])
        print("Start_time:", rounds["Start_time"])
        print("End_time:", rounds["End_time"])
        print("Matchs:", rounds["Matchs"])
        print("---------------------------------")

    def match_view(self, match):
        """ viaw all matchs for a tournament """
        print("Matchs:", match["Matchs"])

    def menu_report(self):
        """ print the report menu """
        print("------------ Report Menu -------------")
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
        print("--------------------------------------")

    def tcontrol_view(self):
        """ start tournament view """
        print("Select tournament time controle: 1- Bullet, 2-Blitz, 3-")

    def f_round(self, p, c):
        """ give the view player vs player """
        print("----- Round players classement-----")
        for i in range(4):
            print(
                "Player:",
                p[i].lastname,
                p[i].elo,
                "vs",
                "Player:",
                c[i].lastname,
                c[i].elo,
            )

    def first_round(self, p, c):
        """ view to say who is the winner"""
        print("--------- Choose the winner or draw -----------")
        for i in range(4):
            print("Winner:", p[i].lastname, "[1]", "or", c[i].lastname, "[2]")
            print("Draw: [3)")
        print("The round is finish, enter results:")

    def new_round(self):
        """ view to choose to start a other round"""
        print("Start the round? y/n")

    def other_round(self, player):
        """ view of the player liste for the score management """
        print("----- Round players classement-----")
        for i in range(0, len(player), 2):
            print(
                "Player:",
                player[i].lastname,
                player[i].score,
                "vs",
                "Player:",
                player[i + 1].lastname,
                player[i + 1].score,
            )
        print("------------------------------------")

    def oth_round(self, player):
        """ view for choose the winner """
        print("--------- Choose the winner or draw -----------")
        for i in range(0, len(player), 2):
            print(
                "Winner:",
                player[i].lastname,
                "[1]",
                "or",
                player[i + 1].lastname,
                "[2]",
            )
            print("Draw: [3)")
        print("The round is finish, enter results:")

    def end_tournament(self, player):
        """ view whit the playersresults of the tournament"""
        print("----- End of the tournament - players classement-----")
        for i in range(0, len(player), 2):
            print(
                "Player:",
                player[i].lastname,
                player[i].score,
                "vs",
                "Player:",
                player[i + 1].lastname,
                player[i + 1].score,
            )
        print("-------------------------------------------------------")
