# 449. Serialize and Deserialize BST

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

## Method:

preorder storage:

map和' '.join()的用法

['3','2','1','4','5']->

'3 2 1 4 5'->

[3,2,1,4,5]

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Codec:
    
        def serialize(self, root):
            """Encodes a tree to a single string.
            
            :type root: TreeNode
            :rtype: str
            """
            
            def helper(root, res):
                if not root:
                    return
                res.append(str(root.val))
                helper(root.left, res)
                helper(root.right, res)
                
            res=[]
            helper(root, res)
            return ' '.join(res)
      
        def deserialize(self, data):
            """Decodes your encoded data to tree.
            
            :type data: str
            :rtype: TreeNode
            """
            
            def helper(q):
                if not q:
                    return
                node = TreeNode(q.popleft())
                smallq=collections.deque()
                while q and q[0]<node.val:
                    smallq.append(q.popleft())
                node.left=helper(smallq)
                node.right=helper(q)
                return node
        
            q=collections.deque(map(int, data.split()))
            return helper(q)
    
    
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))