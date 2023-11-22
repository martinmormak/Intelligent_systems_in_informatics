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
        return hash(key) % self.capacity 
  
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

if __name__ == '__main__': 
  
    # Create a hash table with 
    # a capacity of 5 
    ht = HashTable(5) 
  
    # Add some key-value pairs 
    # to the hash table 
    ht.insert("apple", 3) 
    ht.insert("banana", 2) 
    ht.insert("cherry", 5)
  
    # Check if the hash table 
    # contains a key 
    print("apple" in ht)  # True 
    print("durian" in ht)  # False 
  
    # Get the value for a key 
    print(ht.search("banana"))  # 2 
  
    # Update the value for a key 
    ht.insert("banana", 4) 
    print(ht.search("banana"))  # 4 
    
  
    ht.remove("apple") 
    # Check the size of the hash table 
    print(len(ht))  # 3 