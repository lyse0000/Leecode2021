# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        stack = []
        dummy = ListNode(-1, head)
        start = dummy
        
        for i in range(1, right+1):
            if i < left: 
                start = start.next
            else:
                stack.append(head)            
            head = head.next
        # end = head
        
        while stack:
            node = stack.pop()
            start.next = node
            start = node
        
        start.next = head
        
        return dummy.next
