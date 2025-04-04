# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""    
U:
    - We are needing to remove the node which is nth from the END
Edge Cases:
    - Empty list? We will not have an empty list
    - List length 1? We will remove that node and return an empty list

Match: Linked List
    - We can do a double pass to find the length of the list

Plan:
    - We will do a pass through to get the length of the list
    - We can find what the index from the start is based on the length
    - Then we can traverse back to that point, and remove the node

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
head = [1,2,3,4,5]
curr = [1,2,3,4,5]
length = 5
pos from front = 5 - 2 = 3 (0 indexed)


"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head = head.next
            return head
        
        curr = head
        len_ = 0
    
        while curr:
            len_ += 1
            curr = curr.next
       
        pos = len_ - n
        if pos == 0:
            head = head.next
            return head
        
        curr = head
        for i in range(pos - 1):
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
            
        return head
