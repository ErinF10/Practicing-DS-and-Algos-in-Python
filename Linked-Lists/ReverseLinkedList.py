# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Use two pointers: prev (starts as null) and curr (starts at head).
At each step:
1 . Store curr.next in temp.
2 . Reverse curr.next to point to prev.
3 . Move prev to curr and curr to temp.
Repeat until curr is null.

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
