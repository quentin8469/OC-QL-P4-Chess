#!/usr/bin/python
# -*- coding: utf-8 -*-
from controllers.controller import Controller
#from views.menu import Menu

def main():
    """ Start the application """
    #test = Menu()
    #test.menu_start()
    #test.menu_report()
    test = Controller()
    test.start()


if __name__ == "__main__":
    main()
