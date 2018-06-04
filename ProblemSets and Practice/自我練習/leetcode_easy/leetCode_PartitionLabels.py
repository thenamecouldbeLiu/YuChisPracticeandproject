# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:55:29 2018

@author: Asus
"""

def partitionLabels(S):
    last = {c: i for i, c in enumerate(S)}
    print(last)
    j = anchor = 0
    ans = []
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
            print(i, c)
    return ans