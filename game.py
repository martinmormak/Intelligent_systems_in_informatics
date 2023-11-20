# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:47:30 2023

@author: marti
"""

import pygame

class Game:
    def __init__(self, gui, loader):
        self.gui = gui
        self.loader = loader

    def main_loop(self):
        field_array = self.loader.load_field()
        sw=self.gui.screen_width
        w=self.gui.WIDTH
        sh=self.gui.screen_height
        h=self.gui.HEIGHT

        while True:
            self.gui.handle_events()
            self.gui.screen.fill((255, 255, 255))
            offset_x = (sw - len(field_array[0]) * w) // 2
            offset_y = (sh - len(field_array) * h) // 2
            self.gui.draw_grid(field_array, offset_x, offset_y)
            self.gui.update_display()
            pygame.time.Clock().tick(30)