# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:04:45 2023

@author: zorka
"""


from control import Control
from hashtable import HashTable
import copy
import pygame

class Greedy:
    
    def __init__(self, rows, columns, count, gui):
        
        self.rows = rows
        self.columns = columns
        self.control = Control(rows, columns)
        self.explored_set = HashTable(count)
        self.gui=gui
        
    def solve(self, initial_state): 
        #self.find_heuristics(initial_state)
        print(self.find_heuristics(initial_state))
        
        
    def find_heuristics(self, field_array):
        
        for row in range(self.rows):
            if row==0 or row==self.rows-1 :
                for col in range(self.columns):
                    if field_array[row][col]==0:
                        exit_x_position=col
                        exit_y_position=row
                        break
                        
                    if field_array[row][col]==2:
                        return 0
                  

            else:
                if field_array[row][0]==0:
                    exit_x_position=0
                    exit_y_position=row
                    break
    
                elif field_array[row][self.columns-1]==0:
                    exit_x_position=self.columns-1
                    exit_y_position=row
                    break
      
                
                elif field_array[row][0]==2:
                    
                    return 0
                elif field_array[row][self.columns-1]==2:
                    
                    return 0
                
        #print(exit_x_position, exit_y_position)
        
        no_of_cars = 0
        distance = 0
        if exit_y_position == 0:
            y = 0;           
            while field_array[y][exit_x_position] != 2:
                distance += 1
                if field_array[y][exit_x_position] != 0 :
                    no_of_cars += 1
                y += 1
            
        elif exit_y_position == self.rows - 1:
            y = self.rows - 1;           
            while field_array[y][exit_x_position] != 2:
                distance += 1
                if field_array[y][exit_x_position] != 0 :
                    no_of_cars += 1
                y -= 1
                
        if exit_x_position == 0:
            x = 0;           
            while field_array[exit_y_position][x] != 2:
                distance += 1
                if field_array[exit_y_position][x] != 0 :
                    no_of_cars += 1
                x += 1
            
        elif exit_x_position == self.rows - 1:
            x = self.rows - 1;           
            while field_array[exit_y_position][x] != 2:
                distance += 1
                if field_array[exit_y_position][x] != 0 :
                    no_of_cars += 1
                x -= 1
                
        return no_of_cars + distance
                
            
            
                
                
        