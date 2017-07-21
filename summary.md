# Summery

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
二分法搜索的使用，注意特殊情况。
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
- 