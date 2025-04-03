# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
U:
Can we have a null linked list passed in? Yes
Can there be any cycles in the list?

Edge cases:
- Null list
- Cycles in the linked list

M: Linked List
Temp head method, Two-pointers, double pass through?
- Two-pointer method
    - One pointer at a zero while the other moves forward until it
    reaches a second zero, then the first pointer will move forward and
    add them up
Will making a new list help?
- We can do this in place, but it will be more complex.

P:
#                                   p1
# 0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0
#                                   p2

if head is None:
    return head
p1 = head
p2 = head
#mergedList = copy.deepcopy(head)
mergedList = head
sum = 0
while p2.next:
    p2 = p2.next
    while p2.val != 0:
        p2 = p2.next
    while p1 != p2:
        sum += p1.val
        p1 = p1.next
    mergedList.val = sum
    mergedList = mergedList.next
    sum = 0

How to delete a node?

+= the value of p1 with p1.next, then set p1.next to p1.next.next
    



"""
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        p1 = head
        p2 = head
   
        while p2.next:
            p2 = p2.next
            while p2.val != 0:
                p2 = p2.next
            while p1.next != p2:
                p1.val += p1.next.val
                p1.next = p1.next.next
            if p2.next:
                p1 = p1.next
     
        p1.next = p1.next.next
        return head

"""
   p2           
[4,0,4,5,2,0]
p1
"""
