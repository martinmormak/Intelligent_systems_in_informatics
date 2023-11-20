# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:12:26 2023

@author: marti
"""

"""import os

array2D = [[1,1,1,1,1,1,1,1],
[1,5,5,0,3,0,6,1],
[1,8,0,0,3,4,6,1],
[1,8,2,2,3,4,9,1],
[1,8,10,10,10,4,9,1],
[1,7,0,0,0,11,11,1],
[1,7,0,0,0,12,12,1],
[1,1,1,1,1,1,1,1]]

array2D = []

for filename in os.listdir(os.getcwd()):
    if not filename.endswith('.txt'):
        continue

    with open(filename, 'r') as f:
        for line in f.readlines():
            array2D.append(line.split(','))

print(array2D)"""

import pygame
from pygame.locals import*
import random
import sys

import ast

import pandas as pd

file_path = 'field.txt'

with open(file_path, 'r') as file:
    content = file.read()

field_array = ast.literal_eval(content)

for row in field_array:
    print(row)
    
"""def generate_exit(x,y,orientation,field_array,cars):
    random_number = random.randint(0, 1)
    print(random_number)
    if(orientation=="v"):
        if(random_number==0):
            for i in range(1, len(cars)):
                if cars[4][i] == orientation and 1 <= cars[3][i] < y and cars[2][i] == x:
                    for q in range(1, len(cars)):
                        if cars[4][q] == orientation and y < cars[3][q] <= 6 and cars[2][q] == x:
                            print("Problem generate exit")
                            sys.exit()
                    field_array[7][x]=0
                    return field_array
            field_array[0][x]=0
            return field_array
        else:
            for i in range(1, len(cars)):
                if cars[4][i] == orientation and y < cars[3][i] <= 6 and cars[2][i] == x:
                    for q in range(1, len(cars)):
                        if cars[4][q] == orientation and 1 <= cars[3][q] <= y and cars[2][q] == x:
                            print("Problem generate exit")
                            sys.exit()
                    field_array[0][x]=0
                    return field_array
            field_array[7][x]=0
            return field_array
    else:
        if(random_number==0):
            for i in range(1, len(cars)):
                if cars[4][i] == orientation and 1 <= cars[2][i] < x and cars[3][i] == y:
                    for q in range(1, len(cars)):
                        if cars[4][q] == orientation and x < cars[2][q] <= 6 and cars[3][q] == y:
                            print(i)
                            print(q)
                            print("Problem generate exit")
                            sys.exit()
                    field_array[y][7]=0
                    return field_array
            field_array[y][0]=0
            return field_array
        else:
            for i in range(1, len(cars)):
                if cars[4][i] == orientation and x < cars[2][i] <= 6 and cars[3][i] == y:
                    for q in range(1, len(cars)):
                        if cars[4][q] == orientation and 1 <= cars[2][q] <= x and cars[3][q] == y:
                            print("Problem generate exit")
                            sys.exit()
                    field_array[y][0]=0
                    return field_array
            field_array[y][7]=0
            return field_array
    
file_path = 'cars.txt'

# Replace 'your_file.txt' with the actual path to your text file
cars = pd.read_csv(file_path, header=None)


field_array=[[1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,1],
             [1,1,1,1,1,1,1,1]]

color = 2

for i in range(len(cars)):
    if None in cars[0:i+1]:
        print("I found a None value at line", i)
        sys.exit(0)
    
    # Check for duplicate identifiers
    for x in range(len(cars)):
        if i != x and cars[0][i] == cars[0][x]:
            print("Two cars have the same identifier.")
            sys.exit(0)
    
    # Check for size (assuming size is an integer)
    if cars[1][i] not in (2, 3):
        print("Car must have size 2 or 3.")
        sys.exit(0)
    
    # Check for x position
    if not (1 <= cars[2][i] <= 6):
        print("Car must have x position in [1, 6].")
        sys.exit(0)
    
    # Check for y position
    if not (1 <= cars[3][i] <= 6):
        print("Car must have y position in [1, 6].")
        sys.exit(0)
    
    # Check for orientation ('v' or 'h')
    if cars[4][i] not in ('v', 'h'):
        print("Car must have 'v' or 'h' orientation.")
        sys.exit(0)
    
    size = cars[1][i]
    x = cars[2][i]
    y = cars[3][i]
    orientation = cars[4][i]
    if size == 2:
        if orientation == "v":
            if(1 <= y <= 5):
                if(field_array[y][x] == 0 and field_array[y+1][x] == 0):
                    field_array[y][x] = color
                    field_array[y+1][x] = color
                else:
                    print(color)
                    print(y+1)
                    print(x+1)
                    print(y+2)
                    print(x+1)
            else:
                print("i")
                print(i)
                print("x")
                print(x)
                print("y")
                print(y)
        else:
            if(1 <= x <= 5):
                if(field_array[y][x] == 0 and field_array[y][x+1] == 0):
                    field_array[y][x] = color
                    field_array[y][x+1] = color
                else:
                    print(color)
                    print(y+1)
                    print(x+1)
                    print(y+1)
                    print(x+2)
            else:
                print("i")
                print(i)
                print("x")
                print(x)
                print("y")
                print(y)
    else:
        if orientation == "v":
            if(1 <= y <= 4):
                if(field_array[y][x] == 0 and field_array[y+1][x] == 0 and field_array[y+2][x] == 0):
                    field_array[y][x] = color
                    field_array[y+1][x] = color
                    field_array[y+2][x] = color
                else:
                    print(color)
                    print(y+1)
                    print(x+1)
                    print(y+2)
                    print(x+1)
                    print(y+3)
                    print(x+1)
            else:
                print("i")
                print(i)
                print("x")
                print(x)
                print("y")
                print(y)
        else:
            if(1 <= x <= 4):
                if(field_array[y][x] == 0 and field_array[y][x+1] == 0 and field_array[y][x+2] == 0):
                    field_array[y+1][x+1] = color
                    field_array[y+1][x+2] = color
                    field_array[y+1][x+3] = color
                else:
                    print(color)
                    print(y+1)
                    print(x+1)
                    print(y+1)
                    print(x+2)
                    print(y+1)
                    print(x+3)
            else:
                print("i")
                print(i)
                print("x")
                print(x)
                print("y")
                print(y)
    if(color==2):
        field_array=generate_exit(x,y,orientation,field_array,cars)
        
    color = color + 1"""

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