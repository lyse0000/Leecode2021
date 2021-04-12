# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = self.isCycle(head)
        if not fast:
            return None
        while head!=fast:
            head = head.next
            fast = fast.next
        return head
        
    
    def isCycle(self, head):
        p, q = head, head
        while p and q:
            if p==None or q==None or q.next==None:
                return None
            p=p.next
            q=q.next.next
            if p == q:
                return q
        return None
