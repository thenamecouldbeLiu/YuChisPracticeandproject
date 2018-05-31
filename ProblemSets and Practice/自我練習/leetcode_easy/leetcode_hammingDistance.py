# -*- coding: utf-8 -*-
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
https://leetcode.com/problems/hamming-distance/description/
"""

class Solution(object):
    def hammingDistance(self,x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x,y = bin(x)[2:].zfill(64),bin(y)[2:].zfill(64)
        hammingDistance = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                hammingDistance +=1
        return hammingDistance