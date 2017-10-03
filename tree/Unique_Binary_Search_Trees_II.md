# 95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,

    Given n = 3, your program should return all 5 unique BST's shown below.
    
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

## Method:

1. 根节点可以任取min ~ max (例如min  = 1, max = n)，假如取定为i。
2. 则left subtree由min ~ i-1组成，假设可以有L种可能。right subtree由i+1 ~ max组成，假设有R种可能。生成所有可能的left/right subtree。
3. 对于每个生成的left subtree/right subtree组合<T_left(p), T_right(q)>，p = 1...L，q = 1...R，添加上根节点i而组成一颗新树。


    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def generateTrees(self, n):
            """
            :type n: int
            :rtype: List[TreeNode]
            """
            if n==0:
                return []
            return self.dfs(1,n)
        
        def dfs(self, start, end):
            if start>end:
                return [None]
            res=[]
            for rootval in range(start, end+1):
                leftTree=self.dfs(start,rootval-1)
                rightTree=self.dfs(rootval+1,end)
                for i in leftTree:
                    for j in rightTree:
                        root=TreeNode(rootval)
                        root.left=i
                        root.right=j
                        res.append(root)
            return res