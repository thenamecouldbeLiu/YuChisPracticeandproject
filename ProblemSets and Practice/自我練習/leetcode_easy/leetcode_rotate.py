# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 21:47:22 2018

@author: Asus
"""

def rotate(nums, k):
    nums[:]=nums[(len(nums)-k):]+nums[:(len(nums)-k)]
