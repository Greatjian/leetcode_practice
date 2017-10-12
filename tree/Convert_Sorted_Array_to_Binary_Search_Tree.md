# 108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

## Method:
recursion:

slicing:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sortedArrayToBST(self, nums):
            """
            :type nums: List[int]
            :rtype: TreeNode
            """
            if not nums:
                return
            mid=len(nums)/2
            root=TreeNode(nums[mid])
            root.left=self.sortedArrayToBST(nums[:mid])
            root.right=self.sortedArrayToBST(nums[mid+1:])
            return root
            
index:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def sortedArrayToBST(self, nums):
            """
            :type nums: List[int]
            :rtype: TreeNode
            """
        
            def helper(start, end):
                if start>end:
                    return
                mid=(start+end)/2
                root=TreeNode(nums[mid])
                root.left=helper(start, mid-1)
                root.right=helper(mid+1, end)
                return root
            
            return helper(0, len(nums)-1)