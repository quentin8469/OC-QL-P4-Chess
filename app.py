#!/usr/bin/python
# -*- coding: utf-8 -*-
from controllers.controller import Controller
from views.menu import Menu



if __name__ == "__main__":
    view = Menu()
    start = Controller(view)