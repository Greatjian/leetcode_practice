# 170. Two Sum III - Data structure design

Design and implement a TwoSum class. It should support the following operations: add and find.

- add - Add the number to an internal data structure.
- find - Find if there exists any pair of numbers which sum is equal to the value.

For example,

    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false
    
## Method:

Trade-off between these two functions, should ask the interviewer first:

O(n) add, O(1) find, tle:

    class TwoSum(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.num=[]
            self.s=set()
    
        def add(self, number):
            """
            Add the number to an internal data structure..
            :type number: int
            :rtype: void
            """
            for i in self.num:
                self.s.add(i+number)
            self.num.append(number)
    
        def find(self, value):
            """
            Find if there exists any pair of numbers which sum is equal to the value.
            :type value: int
            :rtype: bool
            """
            return value in self.s
    
    
    # Your TwoSum object will be instantiated and called as such:
    # obj = TwoSum()
    # obj.add(number)
    # param_2 = obj.find(value)
    
O(1) add, O(n) find, pass:    
    
    class TwoSum(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.d=collections.defaultdict(int)
    
        def add(self, number):
            """
            Add the number to an internal data structure..
            :type number: int
            :rtype: void
            """
            self.d[number]+=1
    
        def find(self, value):
            """
            Find if there exists any pair of numbers which sum is equal to the value.
            :type value: int
            :rtype: bool
            """
            for i in self.d.keys():
                j=value-i
                if j in self.d and (i==j and self.d[i]>1 or i!=j):
                    return True
            return False
    
    # Your TwoSum object will be instantiated and called as such:
    # obj = TwoSum()
    # obj.add(number)
    # param_2 = obj.find(value)