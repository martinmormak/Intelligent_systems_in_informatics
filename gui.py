# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:50:38 2023

@author: marti
"""

import pygame
import sys

class GUI:
    def __init__(self, screen_width, screen_height, rows, columns):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rows = rows
        self.columns = columns

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption('RUSH HOUR')

        self.WIDTH = self.screen_width // self.columns
        self.HEIGHT = self.screen_height // self.rows

    def draw_grid(self, field_array, offset_x, offset_y):
        #colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        YELLOW = (255, 255, 0)
        MAGENTA = (255, 0, 255)
        CYAN = (0, 255, 255)
        GRAY = (128, 128, 128)
        MAROON = (128, 0, 0)
        OLIVE = (128, 128, 0)
        DARK_GREEN = (0, 128, 0)
        PURPLE = (128, 0, 128)
        for row in range(self.rows):
            for col in range(self.columns):
                cell_value = field_array[row][col]
                rect = pygame.Rect(offset_x + col * self.WIDTH, offset_y + row * self.HEIGHT, self.WIDTH, self.HEIGHT)

                if cell_value == 0:
                    pygame.draw.rect(self.screen, WHITE, rect)
                elif cell_value == 1:
                    pygame.draw.rect(self.screen, BLACK, rect)
                elif cell_value == 2:
                    pygame.draw.rect(self.screen, RED, rect)
                elif cell_value == 3:
                    pygame.draw.rect(self.screen, GREEN, rect)
                elif cell_value == 4:
                    pygame.draw.rect(self.screen, BLUE, rect)
                elif cell_value == 5:
                    pygame.draw.rect(self.screen, YELLOW, rect)
                elif cell_value == 6:
                    pygame.draw.rect(self.screen, MAGENTA, rect)
                elif cell_value == 7:
                    pygame.draw.rect(self.screen, CYAN, rect)
                elif cell_value == 8:
                    pygame.draw.rect(self.screen, GRAY, rect)
                elif cell_value == 9:
                    pygame.draw.rect(self.screen, MAROON, rect)
                elif cell_value == 10:
                    pygame.draw.rect(self.screen, OLIVE, rect)
                elif cell_value == 11:
                    pygame.draw.rect(self.screen, DARK_GREEN, rect)
                elif cell_value == 12:
                    pygame.draw.rect(self.screen, PURPLE, rect)
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                # Handle window resizing
                pass

    def update_display(self):
        pygame.display.flip()