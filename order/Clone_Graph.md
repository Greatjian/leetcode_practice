# 133. Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

- First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
- Second node is labeled as 1. Connect node 1 to node 2.
- Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
- Visually, the graph looks like the following:


       1
      / \
     /   \
    0 --- 2
         / \
         \_/

## Method:

dict:{node: node.copy}

bfs:

    # Definition for a undirected graph node
    # class UndirectedGraphNode:
    #     def __init__(self, x):
    #         self.label = x
    #         self.neighbors = []
    
    class Solution:
        # @param node, a undirected graph node
        # @return a undirected graph node
        def cloneGraph(self, node):
            if not node:
                return
            deque=collections.deque([node])
            nodeCopy=UndirectedGraphNode(node.label)
            d={node:nodeCopy}
            while deque:
                node=deque.popleft()
                for neighbor in node.neighbors:
                    if neighbor not in d:
                        d[neighbor]=UndirectedGraphNode(neighbor.label)
                        d[node].neighbors.append(d[neighbor])
                        deque.append(neighbor)
                    else:
                        d[node].neighbors.append(d[neighbor])                
            return nodeCopy
            
dfs stack:

    # Definition for a undirected graph node
    # class UndirectedGraphNode:
    #     def __init__(self, x):
    #         self.label = x
    #         self.neighbors = []
    
    class Solution:
        # @param node, a undirected graph node
        # @return a undirected graph node
        def cloneGraph(self, node):
            if not node:
                return
            stack=[node]
            nodeCopy=UndirectedGraphNode(node.label)
            d={node:nodeCopy}
            while stack:
                node=stack.pop()
                for neighbor in node.neighbors:
                    if neighbor not in d:
                        d[neighbor]=UndirectedGraphNode(neighbor.label)
                        d[node].neighbors.append(d[neighbor])
                        stack.append(neighbor)
                    else:
                        d[node].neighbors.append(d[neighbor])                
            return nodeCopy
            
dfs recursion:

    # Definition for a undirected graph node
    # class UndirectedGraphNode:
    #     def __init__(self, x):
    #         self.label = x
    #         self.neighbors = []
    
    class Solution:
        # @param node, a undirected graph node
        # @return a undirected graph node
        def cloneGraph(self, node):
            if not node:
                return
            nodeCopy=UndirectedGraphNode(node.label)
            d={node: nodeCopy}
            self.helper(node, d)
            return nodeCopy
            
        def helper(self, node, d):
            if not node:
                return
            for neighbor in node.neighbors:
                if neighbor not in d:
                    d[neighbor]=UndirectedGraphNode(neighbor.label)
                    d[node].neighbors.append(d[neighbor])
                    self.helper(neighbor, d)
                else:
                    d[node].neighbors.append(d[neighbor])
            