# -*- coding: utf-8 -*-
"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
https://leetcode.com/problems/shortest-distance-to-a-character/description/
"""
class Solution(object):
    def shortestToChar(self,S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = []
        current_closest_C= len(S)
        for i in range(len(S)):
            for j in range(i, len(S)):
                if S[j]==C and j-i<abs(current_closest_C-i):
                    current_closest_C=j
    
            result.append(abs(current_closest_C-i))
        return result
"""
Better Solution
#class Solution(object):
#    def shortestToChar(self, S, C):
#        prev = float('-inf')
#        ans = []
#        for i, x in enumerate(S):
#            if x == C: prev = i
#            ans.append(i - prev)
#
#        prev = float('inf')
#        for i in xrange(len(S) - 1, -1, -1):
#            if S[i] == C: prev = i
#            ans[i] = min(ans[i], prev - i)
#
#        return ans