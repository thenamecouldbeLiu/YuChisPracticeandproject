# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:09:42 2018

@author: Asus
"""

def quickSort(nums):
    if len(nums)<=1:
        return nums
    else:
        left_list = []
        right_list =[]
        key_list = []
        key = nums[0]
        for i in nums:
            if i < key:
                left_list.append(i)
            elif i >key:
                right_list.append(i)
            else:
                key_list.append(i)
        left_list = quickSort(left_list)
        right_list= quickSort(right_list)
    return left_list+key_list+right_list