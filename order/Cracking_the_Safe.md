# 753. Cracking the Safe

There is a box protected by a password. The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.

You can keep inputting the password, the password will automatically be matched against the last n digits entered.

For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

Example 1:

    Input: n = 1, k = 2
    Output: "01"
    Note: "10" will be accepted too.

Example 2:

    Input: n = 2, k = 2
    Output: "00110"
    Note: "01100", "10011", "11001" will be accepted too.

Note:
- n will be in the range [1, 4].
- k will be in the range [1, 10].
- k^n will be at most 4096.

## Method:

dfs going through all occurrence:

    class Solution(object):
        def crackSafe(self, n, k):
            """
            :type n: int
            :type k: int
            :rtype: str
            """
            
            def dfs(res, visited):
                if len(visited)==pow(k, n):
                    return True
                prev=''.join(res[len(res)-n+1:])
                for i in range(k):
                    new=prev+str(i)
                    if new not in visited:
                        res.append(str(i))
                        visited.add(new)
                        if dfs(res, visited):
                            return True
                        res.pop()
                        visited.remove(new)
                return False
            
            res=['0']*n
            dfs(res, set([''.join(res)]))
            return ''.join(res)