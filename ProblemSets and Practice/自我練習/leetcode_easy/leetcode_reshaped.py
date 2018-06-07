# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 00:08:18 2018

@author: Asus
"""

def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    new_list =[]
    reshaped_ele =r*c
    for item in nums:
        if len(nums[0])!=len(item) or len(nums)*len(item)!=reshaped_ele:
            return nums
        else:
            for ele in item:
                new_list.append(ele)
    print(new_list)
    reshaped_matrix=[]
    idx=0
    for i in range(r):
        box =[]
        for j in range(c):
            box.append(new_list[idx])
            idx+=1
        reshaped_matrix.append(box)
    return reshaped_matrix