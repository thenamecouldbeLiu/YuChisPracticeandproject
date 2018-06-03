# -*- coding: utf-8 -*-
"""
 Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree. 
https://leetcode.com/problems/maximum-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        MaxNumber = max(nums)
        Maxindex = nums.index(MaxNumber)
        root =TreeNode(MaxNumber)
        root.left = self.constructMaximumBinaryTree(nums[0:Maxindex])
        root.right = self.constructMaximumBinaryTree(nums[Maxindex+1:])
        
        return root