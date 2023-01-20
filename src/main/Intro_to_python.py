#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:38:32 2023

@author: Janny Velazquez
"""

import numpy as np

def Intro():
    #Print a specific 3x3 matrix where a cell is 1 if i == j, else 0 
    matrix = np.identity(3)
    print(matrix)


    #Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠j  
    matrix2=np.where(matrix !=0, matrix, matrix+3)
    print(matrix2)


    #Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created
    matrix3=np.delete(matrix2, 2,1)
    print(matrix3)


    return

Intro()
