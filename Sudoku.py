#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:24:24 2021

@author: daniele
"""

# Griglia livello expert
grid = [[0,0,0,0,9,0,0,0,4],
        [4,6,0,0,2,0,0,8,1],
        [0,0,1,0,0,0,5,0,7],
        [0,0,0,0,4,1,7,0,0],
        [2,0,0,0,0,0,0,3,8],
        [8,0,0,0,7,0,0,0,0],
        [7,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,4,6,0,9],
        [0,5,4,0,0,8,0,0,0]]

# Stampa griglia dove ci sono 0 sostituisco con punto
def print_grid():
    for line in grid:
        for square in line:
            if square == 0:
                print(".",end=" ")
            else:
                print(square,end=" ")
        print()
        
# Cercare la posizione ottimale
def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i] [x0+j] == n:
                return False
    return True

# Risoluzione con utilizzo di possible()
def solve():
    global grid
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print_grid()
    input("More?")
        
        
        
        
        
        
