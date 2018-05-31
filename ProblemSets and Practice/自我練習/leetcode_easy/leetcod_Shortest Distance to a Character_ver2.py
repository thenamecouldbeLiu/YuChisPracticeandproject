# -*- coding: utf-8 -*-
"""
Created on Thu May 31 18:36:54 2018

@author: Asus
"""

def Distance(S,C):
        C_index= []
        for i in range(len(S)):
            if S[i]==C:
                C_index.append(i)
        current_C = 0
        result =[]
        for j in range(len(S)):
    
            if j+1<len(S) and S[j]==C  and S[j+1]==C:
                result.append(0)
                current_C+=1
            else:
                if S[j]==C:
                    result.append(0)
                elif current_C<len(C_index)-1 and abs(C_index[current_C+1]-j)<abs(C_index[current_C]-j):
                    current_C+=1
                    result.append(abs(C_index[current_C]-j))
                else:
                    result.append(abs(C_index[current_C]-j))
        return result