# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:28:52 2023

@author: marti
"""
import pygame

from loader import Loader
from gui import GUI
from control import Control
from game import Game

if __name__ == "__main__":
    pygame.init()

    # Constants
    SCREEN_WIDTH = 720
    SCREEN_HEIGHT = 720
    WIDTH = SCREEN_WIDTH // 8
    HEIGHT = SCREEN_HEIGHT // 8

    game_loader = Loader()
    game_gui = GUI(SCREEN_WIDTH, SCREEN_HEIGHT, 8, 8)
    game_control = Control(8, 8)
    rush_hour_game = Game(game_gui, game_loader)

    rush_hour_game.main_loop()
        