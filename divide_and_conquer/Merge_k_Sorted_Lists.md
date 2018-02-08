# 023. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

## Method:

O(nlogk):

divide and conquer:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def mergeKLists(self, lists):
            """
            :type lists: List[ListNode]
            :rtype: ListNode
            """
            if not lists:
                return []
            if len(lists)==1:
                return lists[0]
            res=[]
            for i in range(len(lists)/2):
                res.append(self.merge2(lists[2*i], lists[2*i+1]))
            if len(lists)%2:
                res.append(lists[-1])
            return self.mergeKLists(res)
            
        def merge2(self, l1, l2):
            dummy=ListNode(0)
            h=dummy
            while l1 and l2:
                if l1.val<l2.val:
                    h.next=l1
                    l1=l1.next
                else:
                    h.next=l2
                    l2=l2.next
                h=h.next
            if l1:
                h.next=l1
            else:
                h.next=l2
            return dummy.next
            
using heap:

    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    
    class Solution(object):
        def mergeKLists(self, lists):
            """
            :type lists: List[ListNode]
            :rtype: ListNode
            """
            hp=[]
            dummy=ListNode(0)
            head=dummy
            for l in lists:
                if l:
                    heapq.heappush(hp, (l.val, l))
            while hp:
                val, node=heapq.heappop(hp)
                head.next=node
                head=head.next
                if node.next:
                    heapq.heappush(hp, (node.next.val, node.next))
            return dummy.next