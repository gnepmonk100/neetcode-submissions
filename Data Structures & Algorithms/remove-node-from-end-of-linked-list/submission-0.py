# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        num_nodes = len(nodes)
        nodes.pop( num_nodes - n )

        if not nodes:
            return None

        for idx in range( len(nodes) - 1):
            nodes[idx].next = nodes[idx+1]
        
        nodes[-1].next = None

        return nodes[0]


        