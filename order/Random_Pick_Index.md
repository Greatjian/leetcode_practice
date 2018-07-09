# 398. Random Pick Index

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
- The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

    int[] nums = new int[] {1,2,3,3,3};
    Solution solution = new Solution(nums);

    // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
    solution.pick(3);
    
    // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
    solution.pick(1);
    
## Method:

O(n) initialize and pick, O(n) space, lucky to get accepted:

    class Solution(object):
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.d=collections.defaultdict(list)
            for i, v in enumerate(nums):
                self.d[v].append(i)
    
        def pick(self, target):
            """
            :type target: int
            :rtype: int
            """
            return random.choice(self.d[target])
    
    
    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.pick(target)

## Solution:

reservoir sampling, pick O(n) time, O(1) space:

    class Solution(object):
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.nums=nums
    
        def pick(self, target):
            """
            :type target: int
            :rtype: int
            """
            result = -1
            count = 0;
            for i in range(len(self.nums)):
                if self.nums[i]!=target:
                    continue
                if random.randint(0, count)==0:
                    result=i
                count+=1
            return result
    
    
    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.pick(target)