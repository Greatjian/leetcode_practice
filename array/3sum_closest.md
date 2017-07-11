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
         distance=2^32-1
         while i<len(nums)-2:
             j=i+1
             k=len(nums)-1
             total=nums[i]+nums[j]+nums[k]
             res=nums[0]+nums[1]+nums[-1]
             value=min(abs(total-target), abs(distance-target))
             while j<k:
                 if total==target:
                     return total
                 elif total<target:
                     j+=1
                     if abs(total-target)<value:
                         res=total
                 else:
                     k-=1
                     if abs(total-target)<value:
                         res=total
             i+=1
             return res
 ```
  pending for error...
  
  ## Solution:
  要返回最接近的和，需不断用更新过的和与之比较并作替代判断。
  代码中ans的初始值设定与替代判断值得学习。
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