# -*- coding: utf-8 -*-
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

https://leetcode.com/problems/single-number/description/
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        item_dict ={}
        for item in nums:
            if item_dict.has_key(item):
                item_dict[item]+=1
            else:
                item_dict[item]=1
        for item in item_dict:
            if item_dict[item]==1:
                return item