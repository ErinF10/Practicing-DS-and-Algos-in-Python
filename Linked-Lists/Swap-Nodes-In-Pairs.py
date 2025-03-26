"""
U:
- We are swapping nodes in pairs of 2, if a node ever does not have a pair at the end, just leave it be
- The linked list is relatively short so we don't have to be insanely time/space conscious but O(1) space and O(n) time if possible

Edge cases:
- Empty list: return an empty list
- Odd number of nodes: Leave the last node be
- Nodes have the same value: Still must be swapped (nodes are swapping not values)

M: Linked List
- Temp heads (maybe)
- Double pass (x)
- Slow and fast

P: Temp Head

Head = 2 -> 1 -> 4 -> 3 -> 5
Temp = 1 -> 3 -> 5
Curr: 3
Temp curr: 3

create temp list
Check if curr.next
Set head = head.next

while curr.next:
    set temp curr.next = temp curr.next.next
    Set curr.next to temp curr
    set temp curr = temp curr.next 
    set curr = curr.next
    if not curr.next or curr.next.next:
        break
    set curr.next = curr.next.next
    set curr = curr.next

"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = head
        if not head or not head.next:
            return head
        head = head.next
        curr = head
        temp_curr = temp_head

        while curr:
            temp_curr.next = temp_curr.next.next
            curr.next = temp_curr
            temp_curr = temp_curr.next 
            curr = curr.next
            if not curr.next or not curr.next.next:
                curr.next = temp_curr
                return head
            curr.next = curr.next.next
            curr = curr.next
        return head    
    
    
