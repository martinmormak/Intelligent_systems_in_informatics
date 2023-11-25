# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:38:18 2023

@author: marti
"""

"""class Hash():
    def _init_(self,number_of_cars):
        print("ahoj");"""

from node import Node        
        
class HashTable: 
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.table = [None] * capacity
  
    def _hash(self, key):
        parts = key.split()
        return int(parts[1])-1
  
    def insert(self, key, field_array):
        index = self._hash(key)
        
        if self.table[index] is None: 
            self.table[index] = Node(key, field_array) 
            self.size += 1
        else: 
            current = self.table[index] 
            while current: 
                if current.key == key: 
                    current.field_array = field_array 
                    return
                current = current.next
            new_node = Node(key, field_array) 
            new_node.next = self.table[index] 
            self.table[index] = new_node 
            self.size += 1
  
    def search(self, key): 
        index = self._hash(key) 
  
        current = self.table[index] 
        while current: 
            if current.key == key: 
                return current.field_array 
            current = current.next
  
        raise KeyError(key) 
  
    def remove(self, key): 
        index = self._hash(key) 
  
        previous = None
        current = self.table[index] 
  
        while current: 
            if current.key == key: 
                if previous: 
                    previous.next = current.next
                else: 
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current 
            current = current.next
  
        raise KeyError(key) 
  
    def __len__(self): 
        return self.size 
  
    def __contains__(self, key): 
        try: 
            self.search(key) 
            return True
        except KeyError: 
            return False

    def contains_array(self, target_array):
        for node in self.table:
            current = node
            while current:
                if current.field_array == target_array:
                    return True
                current = current.next
        return False

# main.py (usage example)
if __name__ == '__main__':
    ht = HashTable(5)

    a1 = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 5, 5, 0, 3, 0, 6, 1],
          [1, 8, 0, 0, 3, 4, 6, 1],
          [1, 8, 2, 2, 3, 4, 9, 0],
          [1, 8, 0, 0, 0, 4, 9, 1],
          [1, 7, 0, 0, 0, 0, 0, 1],
          [1, 7, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]]

    a2 = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 5, 5, 0, 3, 4, 6, 1],
          [1, 8, 0, 0, 3, 4, 6, 1],
          [1, 8, 2, 2, 3, 4, 9, 0],
          [1, 8, 0, 0, 0, 0, 9, 1],
          [1, 7, 0, 0, 0, 0, 0, 1],
          [1, 7, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]]

    a3 = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 5, 5, 0, 3, 0, 6, 1],
          [1, 8, 0, 0, 3, 4, 6, 1],
          [1, 8, 2, 2, 3, 4, 9, 0],
          [1, 8, 0, 0, 0, 4, 9, 1],
          [1, 7, 0, 0, 0, 0, 0, 1],
          [1, 7, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]]

    ht.insert("a 0", a1)
    
    
    print(ht.contains_array(a1))
    print(ht.contains_array(a2))
    print(ht.contains_array(a3))

    ht.insert("a 4", a2)
    
    
    print(ht.contains_array(a1))
    print(ht.contains_array(a2))
    print(ht.contains_array(a3))
    
    
    ht.insert("a 1", a3)

    print(ht.contains_array(a1))
    print(ht.contains_array(a2))
    print(ht.contains_array(a3))