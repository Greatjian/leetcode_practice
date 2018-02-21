# 297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree


        1
       / \
      2   3
         / \
        4   5

as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

## Method:

preorder + queue:

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
            
            def helper(root):
                if not root:
                    res.append('a,')
                    return
                res.append(str(root.val)+',')
                helper(root.left)
                helper(root.right)
              
            res=[]
            helper(root)
            return ''.join(res)
    
        def deserialize(self, data):
            """Decodes your encoded data to tree.
            
            :type data: str
            :rtype: TreeNode
            """
            def helper(queue):
                if not queue:
                    return
                string=queue.popleft()
                if string=='a':
                    return None
                root=TreeNode(int(string))
                root.left=helper(queue)
                root.right=helper(queue)
                return root
                
            queue=collections.deque(data.split(','))
            return helper(queue)
                
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))