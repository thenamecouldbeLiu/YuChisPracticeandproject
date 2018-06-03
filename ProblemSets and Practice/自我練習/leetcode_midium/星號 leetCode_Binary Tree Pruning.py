# -*- coding: utf-8 -*-
"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
https://leetcode.com/problems/binary-tree-pruning/description/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        root.right = self.pruneTree(root.right)
        root.left =self.pruneTree(root.left)
        
        if root.val ==0 and not root.right and not root.left:
            root =None
        return root
    