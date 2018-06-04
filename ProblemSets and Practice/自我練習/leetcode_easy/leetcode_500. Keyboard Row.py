# -*- coding: utf-8 -*-
"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

American keyboard

Example 1:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
https://leetcode.com/problems/keyboard-row/description/
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans =[]
        alph = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL","zxcvbnmZXCVBNM"]
        row_dict = {}
        for item in alph:
            for letter in item:
                row_dict[letter] =item

        for item in words:
            if len(item)>1:
                for index in range(len(item)-1):
                    if row_dict[item[index]]!=row_dict[item[index+1]]:
                        print("hre")
                        break
                    elif index+1==len(item)-1:
                        ans.append(item)
            else:
                ans.append(item)
        return ans
                