# 866. Smallest Subtree with all the Deepest Nodes

Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in it's subtree.

 

    Example 1:
    
    Input: [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]

    Explanation:
        
    We return the node with value 2, colored in yellow in the diagram.
    The nodes colored in blue are the deepest nodes of the tree.
    The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
    The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
    Both the input and output have TreeNode type.
 

Note:

- The number of nodes in the tree will be between 1 and 500.
- The values of each node are unique.

## Method:

solution is O(n), but it takes three passes which is a little complicated:

1. dfs to get the depth
2. bfs to get all leaves
3. move all leaves upwards each time until they merge into one position
4. return that position TreeNode

code:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def subtreeWithAllDeepest(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            def depth(root):
                if not root:
                    return 0
                return 1+max(depth(root.left),depth(root.right))
            
            dpth=depth(root)
            d={}
            queue=collections.deque([[root, 1]])
            leaf=set()
            while queue:
                root, depth=queue.popleft()
                if depth==dpth:
                    leaf.add(root)
                if root.left:
                    d[root.left]=root
                    queue.append([root.left, depth+1])
                if root.right:
                    d[root.right]=root
                    queue.append([root.right, depth+1])
            
            while len(leaf)!=1:
                nleaf=set()
                for l in leaf:
                    nleaf.add(d[l])
                leaf=nleaf
            return leaf.pop()

## Solution:

one dfs is enough, but one need to track useful information to return (depth and node) each time:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def subtreeWithAllDeepest(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            def dfs(root):
                if not root:
                    return None, 0
                left, right=dfs(root.left), dfs(root.right)
                if left[1]>right[1]:
                    return left[0], left[1]+1
                elif right[1]>left[1]:
                    return right[0], right[1]+1
                else:
                    return root, left[1]+1
                
            return dfs(root)[0]