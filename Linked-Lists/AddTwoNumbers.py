# Leetcode Problem #2. Add Two Numbers (https://leetcode.com/problems/add-two-numbers/description/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
243
564

 342 carry: 1
+465
 807

   342 carry: 
+54465
   807
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = ListNode()
        head = sum_list
        carry = 0
        while l1 or l2 or carry == 1:
            if l1:
                digit1 = l1.val
                l1 = l1.next
            else:
                digit1 = 0
            if l2:
                digit2 = l2.val
                l2 = l2.next
            else:
                digit2 = 0
            digitSum = digit1 + digit2 + carry
            carry = digitSum // 10
            digitSum %= 10

            sum_list.val = digitSum
            if l1 or l2 or carry == 1:
                sum_list.next = ListNode()
                sum_list = sum_list.next
            
          
        return head


        
