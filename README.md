# LeetCode Practice

This is the repository to record and share my [LeetCode](https://leetcode.com/) practice. 
It's the first step for me to become a software engineer.

The practice is listed based on different topics. I start from easy to medium, finally trying to 
get rid of the hard problems. The problems in each topic are listed in numerical order.

I use python to solve each answer. As the popular saying goes:

> Life is short, you need python.

You can see my attempts for each problem in the `Method` section, as well as the final solution in `Solution` part.
Final solutions are mostly inspired from the discussion at LeetCode platform, with small
modifications based on my understanding and coding style. 

I believe self-implementation is as important as coming up with great ideas in terms of solving a problem. 
Therefore it's highly recommended to write your own version of solutions instead of simply copying the codes. 
Coding style is another essential part to focus on :)

My harvests for each practice are summarized [here](/summary.md).

## Catalog:

- [Array](#array)
- [Backtracking](#backtracking)
- [Dynamic Programming](#dynamic-programming)
- [Tree](#tree)
- [String](#string)
- [Hash Table](#hash-table)
- [Math](#math)
- [Divide and Conquer](#divide-and-conquer)
- [Design](#design)
- [Order](#order)
- [Leetcode Contest](#leetcode-contest)

## Array

```
set(zip(*board)), set(map(tuple, board))
```

- binary search:
```
lo, hi=0, len(nums)-1
while lo<hi:
    mid=(lo+hi)/2
    if condition...:
        lo=mid+1
    else:
        hi=mid
return lo
```
- contiguous subarray: preSum
- sum of same length: sliding window 

|Number|Name|Date|
|:---:|:---:|:---:|
|001|[two sum](/array/two_sum.md)|2017.07.10|
|011|[container with most water](/array/container_with_most_water.md)|2017.07.10|
|015|[3sum](/array/3sum.md)|2017.07.10|
|016|[3sum closest](/array/3sum_closest.md)|2017.07.10|
|018|[4sum](/array/4sum.md)|2017.07.11|
|026|[Remove Duplicates from Sorted Array](/array/Remove_Duplicates_from_Sorted_Array.md)|2017.07.12|
|027|[Remove Element](/array/Remove_Element.md)|2017.07.12|
|031|[Next Permutation](/array/Next_Permutation.md)|2017.07.17|
|033|[Search in Rotated Sorted Array](/array/Search_in_Rotated_Sorted_Array.md)|2017.07.17|
|034|[Search for a Range](array/Search_for_a_Range.md)|2017.07.18|
|035|[Search Insert Position](array/Search_Insert_Position.md)|2017.07.18|
|039|[Combination Sum](/array/Combination_Sum.md)|2017.07.19|
|040|[Combination Sum II](/array/Combination_Sum_II.md)|2017.07.19|
|041|[First Missing Positive](/array/First_Missing_Positive.md)|2018.3.27|
|042|[Trapping Rain Water](/array/Trapping_Rain_Water.md)|2018.3.27|
|048|[Rotate Image](/array/Rotate_Image.md)|2017.07.20|
|053|[Maximum Subarray](/array/Maximum_Subarray.md)|2017.07.20|
|054|[Spiral Matrix](/array/Spiral_Matrix.md)|2017.07.20|
|055|[Jump Game](/array/Jump_Game.md)|2017.07.20|
|056|[Merge Intervals](/array/Merge_Intervals.md)|2017.07.20|
|059|[Spiral Matrix II](/array/Spiral_Matrix_II.md)|2017.07.20|
|062|[Unique Paths](/array/Unique_Paths.md)|2017.07.20|
|063|[Unique Paths II](/array/Unique_Paths_II.md)|2017.07.20|
|064|[Minimum Path Sum](/array/Minimum_Path_Sum.md)|2017.07.21|
|066|[Plus One](/array/Plus_One.md)|2017.07.21|
|073|[Set Matrix Zeroes](/array/Set_Matrix_Zeroes.md)|2017.07.21|
|074|[Search a 2D Matrix](/array/Search_a_2D_Matrix.md)|2017.07.21|
|075|[Sort Colors](/array/Sort_Colors.md)|2017.07.21|
|078|[Subsets](/array/Subsets.md)|2017.07.21|
|079|[Word Search](/array/Word_Search.md)|2017.07.23|
|080|[Remove Duplicates from Sorted Array II](/array/Remove_Duplicates_from_Sorted_Array2.md)|2017.07.24|
|081|[Search in Rotated Sorted Array II](/array/Search_in_Rotated_Sorted_Array_II.md)|2017.07.24|
|088|[Merge Sorted Array](/array/Merge_Sorted_Array.md)|2017.07.24|
|090|[Subsets II](/array/Subsets_II.md)|2017.07.25|
|118|[Pascal's Triangle](/array/Pascal's_Triangle.md)|2017.07.26|
|119|[Pascal's Triangle II](/array/Pascal's_Triangle_II.md)|2017.07.26|
|120|[Triangle](/array/Triangle.md)|2017.07.26|
|121|[Best Time to Buy and Sell Stock](/array/Best_Time_to_Buy_and_Sell_Stock.md)|2017.07.26|
|122|[Best Time to Buy and Sell Stock II](/array/Best_Time_to_Buy_and_Sell_Stock_II.md)|2017.07.26|
|128|[Longest Consecutive Sequence](/array/Longest_Consecutive%20_Sequence.md)|2018.3.27|
|152|[Maximum Product Subarray](/array/Maximum_Product_Subarray.md)|2017.07.26|
|153|[Find Minimum in Rotated Sorted Array](/array/Find_Minimum_in_Rotated_Sorted_Array.md)|2017.07.26|
|162|[Find Peak Element](/array/Find_Peak_Element.md)|2017.07.27|
|167|[Two Sum II - Input array is sorted](/array/Two_Sum_II_Input_array_is_sorted.md)|2017.07.27|
|169|[Majority Element](/array/Majority_Element.md)|2017.07.27|
|189|[Rotate Array](/array/Rotate_Array.md)|2017.7.30|
|209|[Minimum Size Subarray Sum](/array/Minimum_Size_Subarray_Sum.md)|2017.7.31|
|216|[Combination Sum III](/array/Combination_Sum_III.md)|2017.8.1|
|217|[Contains Duplicate](/array/Contains_Duplicate.md)|2017.8.1|
|219|[Contains Duplicate II](/array/Contains_Duplicate_II.md)|2017.8.1|
|228|[Summary Ranges](/array/Summary_Ranges.md)|2017.8.1|
|229|[Majority Element II](/array/Majority_Element.md)|2017.8.2|
|238|[Product of Array Except Self](/array/Product_of_Array_Except_Self.md)|2017.8.2|
|268|[Missing Number](/array/Missing_Number.md)|2017.8.2|
|283|[Move Zeroes](/array/Move_Zeroes.md)|2017.8.2|
|287|[Find the Duplicate Number](/array/Find_the_Duplicate_Number.md)|2017.8.2|
|289|[Game of Life](/array/Game_of_Life.md)|2017.8.3|
|380|[Insert Delete GetRandom O(1)](/array/Insert_Delete_GetRandom_O(1).md)|2017.8.3|
|414|[Third Maximum Number](/array/Third_Maximum_Number.md)|2017.8.3|
|442|[Find All Duplicates in an Array](/array/Find_All_Duplicates_in_an_Array.md)|2017.8.3|
|448|[Find All Numbers Disappeared in an Array](/array/Find_All_Numbers_Disappeared_in_an_Array.md)|2017.8.4|
|485|[Max Consecutive Ones](/array/Max_Consecutive_Ones.md)|2017.8.4|
|495|[Teemo Attacking](/array/Teemo_Attacking.md)|2017.8.4|
|532|[K-diff Pairs in an Array](/array/K-diff_Pairs_in_an_Array.md)|2017.8.4|
|560|[Subarray Sum Equals K](/array/Subarray_Sum_Equals_K.md)|2017.8.4|
|561|[Array Partition I](/array/Array_Partition_I.md)|2017.8.4|
|565|[Array Nesting](/array/Array_Nesting.md)|2017.8.4|
|566|[Reshape the Matrix](/array/Reshape_the_Matrix.md)|2017.8.4|
|581|[Shortest Unsorted Continuous Subarray](/array/Shortest_Unsorted_Continuous_Subarray.md)|2017.8.4|
|605|[Can Place Flowers](/array/Can_Place_Flowers.md)|2017.8.4|
|611|[Valid Triangle Number](/array/Valid_Triangle_Number.md)|2017.8.5|
|621|[Task Scheduler](/array/Task_Scheduler.md)|2017.8.8|
|628|[Maximum Product of Three Numbers](/array/Maximum_Product_of_Three_Numbers.md)|2017.8.8|
|643|[Maximum Average Subarray I](/array/Maximum_Average_Subarray_I.md)|2017.8.8|
|644|[Maximum Average Subarray II](/array/Maximum_Average_Subarray_II.md)|2018.2.23|
|697|[Degree of an Array](/array/Degree_of_an_Array.md)|2018.1.15|
|717|[1-bit and 2-bit Characters](/array/1-bit_and_2-bit_Characters.md)|2017.12.13|
|724|[Find Pivot Index](/array/Find_Pivot_Index.md)|2018.4.10|

## Backtracking

|Number|Name|Date|
|:---:|:---:|:---:|
|017|[Letter Combinations of a Phone Number](/backtracking/Letter_Combinations_of_a_Phone_Number.md)|2017.8.9|
|022|[Generate Parentheses](/backtracking/Generate_Parentheses.md)|2017.8.9|
|037|[Sudoku Solver](/backtracking/Sudoku_Solver.md)|2018.5.15|
|051|[N-Queens](/backtracking/N-Queens.md)|2018.3.27|
|060|[Permutation Sequence](/backtracking/Permutation_Sequence.md)|2017.8.10|
|077|[Combinations](/backtracking/Combinations.md)|2017.8.10|
|089|[Gray Code](/backtracking/Gray_Code.md)|2017.8.10|
|093|[Restore IP Addresses](/backtracking/Restore_IP_Addresses.md)|2017.8.13|
|131|[Palindrome Partitioning](/backtracking/Palindrome_Partitioning.md)|2017.8.13|
|357|[Count Numbers with Unique Digits](/backtracking/Count_Numbers_with_Unique_Digits.md)|2017.8.14|
|401|[Binary Watch](/backtracking/Binary_Watch.md)|2017.8.15|
|526|[Beautiful Arrangement](/backtracking/Beautiful_Arrangement.md)|2017.8.16|

## Dynamic Programming

- zero
- base case

|Number|Name|Date|
|:---:|:---:|:---:|
|070|[Climbing Stairs](/DynamicProgramming/Climbing_Stairs.md)|2017.8.17|
|091|[Decode Ways](/DynamicProgramming/Decode_Ways.md)|2017.8.19|
|097|[Interleaving String](/DynamicProgramming/Interleaving_String.md)|2018.2.27|
|139|[Word Break](/DynamicProgramming/Word_Break.md)|2017.8.20|
|198|[House Robber](DynamicProgramming/House_Robber.md)|2017.8.21|
|213|[House Robber II](/DynamicProgramming/House_Robber_II.md)|2017.8.22|
|221|[Maximal Square](/DynamicProgramming/Maximal_Square.md)|2017.8.23|
|264|[Ugly Number II](/DynamicProgramming/Ugly_Number_II.md)|2017.8.26|
|279|[Perfect Squares](/DynamicProgramming/Perfect_Squares.md)|2017.8.26|
|300|[Longest Increasing Subsequence](/DynamicProgramming/Longest_Increasing_Subsequence.md)|2017.8.27|
|303|[Range Sum Query - Immutable](/DynamicProgramming/Range_Sum_Query_Immutable.md)|2017.8.28|
|304|[Range Sum Query 2D - Immutable](/DynamicProgramming/Range_Sum_Query_2D_Immutable.md)|2017.8.28|
|322|[Coin Change](/DynamicProgramming/Coin_Change.md)|2017.8.29|
|338|[Counting Bits](/DynamicProgramming/Counting_Bits.md)|2017.8.30|
|343|[Integer Break](/DynamicProgramming/Integer_Break.md)|2017.8.30|
|357|[Count Numbers with Unique Digits](/backtracking/Count_Numbers_with_Unique_Digits.md)|2017.8.14|
|368|[Largest Divisible Subset](/DynamicProgramming/Largest_Divisible_Subset.md)|2017.8.30|
|375|[Guess Number Higher or Lower II](/DynamicProgramming/Guess_Number_Higher_or_Lower_II.md)|2017.9.1|
|376|[Wiggle Subsequence](/DynamicProgramming/Wiggle_Subsequence.md)|2017.9.6|
|377|[Combination Sum IV](/DynamicProgramming/Combination_Sum_IV.md)|2017.9.6|
|392|[Is Subsequence](/DynamicProgramming/Is_Subsequence.md)|2017.9.6|
|413|[Arithmetic Slices](/DynamicProgramming/Arithmetic_Slices.md)|2017.9.12|
|416|[Partition Equal Subset Sum](/DynamicProgramming/Partition_Equal_Subset_Sum.md)|2017.9.13|
|464|[Can I Win](/DynamicProgramming/Can_I_Win.md)|2017.9.14|
|467|[Unique Substrings in Wraparound String](/DynamicProgramming/Unique_Substrings_in_Wraparound_String.md)|2017.9.15|
|474|[Ones and Zeroes](/DynamicProgramming/Ones_and_Zeroes.md)|2017.9.16|
|474|[Target Sum](/DynamicProgramming/Target_Sum.md)|2017.9.17|
|516|[Longest Palindromic Subsequence](/DynamicProgramming/Longest_Palindromic_Subsequence.md)|2017.9.18|
|523|[Continuous Subarray Sum](/DynamicProgramming/Continuous_Subarray_Sum.md)|2017.9.19|
|576|[Out of Boundary Paths](/DynamicProgramming/Out_of_Boundary_Paths.md)|2017.9.20|
|638|[Shopping Offers](/DynamicProgramming/Shopping_Offers.md)|2017.9.26|
|639|[Decode Ways II](/DynamicProgramming/Decode_Ways_II.md)|2018.2.23|
|646|[Maximum Length of Pair Chain](/DynamicProgramming/Maximum_Length_of_Pair_Chain.md)|2017.9.27|
|647|[Palindromic Substrings](DynamicProgramming/Palindromic_Substrings.md)|2017.9.28|
|650|[2 Keys Keyboard](/DynamicProgramming/2_Keys_Keyboard.md)|2017.9.29|
|673|[Number of Longest Increasing Subsequence](/DynamicProgramming/Number_of_Longest_Increasing_Subsequence.md)|2017.9.30|
|727|[Minimum Window Subsequence](/DynamicProgramming/Minimum_Window_Subsequence.md)|2018.2.25|
|746|[Min Cost Climbing Stairs](/DynamicProgramming/Min_Cost_Climbing_Stairs.md)|2018.5.7|

## Tree

[Tree traversal summary (preorder, inorder, postorder, level order)](/tree/Tree_traversal.md)

|Number|Name|Date|
|:---:|:---:|:---:|
|094|[Binary Tree Inorder Traversal](/tree/Binary_Tree_Inorder_Traversal.md)|2017.10.1|
|095|[Unique Binary Search Trees II](/tree/Unique_Binary_Search_Trees_II.md)|2017.10.2|
|096|[Unique Binary Search Trees](/tree/Unique_Binary_Search_Trees.md)|2017.10.2|
|098|[Validate Binary Search Tree](/tree/Validate_Binary_Search_Tree.md)|2017.10.3|
|100|[Same Tree](/tree/Same_Tree.md)|2017.10.5|
|101|[Symmetric Tree](/tree/Symmetric_Tree.md)|2017.10.5|
|102|[Binary Tree Level Order Traversal](/tree/Binary_Tree_Level_Order_Traversal.md)|2017.10.6|
|103|[Binary Tree Zigzag Level Order Traversal](/tree/Binary_Tree_Zigzag_Level_Order_Traversal.md)|2017.10.9|
|104|[Maximum Depth of Binary Tree](/tree/Maximum_Depth_of_Binary_Tree.md)|2017.10.10|
|105|[Construct Binary Tree from Preorder and Inorder Traversal](/tree/Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.md)|2017.10.10|
|106|[Construct Binary Tree from Inorder and Postorder Traversal](/tree/Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.md)|2017.10.11|
|107|[Binary Tree Level Order Traversal II](/tree/Binary_Tree_Level_Order_Traversal.md)|2017.10.11|
|108|[Convert Sorted Array to Binary Search Tree](/tree/Convert_Sorted_Array_to_Binary_Search_Tree.md)|2017.10.11|
|110|[Balanced Binary Tree](/tree/Balanced_Binary_Tree.md)|2017.10.11|
|111|[Minimum Depth of Binary Tree](/tree/Minimum_Depth_of_Binary_Tree.md)|2017.10.12|
|112|[Path Sum](/tree/Path_Sum.md)|2017.10.12|
|113|[Path Sum II](/tree/Path_Sum_II.md)|2017.10.12|
|114|[Flatten Binary Tree to Linked List](/tree/Flatten_Binary_Tree_to_Linked_List.md)|2017.10.12|
|116|[Populating Next Right Pointers in Each Node](/tree/Populating_Next_Right_Pointers_in_Each_Node.md)|2017.10.12|
|117|[Populating Next Right Pointers in Each Node II](/tree/Populating_Next_Right_Pointers_in_Each_Node_II.md)|2017.10.12|
|129|[Sum Root to Leaf Numbers](/tree/Sum_Root_to_Leaf_Numbers.md)|2017.10.12|
|144|[Binary Tree Preorder Traversal](/tree/Binary_Tree_Preorder_Traversal.md)|2017.10.9|
|145|[Binary Tree Postorder Traversal](/tree/Binary_Tree_Postorder_Traversal.md)|2017.10.9|
|173|[Binary Search Tree Iterator](/tree/Binary_Search_Tree_Iterator.md)|2017.10.14|
|199|[Binary Tree Right Side View](/tree/Binary_Tree_Right_Side_View.md)|2017.10.15|
|222|[Count Complete Tree Nodes](/tree/Count_Complete_Tree_Nodes.md)|2017.10.16|
|226|[Invert Binary Tree](/tree/Invert_Binary_Tree.md)|2017.10.16|
|230|[Kth Smallest Element in a BST](/tree/Kth_Smallest_Element_in_a_BST.md)|2017.10.16|
|235|[Lowest Common Ancestor of a Binary Search Tree](/tree/Lowest_Common_Ancestor_of_a_Binary_Search_Tree.md)|2017.10.16|
|236|[Lowest Common Ancestor of a Binary Tree](/tree/Lowest_Common_Ancestor_of_a_Binary_Tree.md)|2017.10.16|
|257|[Binary Tree Paths](/tree/Binary_Tree_Paths.md)|2017.10.16|
|337|[House Robber III](/tree/House_Robber_III.md)|2017.10.16|
|404|[Sum of Left Leaves](/tree/Sum_of_Left_Leaves.md)|2017.10.17|
|437|[Path Sum III](/tree/Path_Sum_III.md)|2017.10.18|
|449|[Serialize and Deserialize BST](/tree/Serialize_and_Deserialize_BST.md)|2017.10.19|
|450|[Delete Node in a BST](/tree/Delete_Node_in_a_BST.md)|2017.10.19|
|501|[Find Mode in Binary Search Tree](/tree/Find_Mode_in_Binary_Search_Tree.md)|2017.10.20|
|508|[Most Frequent Subtree Sum](/tree/Most_Frequent_Subtree_Sum.md)|2017.10.21|
|513|[Find Bottom Left Tree Value](/tree/Find_Bottom_Left_Tree_Value.md)|2017.10.21|
|515|[Find Largest Value in Each Tree Row](/tree/Find_Largest_Value_in_Each_Tree_Row.md)|2017.10.21|
|538|[Convert BST to Greater Tree](/tree/Convert_Sorted_Array_to_Binary_Search_Tree.md)|2017.10.21|
|543|[Diameter of Binary Tree](/tree/Diameter_of_Binary_Tree.md)|2017.10.21|
|563|[Binary Tree Tilt](/tree/Binary_Tree_Tilt.md)|2017.10.21|
|572|[Subtree of Another Tree](/tree/Subtree_of_Another_Tree.md)|2017.10.21|
|606|[Construct String from Binary Tree](/tree/Construct_String_from_Binary_Tree.md)|2017.10.21|
|617|[Merge Two Binary Trees](/tree/Merge_Two_Binary_Trees.md)|2017.10.21|
|623|[Add One Row to Tree](/tree/Add_One_Row_to_Tree.md)|2017.10.22|
|637|[Average of Levels in Binary Tree](/tree/Average_of_Levels_in_Binary_Tree.md)|2017.10.22|
|652|[Find Duplicate Subtrees](/tree/Find_Duplicate_Subtrees.md)|2017.10.22|
|652|[Two Sum IV - Input is a BST](/tree/Two_Sum_IV_-_Input_is_a_BST.md)|2017.10.22|
|654|[Maximum Binary Tree](/tree/Maximum_Binary_Tree.md)|2017.10.23|
|655|[Print Binary Tree](/tree/Print_Binary_Tree.md)|2017.10.23|
|662|[Maximum Width of Binary Tree](/tree/Maximum_Width_of_Binary_Tree.md)|2017.10.23|
|669|[Trim a Binary Search Tree](/tree/Trim_a_Binary_Search_Tree.md)|2017.10.23|
|671|[Second Minimum Node In a Binary Tree](/tree/Second_Minimum_Node_In_a_Binary_Tree.md)|2017.10.23|
|687|[Longest Univalue Path](/tree/Longest_Univalue_Path.md)|2017.10.24|

## String

```
''.join(s)
s.split()
map(str/int/function, iterable)
ord(), chr()
string.upper()/lower()
zip()/zipped(*)
any()/all()
sorted(iterable, key=len/lambda..., reverse=True)
```

|Number|Name|Date|
|:---:|:---:|:---:|
|003|[Longest Substring Without Repeating Characters](/string/Longest_Substring_Without_Repeating_Characters.md)|2017.10.25|
|005|[Longest Palindromic Substring](/string/Longest_Palindromic_Substring.md)|2017.10.28|
|006|[ZigZag Conversion](/string/ZigZag_Conversion.md)|2017.10.29|
|008|[String to Integer (atoi)](/string/String_to_Integer_(atoi).md)|2017.10.30|
|012|[Integer to Roman](/string/Integer_to_Roman.md)|2017.10.31|
|013|[Roman to Integer](/string/Roman_to_Integer.md)|2017.10.31|
|014|[Longest Common Prefix](/string/Longest_Common_Prefix.md)|2017.11.1|
|020|[Valid Parentheses](/string/Valid_Parentheses.md)|2017.11.2|
|028|[Implement strStr()](/string/Implement_strStr().md)|2017.11.2|
|038|[Count and Say](/string/Count_and_Say.md)|2017.11.2|
|043|[Multiply Strings](/string/Multiply_Strings.md)|2017.11.2|
|049|[Group Anagrams](/string/Group_Anagrams.md)|2017.11.2|
|058|[Length of Last Word](/string/Length_of_Last_Word.md)|2017.11.3|
|067|[Add Binary](/string/Add_Binary.md)|2017.11.3|
|071|[Simplify Path](/string/Simplify_Path.md)|2017.11.3|
|076|[Minimum Window Substring](/string/Minimum_Window_Substring.md)|2018.2.25|
|125|[Valid Palindrome](/string/Valid_Palindrome.md)|2017.11.3|
|151|[Reverse Words in a String](/string/Reverse_Words_in_a_String.md)|2017.11.3|
|165|[Compare Version Numbers](/string/Compare_Version_Numbers.md)|2017.11.3|
|227|[Basic Calculator II](/string/Basic_Calculator_II.md)|2017.11.6|
|344|[Reverse String](/string/Reverse_String.md)|2017.11.6|
|345|[Reverse Vowels of a String](/string/Reverse_Vowels_of_a_String.md)|2017.11.6|
|383|[Ransom Note](/string/Ransom_Note.md)|2017.11.6|
|385|[Mini Parser](/string/Mini_Parser.md)|2017.11.7|
|434|[Number of Segments in a String](/string/Number_of_Segments_in_a_String.md)|2017.11.7|
|443|[String Compression](/string/String_Compression.md)|2017.11.8|
|459|[Repeated Substring Pattern](/string/Repeated_Substring_Pattern.md)|2017.11.9|
|468|[Validate IP Address](/string/Validate_IP_Address.md)|2017.11.9|
|520|[Detect Capital](/string/Detect_Capital.md)|2017.11.9|
|521|[Longest Uncommon Subsequence I](/string/Longest_Uncommon_Subsequence_I.md)|2017.11.9|
|522|[Longest Uncommon Subsequence II](/string/Longest_Uncommon_Subsequence_II.md)|2017.11.9|
|537|[Complex Number Multiplication](/string/Complex_Number_Multiplication.md)|2017.11.11|
|539|[Minimum Time Difference](/string/Minimum_Time_Difference.md)|2017.11.12|
|541|[Reverse String II](/string/Reverse_String_II.md)|2017.11.12|
|551|[Student Attendance Record I](/string/Student_Attendance_Record_I.md)|2017.11.12|
|553|[Optimal Division](/string/Optimal_Division.md)|2017.11.12|
|556|[Next Greater Element III](/string/Next_Greater_Element_III.md)|2017.11.12|
|557|[Reverse Words in a String III](/string/Reverse_Words_in_a_String.md)|2017.11.12|
|583|[Delete Operation for Two Strings](/string/Delete_Operation_for_Two_Strings.md)|2017.11.12|
|609|[Find Duplicate File in System](/string/Find_Duplicate_File_in_System.md)|2017.11.13|
|657|[Judge Route Circle](/string/Judge_Route_Circle.md)|2017.11.13|
|678|[Valid Parenthesis String](/string/Valid_Parenthesis_String.md)|2017.11.13|
|680|[Valid Palindrome II](/string/Valid_Palindrome_II.md)|2017.11.13|
|686|[Repeated String Match](/string/Repeated_Substring_Pattern.md)|2017.11.13|
|696|[Count Binary Substrings](/string/Count_Binary_Substrings.md)|2017.11.14|
|722|[Remove Comments](/string/Remove_Comments.md)|2017.11.14|

## Hash Table

```
set()
collections.defaultdict(int/list/lambda...)
collections.Counter()
d.keys()/values()/items()/elements()
set1()/dict1() +/-/&/| set2()/dict2()
sorted(d.keys(), key=lambda i: (-d[i], i))[:k]
```

|Number|Name|Date|
|:---:|:---:|:---:|
|030|[Substring with Concatenation of All Words](/hash/Substring_with_Concatenation_of_All_Words.md)|2018.5.15|
|036|[Valid Sudoku](hash/Valid_Sudoku.md)|2017.11.19|
|136|[Single Number](/hash/Single_Number.md)|2017.11.19|
|138|[Copy List with Random Pointer](/hash/Copy_List_with_Random_Pointer.md)|2017.11.19|
|166|[Fraction to Recurring Decimal](/hash/Fraction_to_Recurring_Decimal.md)|2017.11.19|
|187|[Repeated DNA Sequences](/hash/Repeated_DNA_Sequences.md)|2017.11.19|
|202|[Happy Number](/hash/Happy_Number.md)|2017.11.19|
|204|[Count Primes](/hash/Count_Primes.md)|2017.11.19|
|205|[Isomorphic Strings](/hash/Isomorphic_Strings.md)|2017.11.20|
|242|[Valid Anagram](/hash/Valid_Anagram.md)|2017.11.20|
|274|[H-Index](/hash/H-Index.md)|2017.11.20|
|290|[Word Pattern](/hash/Word_Pattern.md)|2017.11.20|
|299|[Bulls and Cows](/hash/Bulls_and_Cows.md)|2017.11.21|
|347|[Top K Frequent Elements](/hash/Top_K_Frequent_Elements.md)|2017.11.21|
|349|[Intersection of Two Arrays](/hash/Intersection_of_Two_Arrays.md)|2017.11.21|
|350|[Intersection of Two Arrays II](/hash/Intersection_of_Two_Arrays_II.md)|2017.11.21|
|389|[Find the Difference](/hash/Find_the_Difference.md)|2017.11.21|
|409|[Longest Palindrome](/hash/Longest_Palindrome.md)|2017.11.21|
|438|[Find All Anagrams in a String](/hash/Find_All_Anagrams_in_a_String.md)|2017.11.21|
|447|[Number of Boomerangs](/hash/Number_of_Boomerangs.md)|2017.11.22|
|451|[Sort Characters By Frequency](/hash/Sort_Characters_By_Frequency.md)|2017.11.22|
|454|[4Sum II](/hash/4Sum_II.md)|2017.11.22|
|463|[Island Perimeter](/hash/Island_Perimeter.md)|2017.11.22|
|500|[Keyboard Row](/hash/Keyboard_Row.md)|2017.11.22|
|525|[Contiguous Array](/hash/Contiguous_Array.md)|2017.11.22|
|-|-|Happy Thanksgiving|
|535|[Encode and Decode TinyURL](/hash/Encode_and_Decode_TinyURL.md)|2017.11.27|
|554|[Brick Wall](/hash/Brick_Wall.md)|2017.11.27|
|575|[Distribute Candies](/hash/Distribute_Candies.md)|2017.11.27|
|599|[Minimum Index Sum of Two Lists](/hash/Minimum_Index_Sum_of_Two_Lists.md)|2017.11.27|
|645|[Set Mismatch](/hash/Set_Mismatch.md)|2017.11.27|
|648|[Replace Words](/hash/Replace_Words.md)|2017.11.27|
|676|[Implement Magic Dictionary](/hash/Implement_Magic_Dictionary.md)|2017.11.27|
|690|[Employee Importance](/hash/Employee_Importance.md)|2017.11.27|
|692|[Top K Frequent Words](/hash/Top_K_Frequent_Words.md)|2017.11.28|
|718|[Maximum Length of Repeated Subarray](/hash/Maximum_Length_of_Repeated_Subarray.md)|2017.11.28|
|720|[Longest Word in Dictionary](/hash/Longest_Word_in_Dictionary.md)|2017.11.29|
|734|[Sentence Similarity](/hash/Sentence_Similarity.md)|2017.11.30|
|760|[Find Anagram Mappings](/hash/Find_Anagram_Mappings.md)|2018.4.4|

## Math

- Division

```
if token=='/':
    if t2/t1<0 and t2%t1:
        val=str(t2/t1+1)
    else:
        val=str(t2/t1)
```

|Number|Name|Date|
|:---:|:---:|:---:|
|002|[Add Two Numbers](/math/Add_Two_Numbers.md)|2017.11.30|
|007|[Reverse Integer](/math/Reverse_Integer.md)|2017.11.30|
|009|[Palindrome Number](/math/Palindrome_Number.md)|2017.12.1|
|029|[Divide Two Integers](/math/Divide_Two_Integers.md)|2017.12.1|
|050|[Pow(x, n)](/math/Pow(x,n).md)|2017.12.2|
|069|[Sqrt(x)](/math/Sqrt(x).md)|2017.12.3|
|168|[Excel Sheet Column Title](/math/Excel_Sheet_Column_Title.md)|2017.12.3|
|171|[Excel Sheet Column Number](/math/Excel_Sheet_Column_Number.md)|2017.12.3|
|172|[Factorial Trailing Zeroes](/math/Factorial_Trailing_Zeroes.md)|2017.12.3|
|223|[Rectangle Area](/math/Rectangle_Area.md)|2017.12.3|
|231|[Power of Two](/math/Power_of_Two.md)|2017.12.4|
|258|[Add Digits](/math/Add_Digits.md)|2017.12.4|
|313|[*Super Ugly Number](/math/Super_Ugly_Number.md)|2017.12.5|
|-|-|Happy Final|
|319|[Bulb Switcher](/math/Bulb_Switcher.md)|2017.12.11|
|326|[Power of Three](/math/Power_of_Three.md)|2017.12.11|
|365|[Water and Jug Problem](/math/Water_and_Jug_Problem.md)|2017.12.13|
|367|[Valid Perfect Square](/math/Valid_Perfect_Square.md)|2017.12.13|
|-|-|Happy Winter Vacation|
|396|[Rotate Function](/math/Rotate_Function.md)|2018.1.11|
|397|[Integer Replacement](/math/Integer_Replacement.md)|2018.1.11|
|400|[Nth Digit](/math/Nth_Digit.md)|2018.1.11|
|415|[Add Strings](/math/Add_Strings.md)|2018.1.12|
|423|[Reconstruct Original Digits from English](/math/Reconstruct_Original_Digits_from_English.md)|2018.1.12|
|441|[Arranging Coins](/math/Arranging_Coins.md)|2018.1.14|
|453|[Minimum Moves to Equal Array Elements](/math/Minimum_Moves_to_Equal_Array_Elements.md)|2018.1.15|
|462|[Minimum Moves to Equal Array Elements II](/math/Minimum_Moves_to_Equal_Array_Elements_II.md)|2018.1.15|
|507|[Perfect Number](/math/Perfect_Number.md)|2018.1.15|
|592|[Fraction Addition and Subtraction](/math/Fraction_Addition_and_Subtraction.md)|2018.1.15|
|593|[Valid Square](/math/Valid_Square.md)|2018.1.15|
|598|[Range Addition II](/math/Range_Addition_II.md)|2018.1.15|
|640|[Solve the Equation](/math/Solve_the_Equation.md)|2018.1.15|
|670|[Maximum Swap](/math/Maximum_Swap.md)|2018.1.16|
|728|[Self Dividing Numbers](/math/Self_Dividing_Numbers.md)|2018.1.16|
|754|[Reach a Number](/math/Reach_a_Number.md)|2018.1.16|

## Divide and Conquer

- binary search
- mergesort and count/Binary indexed tree(bisect.bisect_right(s, num))
- defensive coding:
```
if not hp or hp[0]:
    ...
    
while hp:
    hp.pop()
    ...
```

|Number|Name|Date|
|:---:|:---:|:---:|
|327|[Count of Range Sum](/divide_and_conquer/Count_of_Range_Sum.md)|2018.2.5|
|084|[Largest Rectangle in Histogram](/divide_and_conquer/Largest_Rectangle_in_Histogram.md)|2018.2.5|
|493|[Reverse Pairs](/divide_and_conquer/Reverse_Pairs.md)|2018.2.5|
|315|[Count of Smaller Numbers After Self](/divide_and_conquer/Count_of_Smaller_Numbers_After_Self.md)|2018.2.5|
|004|[Median of Two Sorted Arrays](/divide_and_conquer/Median_of_Two_Sorted_Arrays.md)|2018.2.7|
|023|[Merge k Sorted Lists](/divide_and_conquer/Merge_k_Sorted_Lists.md)|2018.2.7|
|218|[The Skyline Problem](/divide_and_conquer/The_Skyline_Problem.md)|2018.2.9|
|312|[Burst Balloons](/divide_and_conquer/Burst_Balloons.md)|2018.2.9|

## Design

- trade-off between functions

|Number|Name|Date|
|:---:|:---:|:---:|
|155|[Min Stack](/order/Min_Stack.md)|2018.1.23|
|170|[Two Sum III - Data structure design](/order/Two_Sum_III_-_Data_structure_design.md)|2018.1.24|
|208|[Implement Trie (Prefix Tree)](/order/Implement_Trie_(Prefix_Tree).md)|2018.1.26|
|211|[Add and Search Word - Data structure design](/order/Add_and_Search_Word_-_Data_structure_design.md)|2018.1.26|
|225|[Implement Stack using Queues](/order/Implement_Stack_using_Queues.md)|2018.1.28|
|232|[Implement Queue using Stacks](/order/Implement_Queue_using_Stacks.md)|2018.1.28|
|244|[Shortest Word Distance II](/order/Shortest_Word_Distance_II.md)|2018.1.30|
|251|[Flatten 2D Vector](/order/Flatten_2D_Vector.md)|2018.2.1|
|146|[LRU Cache](/design/LRU_Cache.md)|2018.2.20|
|297|[Serialize and Deserialize Binary Tree](/design/Serialize_and_Deserialize_Binary_Tree.md)|2018.2.20|
|341|[Flatten Nested List Iterator](/design/Flatten_Nested_List_Iterator.md)|2018.2.21|
|295|[Find Median from Data Stream](/design/Find_Median_from_Data_Stream.md)|2018.2.21|

## Order

- dummy node: 

```
dummy=ListNode(0)
dummy.next=head
# code here
...
return dummy.next
```

- fast and slow(prev) (cycle, mid node)
- int(binary string, 2)
- bin(int) -> string
- dfs and bfs iteration:

```
while stack:
    x, y=stack.pop()
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if x+dx>=0 and x+dx<m and y+dy>=0 and y+dy<n and grid[x+dx][y+dy]=='1':
            grid[x+dx][y+dy]='0'
            stack.append((x+dx, y+dy))  
```
- bit manipulation:
```
delete the last zero:
n&=n-1
```

|Number|Name|Date|Topics|
|:---:|:---:|:---:|:---:|
|010|[Regular Expression Matching](/order/Regular_Expression_Matching.md)|2018.2.14|Dynamic Programming, String, Backtracking|
|019|[Remove Nth Node From End of List](/order/Remove_Nth_Node_From_End_of_List.md)|2018.1.16|Linked List, Two Pointers|
|021|[Merge Two Sorted Lists](/order/Merge_Two_Sorted_Lists.md)|2018.1.17|Linked List|
|024|[Swap Nodes in Pairs](/order/Swap_Nodes_in_Pairs.md)|2018.1.17|Linked List|
|061|[Rotate List](/order/Rotate_List.md)|2018.1.16|Linked List, Two Pointers|
|072|[Edit Distance](/order/Edit_Distance.md)|2018.2.14|Dynamic Programming, String|
|082|[Remove Duplicates from Sorted List II](/order/Remove_Duplicates_from_Sorted_List_II.md)|2018.1.19|Linked List|
|083|[Remove Duplicates from Sorted List](/order/Remove_Duplicates_from_Sorted_List.md)|2018.1.19|Linked List|
|085|[Maximal Rectangle](/order/Maximal_Rectangle.md)|2018.2.14|Dynamic Programming, Array, Hash Table, Stack|
|086|[Partition List](/order/Partition_List.md)|2018.1.19|Linked List, Two Pointers|
|*092|[Reverse Linked List II](/order/Reverse_Linked_List_II.md)|2018.1.19|Linked List|
|109|[Convert Sorted List to Binary Search Tree](/order/Convert_Sorted_List_to_Binary_Search_Tree.md)|2018.1.20|Linked List, Depth-first Search|
|115|[Distinct Subsequences](/order/Distinct_Subsequences.md)|2018.2.18|Dynamic Programming, String|
|*126|[Word Ladder II](/order/Word_Ladder_II.md)|2018.2.3|Array, String, Backtracking, Breadth-first Search|
|127|[Word Ladder](/order/Word_Ladder.md)|2018.1.20|Breadth-first Search|
|130|[Surrounded Regions](/order/Surrounded_Regions.md)|2018.1.21|Breadth-first Search, Depth-first Search|
|133|[Clone Graph](/order/Clone_Graph.md)|2018.1.21|Breadth-first Search, Depth-first Search, Graph|
|134|[Gas Station](/order/Gas_Station.md)|2018.1.21|Greedy|
|137|[Single Number II](/order/Single_Number_II.md)|2018.1.21|Bit Manipulation|
|141|[Linked List Cycle](/order/Linked_List_Cycle.md)|2018.1.21|Linked List, Two Pointers|
|142|[Linked List Cycle II](/order/Linked_List_Cycle_II.md)|2018.1.22|Linked List, Two Pointers|
|143|[Reorder List](/order/Reorder_List.md)|2018.1.22|Linked List|
|147|[Insertion Sort List](/order/Insertion_Sort_List.md)|2018.1.23|Linked List, Sort|
|148|[Sort List](/order/Sort_List.md)|2018.1.23|Linked List, Sort|
|149|[Max Points on a Line](/order/Max_Points_on_a_Line.md)|2018.7.16|Hash Table, Math|
|150|[Evaluate Reverse Polish Notation](/order/Evaluate_Reverse_Polish_Notation.md)|2018.1.23|Stack|
|*156|[Binary Tree Upside Down](/order/Binary_Tree_Upside_Down.md)|2018.1.23|Tree|
|157|[Read N Characters Given Read4](/order/Read_N_Characters_Given_Read4.md)|2018.1.23|String|
|160|[Intersection of Two Linked Lists](/order/Intersection_of_Two_Linked_Lists.md)|2018.1.23|Linked List|
|161|[One Edit Distance](/order/One_Edit_Distance.md)|2018.1.24|String|
|163|[Missing Ranges](/order/Missing_Ranges.md)|2018.1.24|Array|
|186|[Reverse Words in a String II](/order/Reverse_Words_in_a_String_II.md)|2018.1.24|String|
|190|[Reverse Bits](order/Reverse_Bits.md)|2018.1.25|Bit Manipulation|
|191|[Number of 1 Bits](/order/Number_of_1_Bits.md)|2018.1.25|Bit Manipulation|
|200|[Number of Islands](/order/Number_of_Islands.md)|2018.1.25|Breadth-first Search, Depth-first Search|
|201|[Bitwise AND of Numbers Range](/order/Bitwise_AND_of_Numbers_Range.md)|2018.1.25|Bit Manipulation|
|203|[Remove Linked List Elements](/order/Remove_Linked_List_Elements.md)|2018.1.25|Linked List|
|206|[Reverse Linked List](/order/Remove_Duplicates_from_Sorted_List.md)|2018.1.22|Linked List|
|207|[Course Schedule](/order/Course_Schedule.md)|2018.1.25|Breadth-first Search, Depth-first Search, Graph, Topological Sort|
|210|[Course Schedule II](/order/Course_Schedule_II.md)|2018.1.26|Breadth-first Search, Depth-first Search, Graph, Topological Sort|
|215|[Kth Largest Element in an Array](/order/Kth_Largest_Element_in_an_Array.md)|2018.1.27|Divide and Conquer, Heap|
|220|[Contains Duplicate III](/order/Contains_Duplicate_III.md)|2018.1.28|Binary Search Tree|
|234|[Palindrome Linked List](/order/Palindrome_Linked_List.md)|2018.1.28|Linked List, Two Pointers|
|237|[Delete Node in a Linked List](/order/Delete_Node_in_a_Linked_List.md)|2018.1.29|Linked List|
|240|[Search a 2D Matrix II](/order/Search_a_2D_Matrix_II.md)|2018.1.29|Binary Search, Divide and Conquer|
|241|[Different Ways to Add Parentheses](/order/Different_Ways_to_Add_Parentheses.md)|2018.1.30|Divide and Conquer|
|243|[Shortest Word Distance](/order/Shortest_Word_Distance.md)|2018.1.30|Array|
|245|[Shortest Word Distance III](/order/Shortest_Word_Distance_III.md)|2018.1.30|Array|
|246|[Strobogrammatic Number](/order/Strobogrammatic_Number.md)|2018.1.31|Hash Table, Math|
|247|[Strobogrammatic Number II](/order/Strobogrammatic_Number_II.md)|2018.1.31|Recursion, Math|
|249|[Group Shifted Strings](/order/Group_Shifted_Strings.md)|2018.2.1|Hash Table, String|
|250|[Count Univalue Subtrees](/order/Count_Univalue_Subtrees.md)|2018.2.1|Tree|
|252|[Meeting Rooms](/order/Meeting_Rooms.md)|2018.2.1|Sort|
|253|[Meeting Rooms II](/order/Meeting_Rooms_II.md)|2018.2.1|Heap, Greedy, Sort|
|254|[Factor Combinations](/order/Factor_Combinations.md)|2018.2.1|Backtracking|
|*255|[Verify Preorder Sequence in Binary Search Tree](/order/Verify_Preorder_Sequence_in_Binary_Search_Tree.md)|2018.2.2|Stack, Tree|
|256|[Paint House](/order/Paint_House.md)|2018.2.2|Dynamic Programming|
|259|[3Sum Smaller](/order/3Sum_Smaller.md)|2018.2.8|Array, Two Pointers|
|265|[Paint House II](/order/Paint_House_II.md)|2018.2.2|Dynamic Programming|
|266|[Palindrome Permutation](/order/Palindrome_Permutation.md)|2018.2.8|Hash Table|
|267|[Palindrome Permutation II](/order/Palindrome_Permutation_II.md)|2018.2.8|Backtracking|
|270|[Closest Binary Search Tree Value](/order/Closest_Binary_Search_Tree_Value.md)|2018.2.8|Binary Search, Tree|
|272|[Closest Binary Search Tree Value II](/order/Closest_Binary_Search_Tree_Value_II.md)|2018.2.8|Stack, Tree|
|292|[Nim Game](/order/Nim_Game.md)|2018.4.4|Brainteaser|
|307|[Range Sum Query - Mutable](/order/Range_Sum_Query-Mutable.md)|2018.2.26|Binary Indexed Tree|
|308|[Range Sum Query 2D - Mutable](/order/Range_Sum_Query_2D-Mutable.md)|2018.2.27|Binary Indexed Tree|
|316|[Remove Duplicate Letters](/order/Remove_Duplicate_Letters.md)|2018.5.7|Stack, Greedy|
|323|[Number of Connected Components in an Undirected Graph](/order/Number_of_Connected_Components_in_an_Undirected_Graph.md)|2018.3.22|Breadth-first Search, Depth-first Search, Graph|
|356|[Line Reflection](/order/Line_Reflection.md)|2018.7.16|Hash Table, Math|
|378|[Kth Smallest Element in a Sorted Matrix](/order/Kth_Smallest_Element_in_a_Sorted_Matrix.md)|2018.2.18|Binary Search, Heap|
|387|[First Unique Character in a String](/order/First_Unique_Character_in_a_String.md)|2018.5.7|Hash Table, String|
|398|[Random Pick Index](/order/Random_Pick_Index.md)|2018.7.8|Reservoir Sampling|
|402|[Remove K Digits](/order/Remove_K_Digits.md)|2018.6.17|Stack, Greedy|
|406|[Queue Reconstruction by Height](/order/Queue_Reconstruction_by_Height.md)|2018.5.7|Greedy|
|461|[Hamming Distance](/order/Hamming_Distance.md)|2018.4.4|Bit Manipulation|
|477|[Total Hamming Distance](/order/Total_Hamming_Distance.md)|2018.4.4|Bit Manipulation|
|719|[Find K-th Smallest Pair Distance](/order/Find_K-th_Smallest_Pair_Distance.md)|2018.2.18|Binary Search, Heap|
|763|[Partition Labels](/order/Partition_Labels.md)|2018.5.7|Two Pointers, Greedy|
|864|[Random Pick with Blacklist](/order/Random_Pick_with_Blacklist.md)|2018.7.8|Hash Table, Random|

## Leetcode Contest

|Number|Name|Date|Topics|
|:---:|:---:|:---:|:---:|
|Weekly Contest 68|[766. Toeplitz Matrix](/contest/Toeplitz_Matrix.md)|2018.1.21|Array|
|-|[767. Reorganize String](/contest/Reorganize_String.md)|2018.1.21|String, Heap, Greedy, Sort|
|-|[769. Max Chunks To Make Sorted](/contest/Max_Chunks_To_Make_Sorted.md)|2018.1.21|Array|
|-|[768. Max Chunks To Make Sorted II](/contest/Max_Chunks_To_Make_Sorted_II.md)|2018.1.21|Array|
|Weekly Contest 69|[771. Jewels and Stones](/contest/Jewels_and_Stones.md)|2018.1.28|Hash Table|
|-|[775. Global and Local Inversions](/contest/Global_and_Local_Inversions.md)|2018.1.28|Array, Math|
|-|[773. Sliding Puzzle](/contest/Sliding_Puzzle.md)|2018.1.28|Breadth-first Search|
|-|[774. Minimize Max Distance to Gas Station](/contest/Minimize_Max_Distance_to_Gas_Station.md)|2018.1.28|Binary Search|
|Weekly Contest 70|[779. K-th Symbol in Grammar](/contest/K-th_Symbol_in_Grammar.md)|2018.2.4|Recursion|
|-|[777. Swap Adjacent in LR String](/order/Swap_Nodes_in_Pairs.md)|2018.2.4|Brainteaser|
|-|[776. Split BST](/contest/Split_BST.md)|2018.2.4|Binary Search Tree|
|-|[778. Swim in Rising Water](/contest/Swim_in_Rising_Water.md)|2018.2.4|Binary Search, Heap, Depth-first Search|
|Weekly Contest 71|[783. Minimum Distance Between BST Nodes](/contest/Minimum_Distance_Between_BST_Nodes.md)|2018.2.10|Binary Search Tree|
|-|[781. Rabbits in Forest](/contest/Rabbits_in_Forest.md)|2018.2.10|
|-|[780. Reaching Points](/contest/Reaching_Points.md)|2018.2.10|
|-|[782. Transform to Chessboard](/contest/Transform_to_Chessboard.md)|2018.2.10|
|Weekly Contest 72|[784. Letter Case Permutation](/contest/Letter_Case_Permutation.md)|2018.2.18|Backtracking|
|-|[785. Is Graph Bipartite?](/contest/Is_Graph_Bipartite%3F.md)|2018.2.18|Stack|
|-|[787. Cheapest Flights Within K Stops](/contest/Cheapest_Flights_Within_K_Stops.md)|2018.2.18|Heap, Breadth-first Search|
|-|[786. K-th Smallest Prime Fraction](/contest/K-th_Smallest_Prime_Fraction.md)|2018.2.18|Heap, Binary Search|
|Weekly Contest 73|[788. Rotated Digits](/contest/Rotated_Digits.md)|2018.2.25|
|-|[789. Escape The Ghosts](/contest/Escape_The_Ghosts.md)|2018.2.25|
|-|[791. Custom Sort String](/contest/Custom_Sort_String.md)|2018.2.25|
|-|[790. Domino and Tromino Tiling](/contest/Domino_and_Tromino_Tiling.md)|2018.2.25|
|Weekly Contest 74|[794. Valid Tic-Tac-Toe State](/contest/Valid_Tic-Tac-Toe_State.md)|2018.3.6|Math, Recursion|
|-|[792. Number of Matching Subsequences](/contest/Number_of_Matching_Subsequences.md)|2018.3.6|Array|
|-|[795. Number of Subarrays with Bounded Maximum](/contest/Number_of_Subarrays_with_Bounded_Maximum.md)|2018.3.6|Array|
|-|[793. Preimage Size of Factorial Zeroes Function](/contest/Preimage_Size_of_Factorial_Zeroes_Function.md)|2018.3.6|Binary Search|
|Weekly Contest 75|[796. Rotate String](/contest/Rotate_String.md)|2018.3.12|
|-|[797. All Paths From Source to Target](/contest/All_Paths_From_Source_to_Target.md)|2018.3.12|
|-|[799. Champagne Tower](/contest/Champagne_Tower.md)|2018.3.12|
|-|[798. Smallest Rotation with Highest Score](/contest/Smallest_Rotation_with_Highest_Score.md)|2018.3.12|
|Weekly Contest 76|[800. Similar RGB Color](/contest/Similar_RGB_Color.md)|2018.3.19|String, Math|
|-|[801. Minimum Swaps To Make Sequences Increasing](/contest/Minimum_Swaps_To_Make_Sequences_Increasing.md)|2018.3.19|Dynamic Programming|
|-|[802. Find Eventual Safe States](/contest/Find_Eventual_Safe_States.md)|2018.3.19|Depth-first Search, Graph|
|Weekly Contest 77|[804. Unique Morse Code Words](/contest/Unique_Morse_Code_Words.md)|2018.3.26|
|-|[806. Number of Lines To Write String](/contest/Number_of_Lines_To_Write_String.md)|2018.3.26|
|-|[807. Max Increase to Keep City Skyline](/contest/Max_Increase_to_Keep_City_Skyline.md)|2018.3.26|
|-|[805. Split Array With Same Average](/contest/Split_Array_With_Same_Average.md)|2018.3.26|
|Weekly Contest 78|[811. Subdomain Visit Count](/contest/Subdomain_Visit_Count.md)|2018.4.3|String|
|-|[809. Expressive Words](/contest/Expressive_Words.md)|2018.4.3|String|
|-|[808. Soup Servings](/contest/Soup_Servings.md)|2018.4.3|Dynamic Programming|
|-|[810. Chalkboard XOR Game](/contest/Chalkboard_XOR_Game.md)|2018.4.3|Math|
|Weekly Contest 79|[812. Largest Triangle Area](/contest/Largest_Triangle_Area.md)|2018.4.9|Math|
|-|[814. Binary Tree Pruning](/contest/Binary_Tree_Pruning.md)|2018.4.9|Tree|
|-|[813. Largest Sum of Averages](/contest/Largest_Sum_of_Averages.md)|2018.4.9|Dynamic Programming|
|-|[815. Bus Routes](/contest/Bus_Routes.md)|2018.4.9|Breadth-first Search|
|Weekly Contest 80|[819. Most Common Word](/contest/Most_Common_Word.md)|2018.4.18|String|
|-|[817. Linked List Components](/contest/Linked_List_Components.md)|2018.4.18|Linked List|
|-|[816. Ambiguous Coordinates](/contest/Ambiguous_Coordinates.md)|2018.4.18|String|
|-|[818. Race Car](/contest/Race_Car.md)|2018.4.18|Dynamic Programming|
|Weekly Contest 81|[821. Shortest Distance to a Character](/contest/Shortest_Distance_to_a_Character.md)|2018.4.24|
|-|[822. Card Flipping Game](/contest/Card_Flipping_Game.md)|2018.4.24|
|-|[820. Short Encoding of Words](/contest/Short_Encoding_of_Words.md)|2018.4.24|
|-|[823. Binary Trees With Factors](/contest/Binary_Trees_With_Factors.md)|2018.4.24|
|Weekly Contest 82|[824. Goat Latin](/contest/Goat_Latin.md)|2018.4.28|
|-|[825. Friends Of Appropriate Ages](/contest/Friends_Of_Appropriate_Ages.md)|2018.4.28|
|-|[826. Most Profit Assigning Work](/contest/Most_Profit_Assigning_Work.md)|2018.4.28|
|-|[827. Making A Large Island](/contest/Making_A_Large_Island.md)|2018.4.28|
|Weekly Contest 83|[830. Positions of Large Groups](/contest/Positions_of_Large_Groups.md)|2018.5.6|Array|
|-|[831. Masking Personal Information](/contest/Masking_Personal_Information.md)|2018.5.6|String|
|-|[829. Consecutive Numbers Sum](/contest/Consecutive_Numbers_Sum.md)|2018.5.6|Math|
|-|[828. Unique Letter String](/contest/Unique_Letter_String.md)|2018.5.6|Two Pointers|
|Weekly Contest 84|[832. Flipping an Image](/contest/Flipping_an_Image.md)|2018.5.13|
|-|[833. Find And Replace in String](/contest/Find_And_Replace_in_String.md)|2018.5.13|
|-|[835. Image Overlap](/contest/Image_Overlap.md)|2018.5.13|
|-|[834. Sum of Distances in Tree](/contest/Sum_of_Distances_in_Tree.md)|2018.5.13|
|Weekly Contest 85|[836. Rectangle Overlap](/contest/Rectangle_Overlap.md)|2018.5.21|Math|
|-|[838. Push Dominoes](/contest/Push_Dominoes.md)|2018.5.21|Two Pointers, Dynamic Programming|
|-|[837. New 21 Game](/contest/New_21_Game.md)|2018.5.21|Dynamic Programming|
|-|[839. Similar String Groups](/contest/Similar_String_Groups.md)|2018.5.21|Graph, Union Find|
|Weekly Contest 86|[840. Magic Squares In Grid](/contest/Magic_Squares_In_Grid.md)|2018.5.28|Array|
|-|[841. Keys and Rooms](/contest/Keys_and_Rooms.md)|2018.5.28|Depth-first Search, Graph|
|-|[842. Split Array into Fibonacci Sequence](/contest/Split_Array_into_Fibonacci_Sequence.md)|2018.5.28|String, Greedy|
|-|[843. Guess the Word](/contest/Guess_the_Word.md)|2018.5.28|Minimax|
|Weekly Contest 87|[844. Backspace String Compare](/contest/Backspace_String_Compare.md)|2018.6.2|Two Pointers, Stack|
|-|[845. Longest Mountain in Array](/contest/Longest_Mountain_in_Array.md)|2018.6.2|Two Pointers|
|-|[846. Hand of Straights](/contest/Hand_of_Straights.md)|2018.6.2|Hash Table|
|-|[847. Shortest Path Visiting All Nodes](/contest/Shortest_Path_Visiting_All_Nodes.md)|2018.6.2|Dynamic Programming, Breadth-first Search|
|Weekly Contest 88|[848. Shifting Letters](/contest/Shifting_Letters.md)|2018.6.10|String|
|-|[849. Maximize Distance to Closest Person](/contest/Maximize_Distance_to_Closest_Person.md)|2018.6.10|Array|
|-|[851. Loud and Rich](/contest/Loud_and_Rich.md)|2018.6.10|Depth-first Search|
|-|[850. Rectangle Area II](/contest/Rectangle_Area_II.md)|2018.6.10|Segment Tree|
|Weekly Contest 89|[852. Peak Index in a Mountain Array](/contest/Peak_Index_in_a_Mountain_Array.md)|2018.6.17|Binary Search|
|-|[853. Car Fleet](/contest/Car_Fleet.md)|2018.6.17|Stack|
|-|[855. Exam Room](/contest/Exam_Room.md)|2018.6.17|Map|
|-|[854. K-Similar Strings](/contest/K-Similar_Strings.md)|2018.6.17|Breadth-first Search, Graph|
|Weekly Contest 90|[859. Buddy Strings](/contest/Buddy_Strings.md)|2018.6.27|String|
|-|[856. Score of Parentheses](/contest/Score_of_Parentheses.md)|2018.6.27|String, Stack|
|-|[858. Mirror Reflection](/contest/Mirror_Reflection.md)|2018.6.27|Math|
|-|[857. Minimum Cost to Hire K Workers](/contest/Minimum_Cost_to_Hire_K_Workers.md)|2018.6.27|Heap|
|Weekly Contest 91|[860. Lemonade Change](/contest/Lemonade_Change.md)|2018.7.3|Greedy|
|-|[863. All Nodes Distance K in Binary Tree](/contest/All_Nodes_Distance_K_in_Binary_Tree.md)|2018.7.3|Tree, Depth-first Search, Breadth-first Search|
|-|[861. Score After Flipping Matrix](/contest/Score_After_Flipping_Matrix.md)|2018.7.3|Greedy|
|-|[862. Shortest Subarray with Sum at Least K](/contest/Shortest_Subarray_with_Sum_at_Least_K.md)|2018.7.3|Deque|
|Weekly Contest 92|[867. Transpose Matrix](/contest/Transpose_Matrix.md)|2018.7.8|Array|
|-|[865. Smallest Subtree with all the Deepest Nodes](/contest/Smallest_Subtree_with_all_the_Deepest_Nodes.md)|2018.7.8|Tree|
|-|[866. Prime Palindrome](/contest/Prime_Palindrome.md)|2018.7.8|Math|
|-|[864. Shortest Path to Get All Keys](/contest/Shortest_Path_to_Get_All_Keys.md)|2018.7.8|Heap, Breadth-first Search|
|Weekly Contest 93|[868. Binary Gap](/contest/Binary_Gap.md)|2018.7.16|Math|
|-|[869. Reordered Power of 2](/contest/Reordered_Power_of_2.md)|2018.7.16|Math|
|-|[870. Advantage Shuffle](/contest/Advantage_Shuffle.md)|2018.7.16|Array, Greedy|
|-|[871. Minimum Number of Refueling Stops](/contest/Minimum_Number_of_Refueling_Stops.md)|2018.7.16|Dynamic Programming, Heap|
|Weekly Contest 94|[872. Leaf-Similar Trees](/contest/Leaf-Similar_Trees.md)|2018.7.22|
|-|[874. Walking Robot Simulation](/contest/Walking_Robot_Simulation.md)|2018.7.22|
|-|[875. Koko Eating Bananas](/contest/Koko_Eating_Bananas.md)|2018.7.22|
|-|[873. Length of Longest Fibonacci Subsequence](/contest/Length_of_Longest_Fibonacci_Subsequence.md)|2018.7.22|