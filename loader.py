# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:18:54 2023

@author: marti
"""

import ast
import sys
import random
import pandas as pd

class Loader:
    def load_field(self,level):
        file_path = 'levels/level'+str(level)+'.txt'
        
        with open(file_path, 'r') as file:
            content = file.read()

        field_array = ast.literal_eval(content)

        """for row in field_array:
            print(row)"""
        return field_array
    
    def generate_exit(self,x,y,orientation,field_array,cars):
        random_number = random.randint(0, 1)
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
    
    def load_cars(self):
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
                        """else:
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
                        print(y)"""
                else:
                    if(1 <= x <= 5):
                        if(field_array[y][x] == 0 and field_array[y][x+1] == 0):
                            field_array[y][x] = color
                            field_array[y][x+1] = color
                        """else:
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
                        print(y)"""
            else:
                if orientation == "v":
                    if(1 <= y <= 4):
                        if(field_array[y][x] == 0 and field_array[y+1][x] == 0 and field_array[y+2][x] == 0):
                            field_array[y][x] = color
                            field_array[y+1][x] = color
                            field_array[y+2][x] = color
                        """else:
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
                        print(y)"""
                else:
                    if(1 <= x <= 4):
                        if(field_array[y][x] == 0 and field_array[y][x+1] == 0 and field_array[y][x+2] == 0):
                            field_array[y+1][x+1] = color
                            field_array[y+1][x+2] = color
                            field_array[y+1][x+3] = color
                        """else:
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
                        print(y)"""
            if(color==2):
                field_array=self.generate_exit(x,y,orientation,field_array,cars)
        
            color = color + 1
        return field_array