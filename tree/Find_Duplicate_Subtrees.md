# 652. Find Duplicate Subtrees

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1: 

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

The following are two duplicate subtrees:

      2
     /
    4

and

    4

Therefore, you need to return above trees' root in the form of a list.

## Method:

注意s相同时root不同。

defaultdict(list)+recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findDuplicateSubtrees(self, root):
            """
            :type root: TreeNode
            :rtype: List[TreeNode]
            """
            self.d=collections.defaultdict(list)
            self.helper(root)
            return [v[0] for v in self.d.values() if len(v)>1]
            
            
        def helper(self, root):
            if not root:
                return 'a'
            s=str(root.val)+self.helper(root.left)+self.helper(root.right)
            self.d[s].append(root)
            return s
            
亦可在recursion中加入root:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findDuplicateSubtrees(self, root):
            """
            :type root: TreeNode
            :rtype: List[TreeNode]
            """
            self.res=[]
            self.d=collections.defaultdict(int)
            self.helper(root)
            return self.res
            
            
        def helper(self, root):
            if not root:
                return 'a'
            s=str(root.val)+self.helper(root.left)+self.helper(root.right)
            self.d[s]+=1
            if self.d[s]==2:
                self.res.append(root)
                self.d[s]+=1
            return s
