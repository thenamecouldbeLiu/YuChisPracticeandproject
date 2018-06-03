# -*- coding: utf-8 -*-
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
https://leetcode.com/submissions/detail/157083718/
"""

def longestCommonPrefix(strs):
    if len(strs)==0:
        return ""
    if len(strs)==1:
        return strs[0]
    
    min_Scan = min(strs, key= len)
    scan_Time = len(min_Scan)
    for i in range(scan_Time):
        for item in strs:
            if item[i]!=min_Scan[i]:
                return min_Scan[:i]
        
    return min_Scan