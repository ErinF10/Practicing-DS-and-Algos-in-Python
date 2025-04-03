# https://leetcode.com/problems/merge-in-between-linked-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Common Approaches: Linked List
- Two pointer (couild be used here)
- double pass

Plan:
- we can use the 2 pointer method, first to point where list2 should be inserted, 1 where it should end
- p1 goes to a - 1, p2 goes to b + 1
- use a temp node to traverse to the end of list2, and make the endnode.next = p2
- then make p1.next equal to list2.head
           v
list1 = [0,1,2,3,4,5,6] , a = 2, b = 5, 
                     ^
list2 = [1000000,1000001,1000002,1000003,1000004]


"""
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p1 = list1
        for _ in range(a - 1):
            p1 = p1.next
        p2 = p1
        for _ in range(a - 1, b + 1):
            p2 = p2.next
        temp = list2
        while temp.next:
            temp = temp.next
        temp.next = p2
        p1.next = list2
        return list1        
