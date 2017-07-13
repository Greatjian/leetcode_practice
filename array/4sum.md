# 018. 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

    A solution set is:
    [
    [-1,  0, 0, 1],
    [-2, -1, 1, 2],
    [-2,  0, 0, 2]
    ]
    
## Method:

first thought: 四个数字固定两数循环，
其余两数双指针首位夹逼，时间复杂度O(n^3)

代码实现：

```
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for  i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                k=j+1
                l=len(nums)-1
                while k<l:
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        if nums[k+1]==nums[k]:
                            k+=1
                        if nums[l-1]==nums[l]:
                            l-=1
                    elif sum<target:
                        k+=1
                    else:
                        l-=1
                if nums[j+1]==nums[j]:
                    j+=1
                j+=1
            if nums[i+1]==nums[i]:
                    i+=1
            i+=1
        return res
        
Run Code Status: Memory Limit Exceeded
```
换一种思路，先将元素配对两两求和储存在dictionary中，
之后与target比较调用。
```
def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    sum = {}
    res = []
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] in sum:
                sum[nums[i] + nums[j]].append([i, j])
            else:
                sum[nums[i] + nums[j]] = [[i, j]]
    # [1, 0, -1, 0, -2, 2]
    # {-3: [[0, 1]], -2: [[0, 2], [0, 3]], -1: [[0, 4], [1, 2], [1, 3]]...}

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
           if target - nums[i] - nums[j] in sum:
                for element in sum[target - nums[i] - nums[j]]:
                    res.append([nums[i], nums[j], nums[element[0]], nums[element[1]]])
    print(res)
    return res
```
之上结果有重复部分，需要内部升序排列，然后用tuple消除。

```
def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    sum = {}
    res = set()
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] in sum:
                sum[nums[i] + nums[j]].append([i, j])
            else:
                sum[nums[i] + nums[j]] = [[i, j]]
    # [1, 0, -1, 0, -2, 2]
    # {-3: [[0, 1]], -2: [[0, 2], [0, 3]], -1: [[0, 4], [1, 2], [1, 3]]...}

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
           if target - nums[i] - nums[j] in sum:
                for element in sum[target - nums[i] - nums[j]]:
                    if element[0]>j:
                        res.add((nums[i], nums[j], nums[element[0]], nums[element[1]]))
    res= [list(l) for l in res]
    return res
```

## Solution
```
class Solution(object):
    '''
    题意：找到数列中所有和等于目标数的四元组，需去重
    多枚举一个数后，参照3Sum的做法，O(N^3)    
    '''
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res
```
