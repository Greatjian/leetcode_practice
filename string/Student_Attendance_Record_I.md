# 551. Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:

- 'A' : Absent.
- 'L' : Late.
- 'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:

    Input: "PPALLP"
    Output: True

Example 2:

    Input: "PPALLL"
    Output: False
    
## Method:

    class Solution(object):
        def checkRecord(self, s):
            """
            :type s: str
            :rtype: bool
            """
            for i in range(len(s)-2):
                if s[i]==s[i+1]==s[i+2]=='L':
                    return False
            if s.count('A')>1:
                return False
            return True
            
复杂版：

    class Solution(object):
        def checkRecord(self, s):
            """
            :type s: str
            :rtype: bool
            """
            a_count, l_count=0, 0
            for i in s:
                if i=='A':
                    a_count+=1
                if a_count>1:
                    return False
                if i=='L':
                    l_count+=1
                else:
                    l_count=0
                if l_count==3:
                    return False
            return True
            
            
## Solution:

    class Solution(object):
        def checkRecord(self, s):
            """
            :type s: str
            :rtype: bool
            """
            return s.count('A')<=1 and 'LLL' not in s
            