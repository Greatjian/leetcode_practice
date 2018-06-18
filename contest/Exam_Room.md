# 855. Exam Room

In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

Example 1:

    Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
    Output: [null,0,9,4,2,null,5]

    Explanation:
    ExamRoom(10) -> null
    seat() -> 0, no one is in the room, then the student sits at seat number 0.
    seat() -> 9, the student sits at the last seat number 9.
    seat() -> 4, the student sits at the last seat number 4.
    seat() -> 2, the student sits at the last seat number 2.
    leave(4) -> null
    seat() -> 5, the student​​​​​​​ sits at the last seat number 5.
​​​​​​​

Note:

- 1 <= N <= 10^9
- ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
- Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.

## Method:

O(n) seat, O(1) leave, TLE:

    class ExamRoom(object):
    
        def __init__(self, N):
            """
            :type N: int
            """
            self.l=[0]*N
            
        def seat(self):
            """
            :rtype: int
            """
            N=len(self.l)
            # if all(self.l[i]==0 for i in range(N)):
            #     return 0
            left=[N]*N
            right=[N]*N
            for i in range(N):
                if self.l[i]:
                    left[i]=right[i]=0
            for i in range(1, N):
                if right[i-1]!=N and right[i]!=0:
                    right[i]=right[i-1]+1
            for i in range(N-2, -1, -1):
                if left[i+1]!=N and left[i]!=0:
                    left[i]=left[i+1]+1
            # print left, right
            maxIdx, maxVal=-1, float('-inf')
            for i in range(N):
                if min(left[i], right[i])>maxVal:
                    maxVal=min(left[i], right[i])
                    maxIdx=i
            self.l[maxIdx]=1
            return maxIdx
    
        def leave(self, p):
            """
            :type p: int
            :rtype: void
            """
            self.l[p]=0
    
    # Your ExamRoom object will be instantiated and called as such:
    # obj = ExamRoom(N)
    # param_1 = obj.seat()
    # obj.leave(p)
    
## Solution:

only record the index of seated place, pay attention to corner cases,
O(n) seat, O(1) leave:

    class ExamRoom(object):
    
        def __init__(self, N):
            """
            :type N: int
            """
            self.s=[]
            self.N=N
            
    
        def seat(self):
            """
            :rtype: int
            """
            if not self.s:
                self.s.append(0)
                return 0
            d={val:idx for idx, val in enumerate(self.s)}
            maxLen, maxIdx=float('-inf'), -1
            if self.s[0]!=0:
                maxLen, maxIdx=self.s[0], 0
            if self.s[-1]!=self.N-1:
                if self.N-1-self.s[-1]>maxLen:
                    maxLen=self.N-1-self.s[-1]
                    maxIdx=self.N-1
            for i in range(1, len(self.s)):
                if (self.s[i]-self.s[i-1])/2>maxLen:
                    maxLen=(self.s[i]-self.s[i-1])/2
                    maxIdx=self.s[i]
                                    
            if maxIdx==0 and self.s[0]!=0 or maxIdx==self.N-1 and self.s[-1]!=self.N-1:
                idx=maxIdx
            else:
                idx=(maxIdx+self.s[d[maxIdx]-1])/2
            i=0
            while i<len(self.s):
                if self.s[i]>idx:
                    break
                i+=1
            self.s.insert(i, idx)
            return idx
    
        def leave(self, p):
            """
            :type p: int
            :rtype: void
            """
            self.s.remove(p)
            
    
    
    # Your ExamRoom object will be instantiated and called as such:
    # obj = ExamRoom(N)
    # param_1 = obj.seat()
    # obj.leave(p)