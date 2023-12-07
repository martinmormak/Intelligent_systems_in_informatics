# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:47:30 2023

@author: marti
"""

import pygame
from dfs import DFS
from greedy import Greedy
import time
from a_star import A_star

class Game:
    def __init__(self, gui, loader):
        self.gui = gui
        self.loader = loader
        self.dfs = None
        self.greedy = None
        self.a_star = None
        self.dfs_solve=False
        self.greedy_solve=False
        self.a_star_solve=False

    def main_loop(self):
        field_array = self.loader.load_field()
        maximum=field_array[0][0]
        for row in field_array:
            for col in row:
                if col>maximum:
                    maximum=col
        self.dfs=DFS(8,8,maximum,self.gui)
        self.greedy=Greedy(8,8,maximum,self.gui)
        self.a_star=A_star(8,8,maximum,self.gui)
        
        sw=self.gui.screen_width
        w=self.gui.WIDTH
        sh=self.gui.screen_height
        h=self.gui.HEIGHT
        
        initial_state = field_array
        
        DFS_solution = self.dfs.solve(initial_state)
        
        if DFS_solution:
            print("DFS found solution")
        else:
            print("DFS did't found solution")
        
        #self.greedy.solve(field_array);
        
        time.sleep(3)
        
        greedy_solution = self.greedy.solve(field_array)
        
        if greedy_solution:
            print("Greedy found solution")
        else:
            print("Greedy did't found solution")
        
        time.sleep(3)
        
        a_star_solution = self.a_star.solve(field_array)
        
        if a_star_solution:
            print("A* found solution")
        else:
            print("A* did't found solution")
        
        time.sleep(3)
        
        pygame.quit()
 
        """
        for row in initial_state:
            print(row)
        

        if solution_path:
            print("DFS found solution")
        else:
            print("DFS did't found solution")
        self.dfs_solve=True
        
        time.sleep(5)
        
        
        
        
        
        
        while True:
            self.gui.handle_events()
            self.gui.screen.fill((255, 255, 255))
            offset_x = (sw - len(field_array[0]) * w) // 2
            offset_y = (sh - len(field_array) * h) // 2
            self.gui.draw_grid(field_array, offset_x, offset_y)
            self.gui.update_display()
            pygame.time.Clock().tick(30)
            if(self.dfs_solve==False and self.greedy_solve==False and self.a_star_solve==False):
                solution_path = self.dfs.solve(initial_state)

                if solution_path:
                    print("DFS found solution")
                else:
                    print("DFS did't found solution")
                self.dfs_solve=True
        
        self.gui.display(field_array)
        print("HELLO")
        
        solution_path = self.dfs.expand(field_array)
        print(solution_path)
        print("HELLO")
        if solution_path:
            print("DFS found solution")
        else:
            print("DFS did't found solution")"""
