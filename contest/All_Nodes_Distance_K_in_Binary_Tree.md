# 863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
    
    Output: [7,4,1]
    
    Explanation: 
    The nodes that are a distance 2 from the target node (with value 5)
    have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

- The given tree is non-empty.
- Each node in the tree has unique values 0 <= node.val <= 500.
- The target node is a node in the tree.
- 0 <= K <= 1000.

## Method:

traverse to build the graph, then do bfs:

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def distanceK(self, root, target, K):
            """
            :type root: TreeNode
            :type target: TreeNode
            :type K: int
            :rtype: List[int]
            """
            d=collections.defaultdict(list)
            
            def traversal(root):
                if root:
                    if root.left:
                        d[root.val].append(root.left.val)
                        d[root.left.val].append(root.val)
                        traversal(root.left)
                    if root.right:
                        d[root.val].append(root.right.val)
                        d[root.right.val].append(root.val)
                        traversal(root.right)
                        
            traversal(root)
            res=[]
            s=set()
            queue=collections.deque([[target.val, 0]])
            while queue:
                for _ in range(len(queue)):
                    val, dist=queue.popleft()
                    if val not in s:
                        s.add(val)
                        if dist==K:
                            res.append(val)
                        if dist>K:
                            return res
                        for node in d[val]:
                            queue.append([node, dist+1])
            return res