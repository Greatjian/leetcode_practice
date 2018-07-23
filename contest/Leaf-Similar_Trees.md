# 872. Leaf-Similar Trees

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Note:

- Both of the given trees will have between 1 and 100 nodes.

## Method:

dfs:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def leafSimilar(self, root1, root2):
            """
            :type root1: TreeNode
            :type root2: TreeNode
            :rtype: bool
            """
            return self.getRoot(root1)==self.getRoot(root2)
            
        def getRoot(self, root):
            res=[]
            stack=[root]
            while stack:
                node=stack.pop()
                if not node.left and not node.right:
                    res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return res