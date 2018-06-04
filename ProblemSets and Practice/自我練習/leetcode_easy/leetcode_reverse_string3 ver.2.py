# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 00:19:43 2018

@author: Asus
"""

def reverseWords(s):
    aws = ""
    j = -1
    for i in range(len(s)):
        if s[i]==" ":
           for k in range(i,j,-1):
                aws+=s[k]
           j =i
        elif i ==len(s)-1:
            last=""
            for k in range(i,j,-1):
                last+=s[k]
            aws+=" "+last
    return aws[1:]
     