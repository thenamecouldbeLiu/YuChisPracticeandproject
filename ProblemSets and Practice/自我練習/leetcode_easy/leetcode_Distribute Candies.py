# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:49:13 2018

@author: Asus
"""

def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    candyType = set(candies)
    return min(len(candyType), len(candies)//2)