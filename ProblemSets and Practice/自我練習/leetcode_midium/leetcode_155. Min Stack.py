# -*- coding: utf-8 -*-
"""
 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
https://leetcode.com/problems/min-stack/description/
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.item  = []
        self.CurMin =[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.item.append(x)
        if len(self.CurMin)==0 or x<=self.CurMin[-1]:
            self.CurMin.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.item:
            if self.item[-1] == self.CurMin[-1]:
                self.CurMin.pop()
            self.item.pop()
        else:
            return None
    def top(self):
        """
        :rtype: int
        """
        if not self.item:
            return None
        return self.item[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.CurMin:
            return self.CurMin[-1]
        else:
            return None
