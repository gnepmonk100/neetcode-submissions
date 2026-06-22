# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        values = []
        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        values.reverse()
        new_head = ListNode(values[0])
        current_new = new_head

        for val in values[1:]:
            current_new.next = ListNode(val)
            current_new = current_new.next
        return new_head



        
       

    