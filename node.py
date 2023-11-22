# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:43:51 2023

@author: marti
"""

class Node: 
    def __init__(self, key, field_array): 
        self.key = key 
        self.field_array = field_array 
        self.next = None