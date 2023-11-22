# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:49:59 2023

@author: marti
"""

from control import Control
from hashtable import HashTable

class DFS:
    def __init__(self, field_array):
        self.stack.append(field_array)
        self.control = Control()
        self.explored_set = HashTable()
        
    def expand(self,initial_state):
        stack = []
        stack.append(initial_state,0)
        
        while stack:
            current_state, path = stack.pop()

            if current_state in self.explored_set:
                continue

            if self.control.isFinished(current_state):
                return path

            self.explored_set.add(current_state)

            """for successor, action in get_successors(current_state):
                if successor not in explored_set:
                    stack.append((successor, path + [action]))"""

        return None