# Summery

## Catalog:
- [Array](#array)
- [Backtracking](#backtracking)
- [Dynamic Programming](#dynamic-programming)
- [Tree](#tree)
- [String](#string)
- [Hash Table](#hash-table)
- [Math](#math)

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
dfs；math；dp递推。
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
- [264: Ugly Number II](/DynamicProgramming/Ugly_Number_II.md)
找规律，ugly number后面出现的数为列表前出现数字的2，3，5倍。
- [279: Perfect Squares](/DynamicProgramming/Perfect_Squares.md)
不断减去平方差减小替代循环，直至0。
- [300: Longest Increasing Subsequence](/DynamicProgramming/Longest_Increasing_Subsequence.md)
dp；二分法。
- [303: Range Sum Query - Immutable](/DynamicProgramming/Range_Sum_Query_Immutable.md)
遍历求和计算部分在init内完成，可减少每次调用函数所需时间。
- [304: Range Sum Query 2D - Immutable](/DynamicProgramming/Range_Sum_Query_2D_Immutable.md)
二位矩阵元素求和。
- [322: Coin Change](/DynamicProgramming/Coin_Change.md)
状态转移方程：dp[x + c] = min(dp[x] + 1, dp[x + c])。
- [338: Counting Bits](/DynamicProgramming/Counting_Bits.md)
找规律；移位。
- [343: Integer Break](/DynamicProgramming/Integer_Break.md)
找规律；dp状态转移方程：dp[i]=max(3 * dp[i-3], 2 * dp[i-2])。
- [368: Largest Divisible Subset](/DynamicProgramming/Largest_Divisible_Subset.md)
dp状态转移方程：dp[i]=max(dp[i],dp[j]+1)。
- [375: Guess Number Higher or Lower II](/DynamicProgramming/Guess_Number_Higher_or_Lower_II.md)
minimax:最小化最大可能损失。
- [376: Wiggle Subsequence](/DynamicProgramming/Wiggle_Subsequence.md)
dp上升下降状态转换。
- [377: Combination Sum IV](/DynamicProgramming/Combination_Sum_IV.md)
dp，其中dp[x]表示生成数字x的所有可能的组合方式的个数。
- [392: Is Subsequence](/DynamicProgramming/Is_Subsequence.md)
遍历检索count；剔除判断空集。
- [413: Arithmetic Slices](/DynamicProgramming/Arithmetic_Slices.md)
每判断三数记录curr，再判断与之前是否相同增加至sum。
- [416: Partition Equal Subset Sum](/DynamicProgramming/Partition_Equal_Subset_Sum.md)
dp记录遍历数组时记录所有可能值，为防止前对后影响，赋值时可采用倒序。
- [464: Can I Win](/DynamicProgramming/Can_I_Win.md)
位运算+记忆化搜索。
- [467: Unique Substrings in Wraparound String](/DynamicProgramming/Unique_Substrings_in_Wraparound_String.md)
dp[i]记录字母i开头数组满足条件子集数，max去除重复部分。
- [474: Ones and Zeroes](/DynamicProgramming/Ones_and_Zeroes.md)
二维01背包问题（Knapsack Problem)。
- [494: Target Sum](/DynamicProgramming/Target_Sum.md)
dp counter记录每一次求和出现次数。
- [516: Longest Palindromic Subsequence](/DynamicProgramming/Longest_Palindromic_Subsequence.md)
dp 根据index设置状态转移方程。
- [523: Continuous Subarray Sum](/DynamicProgramming/Continuous_Subarray_Sum.md)
subarray sum可转化为任意两Index总和之差，利用字典key记录模值。
- [576: Out of Boundary Paths](/DynamicProgramming/Out_of_Boundary_Paths.md)
dfs+记忆化搜索；dp记录改点次数，每次移动创建ndp不断覆盖。
- [638: Shopping Offers](/DynamicProgramming/Shopping_Offers.md)
Recursion + Memoization = Dynamic Programming；zip函数的使用。
- [646: Maximum Length of Pair Chain](/DynamicProgramming/Maximum_Length_of_Pair_Chain.md)
dp（第一个数排序），贪心算法（第二个数排序）。
- [647: Palindromic Substrings](DynamicProgramming/Palindromic_Substrings.md)
对称中心法。
- [650: 2 Keys Keyboard](/DynamicProgramming/2_Keys_Keyboard.md)
dp；直接分解recursion/while loop。
- [673: Number of Longest Increasing Subsequence](/DynamicProgramming/Number_of_Longest_Increasing_Subsequence.md)
建立两个dp list，分别记录数值和数量。

## Tree
- [094: Binary Tree Inorder Traversal](/tree/Binary_Tree_Inorder_Traversal.md)
recursive and iterative method。
- [095: Unique Binary Search Trees II](/tree/Unique_Binary_Search_Trees_II.md)
- [096: Unique Binary Search Trees](/tree/Unique_Binary_Search_Trees.md)
root.left.val < root.val < root.right.val。
- [098: Validate Binary Search Tree](/tree/Validate_Binary_Search_Tree.md)
iterative(similar to inorder traversal) and recursive method。
- [100: Same Tree](/tree/Same_Tree.md)
recursive and iterative method。
- [101: Symmetric Tree](/tree/Symmetric_Tree.md)
recursive and iterative method，与上题类似。
- [102: Binary Tree Level Order Traversal](/tree/Binary_Tree_Level_Order_Traversal.md)
recursive and iterative method(list, deque)。
- [103: Binary Tree Zigzag Level Order Traversal](/tree/Binary_Tree_Zigzag_Level_Order_Traversal.md)
与上题类似，recursive and iterative method(deque)。
- [104: Maximum Depth of Binary Tree](/tree/Maximum_Depth_of_Binary_Tree.md)
recursion and iteration(list)。
- [105: Construct Binary Tree from Preorder and Inorder Traversal](/tree/Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.md)
recursion(slicing, index, dict)。
- [106: Construct Binary Tree from Inorder and Postorder Traversal](/tree/Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.md)
与上题类似。
- [107: Binary Tree Level Order Traversal II](/tree/Binary_Tree_Level_Order_Traversal.md)
102反向。
- [108: Convert Sorted Array to Binary Search Tree](/tree/Convert_Sorted_Array_to_Binary_Search_Tree.md)
recursion。
- [110: Balanced Binary Tree](/tree/Balanced_Binary_Tree.md)
top down and bottom up。
- [111: Minimum Depth of Binary Tree](/tree/Minimum_Depth_of_Binary_Tree.md)
recursion。
- [112: Path Sum](/tree/Path_Sum.md)
recursion and iteration。
- [113: Path Sum II](/tree/Path_Sum_II.md)
recursion。
- [114: Flatten Binary Tree to Linked List](/tree/Flatten_Binary_Tree_to_Linked_List.md)
recursion: 倒序遍历（右左中）插入。
- [116: Populating Next Right Pointers in Each Node](/tree/Populating_Next_Right_Pointers_in_Each_Node.md)
recursion and iteration。
- [117: Populating Next Right Pointers in Each Node II](/tree/Populating_Next_Right_Pointers_in_Each_Node_II.md)
仿照上题，iteration using more pointers。
- [129: Sum Root to Leaf Numbers](/tree/Sum_Root_to_Leaf_Numbers.md)
recursion and iteration (stack dfs + queue bfs)。
- [144: Binary Tree Preorder Traversal](/tree/Binary_Tree_Preorder_Traversal.md)
recursion and iteration (stack)。
- [145: Binary Tree Postorder Traversal](/tree/Binary_Tree_Postorder_Traversal.md)
recursion and iteration (preorder反向+倒序)。
- [173: Binary Search Tree Iterator](/tree/Binary_Search_Tree_Iterator.md)
inorder traversal using stack。
- [199: Binary Tree Right Side View](/tree/Binary_Tree_Right_Side_View.md)
bfs, iteration and recursion。
- [222: Count Complete Tree Nodes](/tree/Count_Complete_Tree_Nodes.md)
get height, iteration and recursion。
- [226: Invert Binary Tree](/tree/Invert_Binary_Tree.md)
recursion and iteration (dfs, bfs)。
- [230: Kth Smallest Element in a BST](/tree/Kth_Smallest_Element_in_a_BST.md)
inorder traversal。
- [235: Lowest Common Ancestor of a Binary Search Tree](/tree/Lowest_Common_Ancestor_of_a_Binary_Search_Tree.md)
BST。
- [236: Lowest Common Ancestor of a Binary Tree](/tree/Lowest_Common_Ancestor_of_a_Binary_Tree.md)
仿照上题，recursion。
- [257: Binary Tree Paths](/tree/Binary_Tree_Paths.md)
recursion, iteration (stack, queue)。
- [337: House Robber III](/tree/House_Robber_III.md)
resursion+dp。
- [404: Sum of Left Leaves](/tree/Sum_of_Left_Leaves.md)
recursion。
- [437: Path Sum III](/tree/Path_Sum_III.md)
recursion+ path/dict。
- [449: Serialize and Deserialize BST](/tree/Serialize_and_Deserialize_BST.md)
map和' '.join()的用法，string and int转换。
- [450: Delete Node in a BST](/tree/Delete_Node_in_a_BST.md)
recursion+分类讨论。
- [501: Find Mode in Binary Search Tree](/tree/Find_Mode_in_Binary_Search_Tree.md)
dict；inorder traversal。
- [508: Most Frequent Subtree Sum](/tree/Most_Frequent_Subtree_Sum.md)
defaultdict()+recursion。
- [513: Find Bottom Left Tree Value](/tree/Find_Bottom_Left_Tree_Value.md)
level order traversal; recursion。
- [515: Find Largest Value in Each Tree Row](/tree/Find_Largest_Value_in_Each_Tree_Row.md)
level order traversal; recursion。
- [538：Convert BST to Greater Tree](/tree/Convert_Sorted_Array_to_Binary_Search_Tree.md)
reversed inorder traversal。
- [543: Diameter of Binary Tree](/tree/Diameter_of_Binary_Tree.md)
recursion。
- [563: Binary Tree Tilt](/tree/Binary_Tree_Tilt.md)
recursion。
- [572: Subtree of Another Tree](/tree/Subtree_of_Another_Tree.md)
isSametree子集；string比较。
- [606: Construct String from Binary Tree](/tree/Construct_String_from_Binary_Tree.md)
recursion+分类讨论。
- [617: Merge Two Binary Trees](/tree/Merge_Two_Binary_Trees.md)
recursion+分类讨论。
- [623: Add One Row to Tree](/tree/Add_One_Row_to_Tree.md)
level order traversal。
- [637: Average of Levels in Binary Tree](/tree/Average_of_Levels_in_Binary_Tree.md)
level order traversal。
- [652: Find Duplicate Subtrees](/tree/Find_Duplicate_Subtrees.md)
defaultdict()+recursion。
- [653: Two Sum IV - Input is a BST](/tree/Two_Sum_IV_-_Input_is_a_BST.md)
dict+recursion; set+iteration。
- [654: Maximum Binary Tree](/tree/Maximum_Binary_Tree.md)
recursion; iteration。
- [655: Print Binary Tree](/tree/Print_Binary_Tree.md)
recursion。
- [662: Maximum Width of Binary Tree](/tree/Maximum_Width_of_Binary_Tree.md)
level order traversal。
- [669: Trim a Binary Search Tree](/tree/Trim_a_Binary_Search_Tree.md)
recursion。
- [671: Second Minimum Node In a Binary Tree](/tree/Second_Minimum_Node_In_a_Binary_Tree.md)
recursion。
- [687: Longest Univalue Path](/tree/Longest_Univalue_Path.md)
recursion。

## String

- [003: Longest Substring Without Repeating Characters](/string/Longest_Substring_Without_Repeating_Characters.md)
dict()+一次遍历。
- [005: Longest Palindromic Substring](/string/Longest_Palindromic_Substring.md)
记录start point, len()。
- [006: ZigZag Conversion](/string/ZigZag_Conversion.md)
''.join()。
- [008: String to Integer (atoi)](/string/String_to_Integer_(atoi).md)
corner case。
- [012: Integer to Roman](/string/Integer_to_Roman.md)
index-value。
- [013: Roman to Integer](/string/Roman_to_Integer.md)
考虑4，9位。
- [014: Longest Common Prefix](/string/Longest_Common_Prefix.md)
min(strs, key=len), zip(*strs)。
- [020: Valid Parentheses](/string/Valid_Parentheses.md)
- [028: Implement strStr()](/string/Implement_strStr().md)
- [038: Count and Say](/string/Count_and_Say.md)
- [043: Multiply Strings](/string/Multiply_Strings.md)
map(int, num1[::-1])。
- [049: Group Anagrams](/string/Group_Anagrams.md)
collections.defaultdict(list)。
- [058: Length of Last Word](/string/Length_of_Last_Word.md)
s.split()。
- [067: Add Binary](/string/Add_Binary.md)
补位+carry on。
- [071: Simplify Path](/string/Simplify_Path.md)
split and join。
- [125: Valid Palindrome](/string/Valid_Palindrome.md)
s.lower(); s.upper(); s.isalnum(); s.isalpha(); s.isnumeric()。
- [151: Reverse Words in a String](/string/Reverse_Words_in_a_String.md)
join, split。
- [165: Compare Version Numbers](/string/Compare_Version_Numbers.md)
补位。
- [227: Basic Calculator II](/string/Basic_Calculator_II.md)
num+sign。
- [344: Reverse String](/string/Reverse_String.md)
recursive, two pointers, pythonic。
- [345: Reverse Vowels of a String](/string/Reverse_Vowels_of_a_String.md)
two pointers。
- [383: Ransom Note](/string/Ransom_Note.md)
set+count。
- [385: Mini Parser](/string/Mini_Parser.md)
stack。
- [434: Number of Segments in a String](/string/Number_of_Segments_in_a_String.md)
s.split()。
- [443: String Compression](/string/String_Compression.md)
two pointers, while loop for string length modification。
- [459: Repeated Substring Pattern](/string/Repeated_Substring_Pattern.md)
double the string。
- [468: Validate IP Address](/string/Validate_IP_Address.md)
split(), any(), all()。
- [520: Detect Capital](/string/Detect_Capital.md)
isupper(), islower(), istitle()。
- [521: Longest Uncommon Subsequence I](/string/Longest_Uncommon_Subsequence_I.md)
math。
- [522: Longest Uncommon Subsequence II](/string/Longest_Uncommon_Subsequence_II.md)
subsequence定义, sort长度。
- [537: Complex Number Multiplication](/string/Complex_Number_Multiplication.md)
- [539: Minimum Time Difference](/string/Minimum_Time_Difference.md)
sort。
- [541: Reverse String II](/string/Reverse_String_II.md)
recursion; range。
- [551: Student Attendance Record I](/string/Student_Attendance_Record_I.md)
- [553: Optimal Division](/string/Optimal_Division.md)
math。
- [556: Next Greater Element III](/string/Next_Greater_Element_III.md)
找到两个index交换位置，后部分sort。
- [557: Reverse Words in a String III](/string/Reverse_Words_in_a_String.md)
str[::-1]。
- [583: Delete Operation for Two Strings](/string/Delete_Operation_for_Two_Strings.md)
dp。
- [609: Find Duplicate File in System](/string/Find_Duplicate_File_in_System.md)
defaultdict()+split()。
- [657: Judge Route Circle](/string/Judge_Route_Circle.md)
- [678: Valid Parenthesis String](/string/Valid_Parenthesis_String.md)
lo and hi for (, *, )。
- [680: Valid Palindrome II](/string/Valid_Palindrome_II.md)
find the deletion point and check。
- [686: Repeated String Match](/string/Repeated_Substring_Pattern.md)
test twice based on length。
- [696: Count Binary Substrings](/string/Count_Binary_Substrings.md)
s.replace()。
- [722: Remove Comments](/string/Remove_Comments.md)

## Hash Table

- [036: Valid Sudoku](hash/Valid_Sudoku.md)
check for memory using dict() or set()。
- [136: Single Number](/hash/Single_Number.md)
位运算；set()。
- [138: Copy List with Random Pointer](/hash/Copy_List_with_Random_Pointer.md)
dict()。
- [166: Fraction to Recurring Decimal](/hash/Fraction_to_Recurring_Decimal.md)
*10 %, dict for memorization。
- [187: Repeated DNA Sequences](/hash/Repeated_DNA_Sequences.md)
defaultdict()。
- [202: Happy Number](/hash/Happy_Number.md)
set()。
- [204: Count Primes](/hash/Count_Primes.md)
- [205: Isomorphic Strings](/hash/Isomorphic_Strings.md)
dict[val] = idx。
- [242: Valid Anagram](/hash/Valid_Anagram.md)
- [274: H-Index](/hash/H-Index.md)
bucket sort。
- [290: Word Pattern](/hash/Word_Pattern.md)
similar to 205。
- [299: Bulls and Cows](/hash/Bulls_and_Cows.md)
- [347: Top K Frequent Elements](/hash/Top_K_Frequent_Elements.md)
sort, heap。
- [349: Intersection of Two Arrays](/hash/Intersection_of_Two_Arrays.md)
set1() & set2()。
- [350: Intersection of Two Arrays II](/hash/Intersection_of_Two_Arrays_II.md)
dict1() & dict2()。
- [389: Find the Difference](/hash/Find_the_Difference.md)
dict1() - dict2()。
- [409: Longest Palindrome](/hash/Longest_Palindrome.md)
两两搭配。
- [438: Find All Anagrams in a String](/hash/Find_All_Anagrams_in_a_String.md)
前加后减。
- [447: Number of Boomerangs](/hash/Number_of_Boomerangs.md)
记录点与距离。
- [451: Sort Characters By Frequency](/hash/Sort_Characters_By_Frequency.md)
sort。
- [454: 4Sum II](/hash/4Sum_II.md)
两两配对。
- [463: Island Perimeter](/hash/Island_Perimeter.md)
check for adjacent area。
- [500: Keyboard Row](/hash/Keyboard_Row.md)
- [525: Contiguous Array](/hash/Contiguous_Array.md)
后加前减。
- [535: Encode and Decode TinyURL](/hash/Encode_and_Decode_TinyURL.md)
hash()。
- [554: Brick Wall](/hash/Brick_Wall.md)
- [575: Distribute Candies](/hash/Distribute_Candies.md)
- [599: Minimum Index Sum of Two Lists](/hash/Minimum_Index_Sum_of_Two_Lists.md)
d[val]=idx。
- [645: Set Mismatch](/hash/Set_Mismatch.md)
dict；sum(set)。
- [648: Replace Words](/hash/Replace_Words.md)
defaultdict(list) in terms of first character。
- [676: Implement Magic Dictionary](/hash/Implement_Magic_Dictionary.md)
defaultdict(list) in terms of word length。
- [690: Employee Importance](/hash/Employee_Importance.md)
dfs, recursion/iteration。
- [692: Top K Frequent Words](/hash/Top_K_Frequent_Words.md)
one more sorting than 347。
- [718: Maximum Length of Repeated Subarray](/hash/Maximum_Length_of_Repeated_Subarray.md)
dp。
- [720: Longest Word in Dictionary](/hash/Longest_Word_in_Dictionary.md)
sort(key)。
- [734: Sentence Similarity](/hash/Sentence_Similarity.md)
defaultdict(set)。

## Math

- [002: Add Two Numbers](/math/Add_Two_Numbers.md)
carryon。
- [007: Reverse Integer](/math/Reverse_Integer.md)
reverse。
- [009： Palindrome Number](/math/Palindrome_Number.md)
similar to last one, no need to check for overflow。
- [029: Divide Two Integers](/math/Divide_Two_Integers.md)
不断增加divisor。
- [050: Pow(x, n)](/math/Pow(x,n).md)
x*=x, n/=2。
- [069: Sqrt(x)](/math/Sqrt(x).md)
binary search; iterative。
- [168: Excel Sheet Column Title](/math/Excel_Sheet_Column_Title.md)
add iteratively。
- [171: Excel Sheet Column Number](/math/Excel_Sheet_Column_Number.md)
similar to the last question。
- [172: Factorial Trailing Zeroes](/math/Factorial_Trailing_Zeroes.md)
similar to the last question。
- [223: Rectangle Area](/math/Rectangle_Area.md)
分类讨论。
- [231: Power of Two](/math/Power_of_Two.md)
n/=2; bit manipulation。
- [258: Add Digits](/math/Add_Digits.md)
recursive/iterative/mod。
- [313: Super Ugly Number](/math/Super_Ugly_Number.md)
加入顺序。

