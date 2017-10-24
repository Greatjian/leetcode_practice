# 654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]

Output: return the tree root node representing the following tree:

          6
        /   \
       3     5
        \    / 
         2  0   
           \
            1

Note:
- The size of the given array will be in the range [1,1000].

## Method:

recursion:

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
                return
            m=max(nums)
            root=TreeNode(m)
            idx=nums.index(m)
            root.left=self.constructMaximumBinaryTree(nums[:idx])
            root.right=self.constructMaximumBinaryTree(nums[idx+1:])
            return root
            
index更慢：

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
            
            def helper(s, e):
                if s>e:
                    return
                m=max(nums[s:e+1])
                root=TreeNode(m)
                idx=nums.index(m)
                root.left=helper(s, idx-1)
                root.right=helper(idx+1, e)
                return root
            
            return helper(0, len(nums)-1)

## Solution:

iterative method:

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
            stack=[]
            for num in nums:
                node=TreeNode(num)
                while len(stack)!=0 and stack[-1].val<node.val:
                    node.left=stack[-1]
                    stack.pop()
                if len(stack)!=0:
                    stack[-1].right=node
                stack.append(node)
            return stack[0]
            