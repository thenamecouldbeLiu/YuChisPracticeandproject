# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 18:14:49 2018

@author: Asus
"""

def max_contig_sum(L):
    result  =[[]]
    i = 0
    while i<len(L):
        j = i+1
        temp = [L[i]]
        result.append([L[i]])
        while j<len(L):
            temp.append(L[j])
            temp_temp = temp.copy()
            result+=[temp_temp]
            j+=1
        i+=1
        
    return max(sum(i) for i in result)
L =[-1,2,3,-4]
print(max_contig_sum(L))