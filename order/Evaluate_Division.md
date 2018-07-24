# 399. Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:

    Given a / b = 2.0, b / c = 3.0. 
    queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
    return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

    equations = [ ["a", "b"], ["b", "c"] ],
    values = [2.0, 3.0],
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

## Method:

build the graph (store values in nodes), then do dfs for each query:

    class Solution(object):
        def calcEquation(self, equations, values, queries):
            """
            :type equations: List[List[str]]
            :type values: List[float]
            :type queries: List[List[str]]
            :rtype: List[float]
            """
            g=collections.defaultdict(list)
            for i in range(len(equations)):
                g[equations[i][0]].append([equations[i][1], values[i]])
                g[equations[i][1]].append([equations[i][0], 1.0/values[i]])
            res=[]
            for a, b in queries:
                flag=False
                stack=[[a, 1.0]]
                s=set()
                while stack:
                    node, val=stack.pop()
                    if node==b and node in g:
                        flag=True
                        res.append(val)
                        break
                    if node not in s:
                        s.add(node)
                        for n in g[node]:
                            stack.append([n[0], val*n[1]])
                if not flag:
                    res.append(-1.0)
            return res
            
recursive dfs:

    class Solution(object):
        def calcEquation(self, equations, values, queries):
            """
            :type equations: List[List[str]]
            :type values: List[float]
            :type queries: List[List[str]]
            :rtype: List[float]
            """
            g=collections.defaultdict(list)
            for i in range(len(equations)):
                g[equations[i][0]].append([equations[i][1], values[i]])
                g[equations[i][1]].append([equations[i][0], 1.0/values[i]])
                
            def dfs(start, end, visited, val):
                if start == end and start in g:
                    self.ans=val
                    return
                if start not in visited:
                    visited.add(start)
                    for n in g[start]:
                        dfs(n[0], end, visited, val*n[1])
                        
            res=[]
            for a, b in queries:
                self.ans=-1.0
                dfs(a, b, set(), 1.0)
                res.append(self.ans)
            return res
            
## Solution:

with multiply queries, union find is faster:

    class Node:
        def __init__(self):
            self.val = 1.0
            self.parent = self
    
    class Solution:
        def calcEquation(self, equations, values, queries):
            """
            :type equations: List[List[str]]
            :type values: List[float]
            :type queries: List[List[str]]
            :rtype: List[float]
            """
            def find(node):
                if node == node.parent:
                    return node
                return find(node.parent)
    
            def union(p, q, val):
                r1=find(p)
                r2=find(q)
                r2.parent=r1
                r2.val=p.val * val / q.val
    
            def evaluate(node):
                if node.parent==node:
                    return node.val;
                return node.val*evaluate(node.parent)
    
            d={}
            for i in range(len(equations)):
                x1, x2=equations[i][0], equations[i][1]
                if x1 not in d:
                    d[x1]=Node()
                if x2 not in d:
                    d[x2]=Node()
                union(d[x1], d[x2], values[i])
                
            res=[-1.0]*len(queries)
            for i in range(len(queries)):
                x1, x2=queries[i][0], queries[i][1]
                if x1 not in d or x2 not in d:
                    continue
                if find(d[x1])!=find(d[x2]):
                    continue
                res[i]=evaluate(d[x2]) / evaluate(d[x1])
            return res;