# 103. Binary Tree Zigzag Level Order Traversal


Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:

Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

return its zigzag level order traversal as:
    
    [
      [3],
      [20,9],
      [15,7]
    ]
    
## Method:

对照前题用recursion，level奇偶不同输出顺序，但改变的是局部顺序而不是整体顺序，失败：

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def zigzagLevelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            self.l=[]
            self.helper(root, 0)
            return self.l
    
        def helper(self, root, level):
            if not root:
                return
            if level==len(self.l):
                self.l.append([])
            self.l[level].append(root.val)
            if level%2:
                self.helper(root.left, level+1)
                self.helper(root.right, level+1)
            else:
                self.helper(root.right, level+1)
                self.helper(root.left, level+1)
                
后改变主意，直接从输出地方改，正确：

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def zigzagLevelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            self.l=[]
            self.helper(root, 0)
            for i in range(len(self.l)):
                if i%2:
                    self.l[i]=self.l[i][::-1]
            return self.l
    
        def helper(self, root, level):
            if not root:
                return
            if level==len(self.l):
                self.l.append([])
            self.l[level].append(root.val)
            self.helper(root.left, level+1)
            self.helper(root.right, level+1)
            
iteration:

每层加入flag调整顺序：

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def zigzagLevelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            res = []
            flag = 1
            level = collections.deque([root])
            while root and level:
                local = []
                for _ in range(len(level)):
                    t = level.popleft()
                    local.append(t.val)
                    if t.left:
                        level.append(t.left)
                    if t.right:
                        level.append(t.right)
                res.append(local[::flag])
                flag*=-1
            return res