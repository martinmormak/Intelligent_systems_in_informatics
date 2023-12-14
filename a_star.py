# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:31:55 2023

@author: zorka
"""



from control import Control
from hashtable import HashTable
import copy
import pygame
import heapq

class A_star:
    
    def __init__(self, rows, columns, count, gui):
        
        self.rows = rows
        self.columns = columns
        self.control = Control(rows, columns)
        self.explored_set = HashTable(count)
        self.gui=gui
        
    def solve(self, initial_state, delay): 
        #self.find_heuristics(initial_state)
        #print(self.find_heuristics(initial_state))
        visited_states=set()
        
        stack = []
        heuristic = self.find_heuristics(initial_state)
        cost=0;
        heapq.heappush(stack, (heuristic + cost, heuristic, cost, initial_state, '1 1'))
        sw=self.gui.screen_width
        w=self.gui.WIDTH
        sh=self.gui.screen_height
        h=self.gui.HEIGHT
        expanded_states=0
        maximal_stack_size=len(stack)
        
        while stack:
            heapq.heapify(stack)
            path_function, heuristic, cost, current_state, path = heapq.heappop(stack)
            
            self.gui.handle_events()
            self.gui.screen.fill((255, 255, 255))
            offset_x = (sw - len(current_state[0]) * w) // 2
            offset_y = (sh - len(current_state) * h) // 2
            self.gui.draw_grid(current_state, offset_x, offset_y)
            self.gui.write_text("A*")
            self.gui.update_display()
            pygame.time.Clock().tick(delay)
            
            """print("from")
            for row in current_state:
                print(row)"""
            
            expanded_states=expanded_states+1
            if(len(stack)>maximal_stack_size):
                maximal_stack_size=len(stack)
            
            tuple_of_tuples = tuple(tuple(row) for row in current_state)
            #if tuple_of_tuples in visited_states:
                #print("True in set")
                #continue

            if self.explored_set.contains_2d_array(current_state):
                #print("True")
                continue
            
            if self.control.isFinished(current_state):
                print("Maximal stack size in A*")
                print(maximal_stack_size)
                print("Number of expanded states in A*")
                print(expanded_states)
                print("Cost of expanded states in A*")
                print(cost)
                return path

            #self.explored_set.insert(path, current_state)
            self.explored_set.insert(path,current_state)
            
            visited_states.add(tuple_of_tuples)
            
            new_cost=cost+1;
            for successor, action in self._expand(current_state):
                """if any(state[3] == successor for state in stack):
                    continue
                else:
                    if self.explored_set.contains_2d_array(successor):
                        continue
                    else:
                        new_heuristic = self.find_heuristics(successor)
                        heapq.heappush(stack, (new_heuristic + new_cost, new_heuristic, new_cost, successor, action))"""
                if self.explored_set.contains_2d_array(successor):
                    continue
                else:
                    new_heuristic = self.find_heuristics(successor)
                    heapq.heappush(stack, (new_heuristic + new_cost, new_heuristic, new_cost, successor, action))
               #stack.append((successor, action))
               #new_heuristic = self.find_heuristics(successor)
               #heapq.heappush(stack, (new_heuristic + new_cost, new_heuristic, new_cost, successor, action))
                
            
        print("Maximal stack size in A*")
        print(maximal_stack_size)
        print("Number of expanded states in A*")
        print(expanded_states)
        return None
        
        
    def _expand(self,current_state):
            moves = []
            visited_cars=set()
            """north=False
            south=False
            east=False
            west=False"""
            for row in range(self.rows):
                for col in range(self.columns):
                    if(current_state[row][col]!=0 and current_state[row][col]!=1):
                        if(current_state[row][col] not in visited_cars):
                            visited_cars.add(current_state[row][col])
                            """if(row!=1):
                                north=True
                            else:
                                north=False
                            if(row!=range(current_state)-1):
                                south=True
                            else:
                                south=False
                            if(col!=1):
                                west=True
                            else:
                                west=False
                            if(col!=range(current_state[0])-1):
                                east=True
                            else:
                                east=False"""
                            if(row>0 and current_state[row][col]==current_state[row+1][col]):
                                row_after=1
                                while(current_state[row][col]==current_state[row+row_after][col]):
                                    row_after=row_after+1
                                    if(row+row_after>self.rows-1):
                                        row_after=row_after-1
                                        break
                                if(current_state[row-1][col]==0):
                                    new_state = copy.deepcopy(current_state)
                                    new_state[row-1][col]=new_state[row][col]
                                    new_state[row+row_after-1][col]=0
                                    moves.append((new_state,'N '+str(current_state[row][col])))
                                        
                                if(current_state[row+row_after][col]==0):
                                    new_state = copy.deepcopy(current_state)
                                    new_state[row+row_after][col]=new_state[row][col]
                                    new_state[row][col]=0
                                    moves.append((new_state,'S '+str(current_state[row][col])))
                            if(col>0 and current_state[row][col]==current_state[row][col+1]):
                                column_after=1
                                while(current_state[row][col]==current_state[row][col+column_after]):
                                    column_after=column_after+1
                                    if(col+column_after>self.columns-1):
                                        column_after=column_after-1
                                        break
                                if(current_state[row][col-1]==0):
                                    new_state = copy.deepcopy(current_state)
                                    new_state[row][col-1]=new_state[row][col]
                                    new_state[row][col+column_after-1]=0
                                    moves.append((new_state,'W '+str(current_state[row][col])))
                                        
                                if(current_state[row][col+column_after]==0):
                                    new_state = copy.deepcopy(current_state)
                                    new_state[row][col+column_after]=new_state[row][col]
                                    new_state[row][col]=0
                                    moves.append((new_state,'E '+str(current_state[row][col])))
            return moves
        
        
        
        
        
        
        
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
                
        no_of_cars = 0
        return no_of_cars + distance
                
            
            
                
                
        