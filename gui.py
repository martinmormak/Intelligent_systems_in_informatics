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
        self.car2_image = pygame.image.load('sprites/car2.png')  # Replace with the actual image path for size 2 ship
        self.car3_image = pygame.image.load('sprites/car3.png')  # Replace with the actual image path for size 3 ship
        self.rotated_car2_image = pygame.transform.rotate(self.car2_image, -90)
        self.rotated_car3_image = pygame.transform.rotate(self.car3_image, -90)
        self.colors = [[0,0,0,100],
                       [0,0,100,100],
                       [0,100,50,100],
                       [120,100,50,100],
                       [240,100,50,100],
                       [60,100,50,100],
                       [300,100,50,100],
                       [180,100,50,100],
                       [0,100,25,100],
                       [60,100,25,100],
                       [120,100,25,100],
                       [300,100,25,100],
                       [39,100,50,100],
                       [350,100,80,100],
                       [0,59,41,100],
                       [240,100,25,100],
                       [180,100,25,100],
                       [51,100,50,100],
                       [0,0,73,100],
                       [0,0,83,100],
                       [0,0,50,100],]

    def draw_grid(self, field_array, offset_x, offset_y):
        #colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        """RED = (255, 0, 0)
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
        ORANGE = (255, 165, 0)
        PINK = (255, 192, 203)
        BROWN = (165, 42, 42)
        NAVY_BLUE = (0, 0, 128)
        TEAL = (0, 128, 128)
        GOLD = (255, 215, 0)
        SILVER = (192, 192, 192)
        LIGHT_GRAY = (211, 211, 211)
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
                elif cell_value == 13:
                    pygame.draw.rect(self.screen, ORANGE, rect)
                elif cell_value == 14:
                    pygame.draw.rect(self.screen, PINK, rect)
                elif cell_value == 15:
                    pygame.draw.rect(self.screen, BROWN, rect)
                elif cell_value == 16:
                    pygame.draw.rect(self.screen, NAVY_BLUE, rect)
                elif cell_value == 17:
                    pygame.draw.rect(self.screen, TEAL, rect)
                elif cell_value == 18:
                    pygame.draw.rect(self.screen, GOLD, rect)
                elif cell_value == 19:
                    pygame.draw.rect(self.screen, SILVER, rect)
                elif cell_value == 20:
                    pygame.draw.rect(self.screen, LIGHT_GRAY, rect)"""
        visited_cars=set()
        for row in range(self.rows):
            for col in range(self.columns):
                cell_value = field_array[row][col]
                rect = pygame.Rect(offset_x + col * self.WIDTH, offset_y + row * self.HEIGHT, self.WIDTH, self.HEIGHT)
                if(cell_value!=0 and cell_value!=1):
                    if(cell_value not in visited_cars):
                        visited_cars.add(cell_value)
                        if(row>0 and cell_value==field_array[row+1][col]):
                            row_after=1
                            while(cell_value==field_array[row+row_after][col]):
                                row_after=row_after+1
                                if(row+row_after>self.rows-1):
                                    row_after=row_after-1
                                    break
                            if(row_after==3):
                                color = pygame.Color(0)
                                color.hsla = (self.colors[cell_value][0], self.colors[cell_value][1], self.colors[cell_value][2], self.colors[cell_value][3])
                                color_image = self.changeColor(self.car3_image, color)
                                self.screen.blit(color_image, (col * self.WIDTH, row * self.HEIGHT))
                            else:
                                color = pygame.Color(0)
                                color.hsla = (self.colors[cell_value][0], self.colors[cell_value][1], self.colors[cell_value][2], self.colors[cell_value][3])
                                color_image = self.changeColor(self.car2_image, color)
                                self.screen.blit(color_image, (col * self.WIDTH, row * self.HEIGHT))
                        if(col>0 and cell_value==field_array[row][col+1]):
                            column_after=1
                            while(cell_value==field_array[row][col+column_after]):
                                column_after=column_after+1
                                if(col+column_after>self.columns-1):
                                    column_after=column_after-1
                                    break
                            if(column_after==3):
                                color = pygame.Color(0)
                                color.hsla = (self.colors[cell_value][0], self.colors[cell_value][1], self.colors[cell_value][2], self.colors[cell_value][3])
                                color_image = self.changeColor(self.rotated_car3_image, color)
                                self.screen.blit(color_image, (col * self.WIDTH, row * self.HEIGHT))
                            else:
                                color = pygame.Color(0)
                                color.hsla = (self.colors[cell_value][0], self.colors[cell_value][1], self.colors[cell_value][2], self.colors[cell_value][3])
                                color_image = self.changeColor(self.rotated_car2_image, color)
                                self.screen.blit(color_image, (col * self.WIDTH, row * self.HEIGHT))
                elif cell_value == 0:
                    pygame.draw.rect(self.screen, WHITE, rect)
                elif cell_value == 1:
                    pygame.draw.rect(self.screen, BLACK, rect)
        pass
    
    def changeColor(self, image, color):
        colouredImage = pygame.Surface(image.get_size())
        colouredImage.fill(color)
    
        finalImage = image.copy()
        finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
        return finalImage
    
    def write_text(self, algoritmus):
        WHITE = (255, 255, 255)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(algoritmus, True, WHITE)
        textRect = text.get_rect()
        textRect.center = ((self.WIDTH * self.columns) // 2, self.HEIGHT // 2)
        self.screen.blit(text, textRect)
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
    
    def display(self,field_array):
        pygame.init()

        WIDTH = 120
        HEIGHT = 120
        if ((len(field_array) != 8) or (len(field_array[0]) != 8)):
            print("Array must have 8x8 size.");
            sys.exit()
        ROWS = len(field_array)
        COLUMNS = len(field_array[0])

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


        screen_width = COLUMNS * WIDTH
        screen_height = ROWS * HEIGHT
        screen=pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
        pygame.display.set_caption('RUSH HOUR')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    screen_width, screen_height = event.size
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

            screen.fill(WHITE)
            
            offset_x = (screen_width - COLUMNS * WIDTH) // 2
            offset_y = (screen_height - ROWS * HEIGHT) // 2

            for row in range(ROWS):
                for col in range(COLUMNS):
                    cell_value = field_array[row][col]
                    rect = pygame.Rect(offset_x + col * WIDTH, offset_y + row * HEIGHT, WIDTH, HEIGHT)

                    if cell_value == 0:
                        pygame.draw.rect(screen, WHITE, rect)
                    elif cell_value == 1:
                        pygame.draw.rect(screen, BLACK, rect)
                    elif cell_value == 2:
                        pygame.draw.rect(screen, RED, rect)
                    elif cell_value == 3:
                        pygame.draw.rect(screen, GREEN, rect)
                    elif cell_value == 4:
                        pygame.draw.rect(screen, BLUE, rect)
                    elif cell_value == 5:
                        pygame.draw.rect(screen, YELLOW, rect)
                    elif cell_value == 6:
                        pygame.draw.rect(screen, MAGENTA, rect)
                    elif cell_value == 7:
                        pygame.draw.rect(screen, CYAN, rect)
                    elif cell_value == 8:
                        pygame.draw.rect(screen, GRAY, rect)
                    elif cell_value == 9:
                        pygame.draw.rect(screen, MAROON, rect)
                    elif cell_value == 10:
                        pygame.draw.rect(screen, OLIVE, rect)
                    elif cell_value == 11:
                        pygame.draw.rect(screen, DARK_GREEN, rect)
                    elif cell_value == 12:
                        pygame.draw.rect(screen, PURPLE, rect)

            pygame.display.flip()

            pygame.time.Clock().tick(30)