# 671. Second Minimum Node In a Binary Tree

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 

        2
       / \
      2   5
         / \
        5   7

Output: 5

Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:

Input: 

        2
       / \
      2   2

Output: -1

Explanation: The smallest value is 2, but there isn't any second smallest value.

## Method:

recursion:

using set to remove duplicates:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findSecondMinimumValue(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.s=set()
            self.helper(root)
            if len(self.s)<2:
                return -1
            self.s.remove(min(self.s)) // self.s.remove(root.val) would be faster
            return min(self.s)
            
        def helper(self, root):
            if not root:
                return
            self.s.add(root.val)
            self.helper(root.left)
            self.helper(root.right)
            
using one variable to save space:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findSecondMinimumValue(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            self.r=root.val
            self.res=float('inf')
            self.helper(root)
            return -1 if self.res==float('inf') else self.res
            
        def helper(self, root):
            if not root:
                return
            if root.val>self.r:
                self.res=min(self.res, root.val)
            self.helper(root.left)
            self.helper(root.right)