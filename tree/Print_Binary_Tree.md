# 655. Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:

- The row number m should be equal to the height of the given binary tree.
- The column number n should always be an odd number.
- The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
- Each unused space should contain an empty string "".
- Print the subtrees following the same rules.

Example 1:

Input:

         1
        /
       2

Output:

    [["", "1", ""],
     ["2", "", ""]]

Example 2:

Input:

         1
        / \
       2   3
        \
         4

Output:

    [["", "", "", "1", "", "", ""],
     ["", "2", "", "", "", "3", ""],
     ["", "", "4", "", "", "", ""]]

Example 3:

Input:

          1
         / \
        2   5
       / 
      3 
     / 
    4 

Output:

    [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
     ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
     ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
     ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

Note: The height of binary tree is in the range of [1, 10].

## Method:

recursion:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def printTree(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[str]]
            """
            
            def depth(root):
                if not root:
                    return 0
                return max(depth(root.left), depth(root.right))+1
            
            d=depth(root)
            res=[['']*(2**d-1) for _ in range(d)]
            
            def helper(root, i, j, depth):
                if not root:
                    return
                res[i][j]=str(root.val)
                helper(root.left, i+1, j-2**(depth-2), depth-1)
                helper(root.right, i+1, j+2**(depth-2), depth-1)
            
            helper(root, 0, 2**(d-1)-1, d)    
            
            return res
            