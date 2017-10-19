# 437. Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

## Method:

记录求和并判断是否包含：

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def pathSum(self, root, sum):
            """
            :type root: TreeNode
            :type sum: int
            :rtype: int
            """
            self.count=0
            self.helper(root, [], sum)
            return self.count
            
        def helper(self, root, s, sum):
            if not root:
                return
            s=[root.val]+[root.val+ i for i in s]
            self.count+=s.count(sum)
            self.helper(root.left, s, sum)
            self.helper(root.right, s, sum)
            
## Solution:

using dict for memorization:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def pathSum(self, root, sum):
            """
            :type root: TreeNode
            :type sum: int
            :rtype: int
            """
            self.count=0
            self.d={0:1}
            self.helper(root, 0, sum)
            return self.count
            
        def helper(self, root, path, sum):
            if not root:
                return
            path+=root.val
            if path-sum in self.d:
                self.count+=self.d[path-sum]
            if path not in self.d:
                self.d[path]=1
            else:
                self.d[path]+=1
            self.helper(root.left, path, sum)
            self.helper(root.right, path, sum)
            self.d[path]-=1
            
也可设置defaultdict:

    self.d=collections.defaultdict(int)
    self.d[0]=1

这样函数中可直接

    self.d[path]+=1
    self.helper(root.left, path, sum)
    self.helper(root.right, path, sum)
    self.d[path]-=1