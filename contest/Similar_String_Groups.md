# 839. Similar String Groups

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of unique strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

Example 1:

    Input: ["tars","rats","arts","star"]
    Output: 2

Note:

- A.length <= 2000
- A[i].length <= 1000
- A.length * A[i].length <= 20000
- All words in A consist of lowercase letters only.
- All words in A have the same length and are anagrams of each other.
- The judging time limit has been increased for this question.

## Method:

- build graph: compare every two (O(WN^2)) or construct and check (O(NW^3)),
where N is the length of input, W is the length of every words.

- find number of components: bfs_all/dfs_all (O(E)) or union find (O(N)).

- In python, judging time is limited, so the answer has to reach O(NW*min(N, W^2)), otherwise you'll get TLE.

dfs:

    class Solution(object):
        def numSimilarGroups(self, A):
            """
            :type A: List[str]
            :rtype: int
            """
            g=collections.defaultdict(list)
            if len(A)<len(A[0])**2:
                for i in range(len(A)):
                    for j in range(i+1, len(A)):
                        if sum(A[i][k]!=A[j][k] for k in range(len(A[i])))==2:
                            g[A[i]].append(A[j])
                            g[A[j]].append(A[i])
            else:
                setA=set(A)
                for a in A:
                    for i in range(len(a)):
                        for j in range(i+1, len(a)):
                            nei=a[:i]+a[j]+a[i+1:j]+a[i]+a[j+1:]
                            if nei in setA:
                                g[a].append(nei)
                                g[nei].append(a)
            
            # iterative
                    
            cnt=0
            s=set()
            for a in A:
                if a not in s:
                    cnt+=1
                    s.add(a)
                    stack=[a]
                    while stack:
                        node=stack.pop()
                        for n in g[node]:
                            if n not in s:
                                s.add(n)
                                stack.append(n)
            return cnt
            
            # recursive
            
            def dfs(node):
                s.add(node)
                for n in g[node]:
                    if n not in s:
                        dfs(n)
                        
            s=set()
            cnt=0
            for a in A:
                if a not in s:
                    dfs(a)
                    cnt+=1
            return cnt
                            
union find:

    class Solution(object):
        def numSimilarGroups(self, A):
            """
            :type A: List[str]
            :rtype: int
            """
            uf=UnionFind(len(A))
            if len(A)<len(A[0])**2:
                for i in range(len(A)):
                    for j in range(i+1, len(A)):
                        if sum(A[i][k]!=A[j][k] for k in range(len(A[i])))==2:
                            uf.union(i, j)
            else:
                d={v:i for i, v in enumerate(A)}
                for a in A:
                    for i in range(len(a)):
                        for j in range(i+1, len(a)):
                            nei=a[:i]+a[j]+a[i+1:j]+a[i]+a[j+1:]
                            if nei in d:
                                uf.union(d[a], d[nei])
            return sum(uf._id[i]==i for i in range(len(A)))
                        
            
    class UnionFind:
        def __init__(self, n):
            self._id = list(range(n))
            self._sz = [1] * n
    
        def _root(self, i):
            j = i
            while (j != self._id[j]):
                self._id[j] = self._id[self._id[j]]
                j = self._id[j]
            return j
    
        def find(self, p, q):
            return self._root(p) == self._root(q)
    
        def union(self, p, q):
            i = self._root(p)
            j = self._root(q)
            if i!=j:
                if (self._sz[i] < self._sz[j]):
                    self._id[i] = j
                    self._sz[j] += self._sz[i]
                else:
                    self._id[j] = i
                    self._sz[i] += self._sz[j]	
                            