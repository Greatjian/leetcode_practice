# Summery

## catalog:
- [Array](#array)
- [Backtracking](#backtracking)

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

## Backtracking

- [039: Combination Sum](/array/Combination_Sum.md) 
采用回溯法遍历，dfs(深度优先搜索)，正推与倒推方式。
- [040: Combination Sum II](/array/Combination_Sum_II.md)
采用回溯法遍历，dfs(深度优先搜索)，正推与倒推方式，删除重复元素。
- [046: Permutations](/backtracking/Permutations.md)
nums减少，path增加，nums为空时添加入res
- [047: Permutations II](/backtracking/Permutations_II.md)
类似前题，出现重复元素需加入条件判断删除重复结果。
- [078: Subsets](/array/Subsets.md)
递归(recursion)与迭代(iteration)方法的使用。
- [079: Word Search](/array/Word_Search.md)
递归的使用，操作时最好不改变矩阵数值，可对每个元素增加对应判断值T/F。
- [090: Subsets II](/array/Subsets_II.md)
若新添加元素与之前不同，则新元素分别于结果中所有元素结合添加；否则与上一添加结果后元素结合添加。
