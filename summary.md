# Summery

## Catalog:
- [Array](#array)
- [Backtracking](#backtracking)
- [Dynamic Programming](#dynamic-programming)

## Array

- [001: two sum](/array/two_sum.md) 
using dictionary for less time complexity.
- [011: container with most water](/array/container_with_most_water.md) 
建立初始值，后寻找判据依次遍历。注意while与for loop在其中的使用条件。
- [015: 3sum](/array/3sum.md) 
三数和转化为两数和，双指针夹逼求解，代码实现时需要注意删除重复部分。
- [016: 3sum closest](/array/3sum_closest.md)
返回值的初始值设定与替代判断实现。
- [018: 4sum](/array/4sum.md)
dictionary 与 tuple 的使用。
- [026: Remove Duplicates from Sorted Array](/array/Remove_Duplicates_from_Sorted_Array.md)
双指针的标记：两前。
- [027: Remove Element](/array/Remove_Element.md)
双指针的标记：前后标记或两后。
- [031: Next Permutation](/array/Next_Permutation.md)
举例找规律形成代码思路，具体实施：数组倒序、break语句、特殊情况单独考虑。
- [033: Search in Rotated Sorted Array](/array/Search_in_Rotated_Sorted_Array.md)
二分法搜索的使用，注意特殊情况(nums=1 or 2)。
- [034: Search for a Range](array/Search_for_a_Range.md)
二分法搜索的使用，注意特殊情况...
- [035: Search Insert Position](array/Search_Insert_Position.md)
二分法搜索的使用，注意特殊情况...
- [039: Combination Sum](/array/Combination_Sum.md) 
采用回溯法遍历，dfs(深度优先搜索)，正推与倒推方式。
- [040: Combination Sum II](/array/Combination_Sum_II.md)
采用回溯法遍历，dfs(深度优先搜索)，正推与倒推方式，删除重复元素。
- [048: Rotate Image](/array/Rotate_Image.md)
一步实现需要深度复制新数组，若不复制数组需要两次数组内部元素替换，注意替换时选定一半元素即可。
- [053: Maximum Subarray](/array/Maximum_Subarray.md)
动态规划问题，寻找动中之静。
- [054: Spiral Matrix](/array/Spiral_Matrix.md)
注意遍历顺序：每次都为右下左上（if...elif)与该方向到头后为右下左上（if...if并设置direction值）。还要注意退出while循环的边界设定。
- [055: Jump Game](/array/Jump_Game.md) 
倒序遍历：for i in range(len(nums)-1,-1,-1)。
- [056: Merge Intervals](/array/Merge_Intervals.md) 
使用双指针，一个遍历，一个与之比较并添加到结果集合中。
- [059: Spiral Matrix II](/array/Spiral_Matrix_II.md)
二维数组的一步建立：list = [[0 for i in range(n)] for j in range(n)]，高级解法的使用（i,j,di,dj,%）。
- [062: Unique Paths](/array/Unique_Paths.md)
数学题，每条路是其上方与左侧可能性之和。
- [063: Unique Paths II](array/Unique_Paths_II.md)
数学题同上，每条路是其上方与左侧可能性之和，但需要减去障碍位置（需考虑多种特殊情况）。
- [064: Minimum Path Sum](/array/Minimum_Path_Sum.md)
复制一维新数组操作，每一元素新数值为该处元素值加上上方和左侧数值的最小值。
- [066: Plus One](/array/Plus_One.md)
遍历通过使用for loop或者递归，分别判断每一位是否为9以及9是否在最高位。
- [073: Set Matrix Zeroes](/array/Set_Matrix_Zeroes.md)
对第一行和第一列是否有0进行判断，然后对其余（m-1）行与（n-1）列是否有0判断
并表示在对应第一行与第一列位置，再讲第一行第一列中含0项进行整行整列标记，最后标记
第一行与第一列本身.
- [074: Search a 2D Matrix](/array/Search_a_2D_Matrix.md)
双指针二分法，一列数中第x个对应m*n矩阵中的位置可以表示为matrix[x//n][x%n]
- [075: Sort Colors](/array/Sort_Colors.md)
使用三指针，前后标记0，2位置，中间依次遍历，分别判断并与前后交换位置。
- [078: Subsets](/array/Subsets.md)
递归(recursion)与迭代(iteration)方法的使用。
- [079: Word Search](/array/Word_Search.md)
递归的使用，操作时最好不改变矩阵数值，可对每个元素增加对应判断值T/F。
- [080: Remove Duplicates from Sorted Array II](/array/Remove_Duplicates_from_Sorted_Array2.md)
不改变数组长度，增设一指针将第三个以上的相同元素赋值为下一不同元素值
- [081: Search in Rotated Sorted Array II](/array/Search_in_Rotated_Sorted_Array_II.md)
同033：二分法搜索的使用，注意特殊情况(nums=1 or 2)。
- [088: Merge Sorted Array](/array/Merge_Sorted_Array.md)
倒序比较两数组值大小并赋值，这样可以避免数组前端元素被覆盖。
- [090: Subsets II](/array/Subsets_II.md)
若新添加元素与之前不同，则新元素分别于结果中所有元素结合添加；否则与上一添加结果后元素结合添加。
- [118: Pascal's Triangle](/array/Pascal's_Triangle.md)
找规律，从第三行开始遍历。
- [119: Pascal's Triangle II](/array/Pascal's_Triangle_II.md)
直接初始化数组，为防止数值被覆盖，可倒序遍历。
- [120: Triangle](/array/Triangle.md)
倒层倒序遍历更为简洁。
- [121: Best Time to Buy and Sell Stock](/array/Best_Time_to_Buy_and_Sell_Stock.md)
一次遍历求出后元素减前元素的最大值。
- [122: Best Time to Buy and Sell Stock II](/array/Best_Time_to_Buy_and_Sell_Stock_II.md)
一次遍历，总收益分解为若干大减小值的和。
- [152: Maximum Product Subarray](/array/Maximum_Product_Subarray.md)
最大值最小值分别为前任最大最小与新数相乘以及新数本身比较的最大最小。比较时要注意maxp中段会改变数值，故需要提前赋值给新变量。
- [153: Find Minimum in Rotated Sorted Array](/array/Find_Minimum_in_Rotated_Sorted_Array.md)
二分法，注意条件与1，2number时的对应。
- [162: Find Peak Element](/array/Find_Peak_Element.md)
二分法，根据元素数目分别讨论。
- [167: Two Sum II - Input array is sorted](/array/Two_Sum_II_Input_array_is_sorted.md)
字典或双指针遍历。
- [169: Majority Element](/array/Majority_Element.md)
返回中间值。
- [189: Rotate Array](/array/Rotate_Array.md)
翻转数组的三种方式。
- [209: Minimum Size Subarray Sum](/array/Minimum_Size_Subarray_Sum.md)
双指针操作：右侧指针右移，和超过s后左指针左移，和小于s后右指针右移，以此类推直到遍历完全部数组。
- [216: Combination Sum III](/array/Combination_Sum_III.md)
模仿前两题。每次回溯s减去元素值，k减一，两者同时为0将path加入结果。
- [217: Contains Duplicate](/array/Contains_Duplicate.md)
排序前后直接比较，set比较长度，dict判断key是否存在。
- [219: Contains Duplicate II](/array/Contains_Duplicate_II.md)
用dict判断key是否存在，用value排序后比较index差值。
- [228: Summary Ranges](/array/Summary_Ranges.md)
双指针；end移至后端点；通过判断前后端点是否一致分别加入res。
- [229: Majority Element II](/array/Majority_Element.md)
使用dict，用value作为count；最多返回两个值，分别记录数值与出现次数。
- [238: Product of Array Except Self](/array/Product_of_Array_Except_Self.md)
设置新数组，正反各遍历数组一遍。
- [268: Missing Number](/array/Missing_Number.md)
求和公式。
- [283: Move Zeroes](/array/Move_Zeroes.md)
零与非零交换位置；非零覆盖零位，赋值剩余位置为零。
- [287: Find the Duplicate Number](/array/Find_the_Duplicate_Number.md)
二分法；映射找环法。
- [289: Game of Life](/array/Game_of_Life.md)
0，1外通过增加2，3表示后轮状态，移位可实现原状态到新状态的转变。
- [380: Insert Delete GetRandom O(1)](/array/Insert_Delete_GetRandom_O(1).md)
在map中将key的value值记为index，列表中使用pop剔除元素达到O(1)。
- [414: Third Maximum Number](/array/Third_Maximum_Number.md)
一次遍历通过三个指针不断代替求得；用set去除重复元素，然后剔除两个最大值。
- [442: Find All Duplicates in an Array](/array/Find_All_Duplicates_in_an_Array.md)
将元素值视作下标取负，使用绝对值判断；位置交换法。
- [448: Find All Numbers Disappeared in an Array](/array/Find_All_Numbers_Disappeared_in_an_Array.md)
同上题，负数标记法。
- [485: Max Consecutive Ones](/array/Max_Consecutive_Ones.md)
简单动态规划，计数器。
- [495: Teemo Attacking](/array/Teemo_Attacking.md)
分类讨论：下一次攻击时前次攻击是否停止。
- [532: K-diff Pairs in an Array](/array/K-diff_Pairs_in_an_Array.md)
使用set和dict处理重复元素。
- [560: Subarray Sum Equals K](/array/Subarray_Sum_Equals_K.md)
使用dict计数，sum(j)-sum(i)=k。
- [561: Array Partition I](/array/Array_Partition_I.md)
排序求偶数位元素和。
- [565: Array Nesting](/array/Array_Nesting.md)
判断遍历：赋值-1或创建新数组。
- [566: Reshape the Matrix](/array/Reshape_the_Matrix.md)
一次遍历，不需额外占用空间（、与%的妙用。
- [581: Shortest Unsorted Continuous Subarray](/array/Shortest_Unsorted_Continuous_Subarray.md)
通过新建立排序数组与原数组比较，记满足nums[i] != snums[i]的最小i值为s，最大i值为e。
- [605: Can Place Flowers](/array/Can_Place_Flowers.md)
贪心算法（局部最优可导致整体最优）。
- [611: Valid Triangle Number](/array/Valid_Triangle_Number.md)
双指针移动的两小边,O(n^2)。
- [621: Task Scheduler](/array/Task_Scheduler.md)
贪心法，直接从最多任务元素开始排列。
- [628: Maximum Product of Three Numbers](/array/Maximum_Product_of_Three_Numbers.md)
最大三数和为数组最大三数乘积或最大数乘两最小数值。float('inf')，float('-inf')/None。

## Backtracking

- [017: Letter Combinations of a Phone Number](/backtracking/Letter_Combinations_of_a_Phone_Number.md)
dfs，注意遍历时return位置以及元素变化时的添加位置（for loop or dfs）。
- [022: Generate Parentheses](/backtracking/Generate_Parentheses.md)
添加左右变量判断。
- [039: Combination Sum](/array/Combination_Sum.md) 
采用回溯法遍历，dfs(深度优先搜索)，正推与倒推方式。
- [040: Combination Sum II](/array/Combination_Sum_II.md)
采用回溯法遍历，dfs(深度优先搜索)，正推与倒推方式，删除重复元素。
- [046: Permutations](/backtracking/Permutations.md)
nums减少，path增加，nums为空时添加入res
- [047: Permutations II](/backtracking/Permutations_II.md)
类似前题，出现重复元素需加入条件判断删除重复结果。
- [060: Permutation Sequence](/backtracking/Permutation_Sequence.md)
使用n-1阶乘迭代。
- [077: Combinations](/backtracking/Combinations.md)
dfs增加判断去除不必要的递归；主函数自我递归。
- [078: Subsets](/array/Subsets.md)
递归(recursion)与迭代(iteration)方法的使用。
- [079: Word Search](/array/Word_Search.md)
递归的使用，操作时最好不改变矩阵数值，可对每个元素增加对应判断值T/F。
- [089: Gray Code](/backtracking/Gray_Code.md)
位操作；找规律。
- [090: Subsets II](/array/Subsets_II.md)
若新添加元素与之前不同，则新元素分别于结果中所有元素结合添加；否则与上一添加结果后元素结合添加。
- [093: Restore IP Addresses](/backtracking/Restore_IP_Addresses.md)
四段数字，每段1-3位，大小在0-255间，若非0则首位不能有0。
- [131: Palindrome Partitioning](/backtracking/Palindrome_Partitioning.md)
判断回文数：s[0:i+1]==s[i::-1]。
- [216: Combination Sum III](/array/Combination_Sum_III.md)
模仿前两题。每次回溯s减去元素值，k减一，两者同时为0将path加入结果。
- [357: Count Numbers with Unique Digits](/backtracking/Count_Numbers_with_Unique_Digits.md)
dfs；math。
- [401: Binary Watch](/backtracking/Binary_Watch.md)
位操作。
- [526: Beautiful Arrangement](/backtracking/Beautiful_Arrangement.md)
dfs；dict。

## Dynamic Programming
- [053: Maximum Subarray](/array/Maximum_Subarray.md)
动态规划问题，寻找动中之静。
- [062: Unique Paths](/array/Unique_Paths.md)
数学题，每条路是其上方与左侧可能性之和。
- [063: Unique Paths II](array/Unique_Paths_II.md)
数学题同上，每条路是其上方与左侧可能性之和，但需要减去障碍位置（需考虑多种特殊情况）。
- [064: Minimum Path Sum](/array/Minimum_Path_Sum.md)
复制一维新数组操作，每一元素新数值为该处元素值加上上方和左侧数值的最小值。
- [070: Climbing Stairs](/DynamicProgramming/Climbing_Stairs.md)
递推法。
- [091: Decode Ways](/DynamicProgramming/Decode_Ways.md)
递推，判断0位。
- [139: Word Break](/DynamicProgramming/Word_Break.md)
dp list传递。
- [198: House Robber](DynamicProgramming/House_Robber.md)
dp, 寻找递推公式。
- [213: House Robber II](/DynamicProgramming/House_Robber_II.md)
将环形DP问题转化为两趟线性DP问题。
- [221: Maximal Square](/DynamicProgramming/Maximal_Square.md)
dp，状态转移方程；create list using comprehension: dp=[[0]*n for i in range(m)]