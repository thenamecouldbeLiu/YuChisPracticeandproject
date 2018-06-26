# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 22:57:14 2018

@author: Asus
"""

def hasAlternatingBits( n):
    """
    :type n: int
    :rtype: bool
    """

    for i in range(2,len(bin(n))-1):
        if bin(n)[i]==bin(n)[i+1]:
            return False

    return True
        