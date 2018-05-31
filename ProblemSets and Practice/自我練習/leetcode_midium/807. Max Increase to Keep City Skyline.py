# -*- coding: utf-8 -*-
"""
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
"""

#class Solution(object):
def maxIncreaseKeepingSkyline(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    
    long = len(grid)
    grid_new= [[0 for i in range(long)]for i in range(long)]
    Max_Y_Cor = [0 for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[j][i]>Max_Y_Cor[i]:
                Max_Y_Cor[i]=grid[j][i]
    Max_X_Cor=[max(i) for i in grid]
    result =0
    for i in range(long):
        for j in range(long):
            if Max_X_Cor[j]>=Max_Y_Cor[i]:
                grid_new[j][i] =Max_Y_Cor[i]
            else:
                grid_new[j][i] =Max_X_Cor[j]
    for item1 in grid_new:
        result+= sum(item1)
    for item in grid:
        result -=sum(item)
    return result
grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(maxIncreaseKeepingSkyline(grid))