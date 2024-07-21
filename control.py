# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:28:39 2023

@author: marti
"""

class Control: 
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
    
    def isFinished(self, field_array):
        for row in range(self.rows):
            if row==0 or row==self.rows-1 :
                for col in range(self.columns):
                    if field_array[row][col]==2:
                        """exit_x_position=col
                        exit_y_position=row
                        break"""
                        return True
            else:
                if field_array[row][0]==2:
                    """exit_x_position=0
                    exit_y_position=row
                    break"""
                    return True
                elif field_array[row][self.columns-1]==2:
                    """exit_x_position=0
                    exit_y_position=row
                    break"""
                    return True
        return False
        """for row in range(self.rows):
            if row==0 or row==self.rows-1 :
                for col in range(self.columns):
                    if field_array[row][col]==0 and field_array[row][col]==2:
                        return True
            else:
                if field_array[row][0]==0 and field_array[row][1]==2:
                    return True
                elif field_array[row][self.columns-1]==0 and field_array[row][self.columns-2]==2:
                    return True
        return False """
        """if exit_y_position==0:
            if field_array[1][exit_x_position]==2:
                return True
            else:
                return False
        elif exit_y_position==self.rows-1:
            if field_array[self.rows-2][exit_x_position]==2:
                return True
            else:
                return False
        elif exit_x_position==0:
            if field_array[exit_y_position][1]==2:
                return True
            else:
                return False
        elif exit_x_position==self.columns-1:
            if field_array[exit_y_position][self.columns-2]==2:
                return True
            else:
                return False
        return False"""