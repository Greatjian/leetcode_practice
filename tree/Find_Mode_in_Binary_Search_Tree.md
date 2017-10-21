# 501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

For example:

Given BST [1,null,2,2],

       1
        \
         2
        /
       2
       
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

## Method:

dict.items() and dict.values(), O(n) space:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findMode(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if not root:
                return []
            self.d=collections.defaultdict(int)
            self.helper(root)
            m=max(self.d.values())
            return [k for k, v in self.d.items() if v==m]
            
        def helper(self, root):
            if not root:
                return
            self.d[root.val]+=1
            self.helper(root.left)
            self.helper(root.right)
            
inorder traversal, O(1) space:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def findMode(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if not root:
                return []
            res=[]
            stack=[]
            prev=None
            curCount=0
            maxCount=0
            while root or stack:
                while root:
                    stack.append(root)
                    root=root.left
                root=stack.pop()
                if prev==None:
                    prev=root.val
                    curCount+=1
                else:
                    if root.val==prev:
                        curCount+=1
                    else:
                        if curCount==maxCount:
                            res.append(prev)
                        if curCount>maxCount:
                            maxCount=curCount
                            res=[prev]
                        curCount=1
                        prev=root.val
                root=root.right
            if curCount==maxCount:
                res.append(prev)
            if curCount>maxCount:
                res=[prev]
            return res