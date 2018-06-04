# -*- coding: utf-8 -*-
"""
 A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.

https://leetcode.com/problems/partition-labels/description/
"""

def partitionLabels(S):
    """
    :type S: str
    :rtype: List[int]
    """
    result =[]
    index_dict={}
    for index in range(len(S)):
        if S[index] not in index_dict:
            index_dict[S[index]] = [index, index]
        else:
            index_dict[S[index]][1] = index
#        index_dict[S[index]] =index
#    li = list(index_dict.items())
    ancher =k = 0
    for i in range(len(S)):
        curLast = index_dict[S[i]][1]
        print("k=",k,"curLast=",curLast,"i=",i ,"anchor=",ancher, "letter=",S[i])
        if curLast>k:
            print("swop")
            k =curLast
        if i==k:
            result.append(i-ancher+1)
            ancher=i+1
    return result