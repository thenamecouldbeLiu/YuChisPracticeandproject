# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:10:19 2018

@author: Asus
"""

def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    4 6 8 10
    4+(4-N)
    N為該格四周有幾個1
    """
    perimeter =0
    for i in range(len(grid)):#Y軸 or row
        for j in range(len(grid[i])):#X軸 or colum
            if grid[i][j]==1:
                perimeter+=4
                try:
                    
                    if i>0 and grid[i-1][j]==1:
                        perimeter-=1
                    if j>0 and grid[i][j-1]==1:
                        perimeter-=1
                    if i<len(grid)-1 and grid[i+1][j]== 1:
                        perimeter-=1
                    if j< len(grid[i]) and grid[i][j+1]==1:
                        perimeter-=1
#                    print("grid now", i, j,"perimeter=", perimeter)
                except IndexError:
                    continue
                    
    return perimeter