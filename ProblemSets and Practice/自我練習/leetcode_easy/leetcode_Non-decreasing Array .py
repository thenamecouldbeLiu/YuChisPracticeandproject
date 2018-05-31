# -*- coding: utf-8 -*-
"""
 Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
https://leetcode.com/problems/non-decreasing-array/description/
"""


def checkPossibility(nums):
    remove_counter = 0
    time= 1
    length=len(nums)
    while time<length-1:
        if not nums[time]<=nums[time+1]:
            remove_counter+=1
            if remove_counter>1:
                return False
            else:
                if nums[time-1]<=nums[time+1]:
                    del(nums[time])
                    time=0
                    length-=1
                else:
                    del(nums[time+1])
                    time=0
                    length-=1
        else:            
            time+=1
    return True
            
            
def auto_test(li):
    for item in li:
        print(checkPossibility(item),item)
        
li =[[-1,4,2,3],[2,3,3,2,4],[3,4,2,3],[-1,4,2,3],[4,2,3],[4,2,1]]
auto_test(li)