# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:38:18 2023

@author: marti
"""

"""class Hash():
    def _init_(self,number_of_cars):
        print("ahoj");"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(str(key)) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return
        raise KeyError(f"Key '{key}' not found")

    def contains_2d_array(self, target_array):
        for bucket in self.table:
            if bucket is not None:
                for _, value in bucket:
                    if value == target_array:
                        return True
        return False


# main.py (usage example)
if __name__ == '__main__':
    # Example usage:
    hash_table = HashTable(size=10)

    # Inserting elements
    hash_table.insert("row1", [[1, 2, 3], [4, 5, 6]])
    hash_table.insert("row2", [[7, 8, 9], [10, 11, 12]])

    # Checking if specific 2D arrays are in the hash table
    print(hash_table.contains_2d_array([[1, 2, 3], [4, 5, 6]]))  # Output: True
    print(hash_table.contains_2d_array([[7, 8, 9], [10, 11, 12]]))  # Output: True
    print(hash_table.contains_2d_array([[13, 14, 15], [16, 17, 18]]))  # Output: False