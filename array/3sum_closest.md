# 016. 3Sum Closest

Given an array S of n integers, 
find three integers in S such that the sum is closest to a given number, 
target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

## Method:

first thought: similar to 3sum, sort and traverse using two pointers. 
make the sum and compute the closest value.

卡在没有设定初始值，导致未找到合适条件判据。
```
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i=0
        while i<len(nums)-2:
            j=i+1
            k=len(nums-1)
            total=nums[i]+nums[j]+nums[k]
            value=abs(total-target)
            while j<k:
                if 
            i+=1
            return value
 ```
新一次尝试用利用差值distance最小替换，pending for error... 
 
 ```
 class Solution(object):
     def threeSumClosest(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         nums.sort()
         i=0
         distance=2^32-1
         res=0
         while i<len(nums)-2:
             j=i+1
             k=len(nums)-1
             while j<k:
                total=nums[i]+nums[j]+nums[k]
                 if total==target:
                     return total
                 if abs(total-target)<distance:
                     res=total
                     distance=abs(total-target)
                 elif total<target:
                     j+=1
                 else:
                     k-=1
             i+=1
             return res
  
fail for case ([1,1,1,1],100) should return 3 instead of 0
 ```
 good try:
 
 ```
 class Solution(object):
     def threeSumClosest(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         nums.sort()
         i=0
         distance=2^32-1
         res='none'
         while i<len(nums)-2:
             j=i+1
             k=len(nums)-1
             while j<k:
                 total=nums[i]+nums[j]+nums[k]
                 if total==target:
                     return total
                 if abs(total-target)<distance or res=='none':
                     res=total
                     distance=abs(total-target)
                 if total<target:
                     j+=1
                 else:
                     k-=1
             i+=1
         return res

 ```
  
  
  ## Solution:
  要返回最接近的和，需不断用更新过的和与之比较并作替代判断。
  代码中ans的初始值设定与替代判断值得学习。
  
  返回值为sum，但sum由变量相加得到，需用ans不断替代。
  
  重复情形不影响，故i直接遍历即可。
  ```
  class Solution:
      """
      @param numbers: Give an array numbers of n integer
      @param target : An integer
      @return : return the sum of the three integers, the sum closest target.
      """
      def threeSumClosest(self, numbers, target):
          numbers.sort()
          ans = None
          for i in range(len(numbers)):
              l, r = i + 1, len(numbers) - 1
              while (l < r):                    
                  sum = numbers[l] + numbers[r] + numbers[i]
                  if ans is None or abs(sum- target) < abs(ans - target):
                      ans = sum
                  if sum <= target:
                      l = l + 1
                  else:
                      r = r - 1
          return ans
  ```