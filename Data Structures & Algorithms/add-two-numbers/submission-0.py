# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodes_l1 = []
        nodes_l2 = []
        num1 = 0
        num2 = 0

        curr1 = l1
        curr2 = l2

        while curr1:
            nodes_l1.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            nodes_l2.append(curr2.val)
            curr2 = curr2.next
        
        for idx in range( len(nodes_l1) ):
            num1 += nodes_l1[idx] * (10 ** idx)

        for idx in range( len(nodes_l2) ):
            num2 += nodes_l2[idx] * (10 ** idx)
        
        two_sum = num1 + num2

        sum_digits = []
        
        while two_sum > 0:
            digit = two_sum % 10
            sum_digits.append(ListNode(digit))
            two_sum = two_sum//10
        
        for idx in range( len(sum_digits) - 1):
            sum_digits[idx].next = sum_digits[idx+1]
        
        sum_digits[-1].next = None

        return sum_digits[0]


        