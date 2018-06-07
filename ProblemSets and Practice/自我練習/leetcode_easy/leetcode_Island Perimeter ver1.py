# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:33:51 2018

@author: Asus
"""

class Solution(object):
    def islandPerimeter(self,grid):
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
                testCor =[(i+1,j),(i-1,j),(i,j-1), (i,j+1)]
    #            land_near=0
    #            print("grid",i,j)
    #            print("P now",perimeter,"\b")
                if grid[i][j]==1:
                    perimeter+=4
    #                print("grid",i,j,"+4")
                    for cord in testCor:
                        try:
                            if cord[0]>=0 and cord[1]>=0 and grid[cord[0]][cord[1]]==1:
                                perimeter-=1
    #                            print("testing",cord,"-1")

                        except IndexError:
    #                        print("exception")
    #                        perimeter-=1
                            continue

        return perimeter