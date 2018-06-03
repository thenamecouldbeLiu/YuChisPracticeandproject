# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 11:12:16 2018

@author: Asus
"""

def largestPalindrome(n):
    """
    :type n: int
    :rtype: int
    """
    def isPalindrome(number):
        number  =str(number)
        i = 0
        j= len(number)-1
        if len(number)>2:
            if len(number)%2!=0:
                while i < (len(number)-1)/2 and j> (len(number)-1)/2:
    #                print(number[i],i,number[j],j)
                    if number[i]!=number[j]:
                        return False
                    i+=1
                    j-=1
                return True
            else:
                while i < (len(number))/2 and j> (len(number))/2:
    #                print(number[i],i,number[j],j)
                    if number[i]!=number[j]:
                        return False
                    i+=1
                    j-=1
                return True    
        else:
            return number[i]==number[j]