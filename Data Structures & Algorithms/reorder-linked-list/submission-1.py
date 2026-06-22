class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        reordered = []
        left = 0
        right = len(nodes) - 1

        while left <=right:
            if left == right:
                reordered.append(nodes[left])
            else:
                reordered.append(nodes[left])
                reordered.append(nodes[right])

            left +=1
            right -=1 
        
        for idx in range( len(nodes) - 1):
            reordered[idx].next = reordered[idx+1]
        
        reordered[-1].next = None

