# -*- coding: utf-8 -*-
"""
 Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

https://leetcode.com/problems/find-the-difference/description/
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dic ={}
        for i in s:
            if i not in s_dic:
                s_dic[i]=s.count(i)
        for l in set(t):
            if l not in s_dic or s_dic[l]!=t.count(l):
                return l
                