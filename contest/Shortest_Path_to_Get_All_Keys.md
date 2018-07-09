# 865. Shortest Path to Get All Keys

We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

 

Example 1:

    Input: ["@.a.#","###.#","b.A.B"]
    Output: 8

Example 2:

    Input: ["@..aA","..B#.","....b"]
    Output: 6
 

Note:

- 1 <= grid.length <= 30
- 1 <= grid[0].length <= 30
- grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
- The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.

## Method:

1. each step adds to one, so dijkstra is the same as bfs here
2. for each visiting node, keep track of useful information as `state`
(i for s-index, j for y-index, Set<String> for keys here)
3. Set<String> for keys can also represented by bits: `1 << (key - 'a')`

code:

    class Solution(object):
        def shortestPathAllKeys(self, grid):
            """
            :type grid: List[str]
            :rtype: int
            """
            m, n=len(grid), len(grid[0])
            cnt=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]=='@':
                        sx, sy=i, j
                    if grid[i][j] in 'abcdef':
                        cnt+=1
                        
            def neighbor(i, j):
                res=[]
                for di, dj in [[-1,0],[1,0],[0,1],[0,-1]]:
                    if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj]!='#':
                        res.append((i+di, j+dj))
                return res
                        
            queue=collections.deque([[sx,sy,set(),0]])
            s=set()
            while queue:
                i, j, keys, move=queue.popleft()
                if len(keys)==cnt:
                    return move
                if (i, j, tuple(keys)) not in s:
                    s.add((i, j, tuple(keys)))
                    for ni, nj in neighbor(i ,j):
                        if grid[ni][nj] in 'abcdef':
                            queue.append([ni,nj,keys|set([grid[ni][nj]]),move+1])
                        elif grid[ni][nj] in 'ABCDEF' and grid[ni][nj].lower() in keys:
                            queue.append([ni,nj,keys,move+1])
                        elif grid[ni][nj] in '.@':
                            queue.append([ni,nj,keys,move+1])
            return -1