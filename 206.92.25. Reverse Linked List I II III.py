# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        """
          p h 
            1 2 3 4 5
            
            p h
            1 2 3 4 5   
            
            p   h
            2 1 3 4 5   
            
            p     h
            3 2 1 4 5   
            
            p       h
            4 3 2 1 5   
            
            p         h
            5 4 3 2 1    
        """
        prev = None
        
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        
        return prev

# ================================================================================================
# 92. Reverse Linked List II
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


# ================================================================================================
# 25. Reverse Nodes in k-Group
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        check, count = head, 0
        while check and count<k:
            check = check.next
            count+=1
        
        if count<k: return head
        
        newHead, tail = self.reverse(head, count)
        tail.next = self.reverseKGroup(check, k)
        return newHead
        
    
    def reverse(self, head, count):
        prev, tail = None, head
        
        for i in range(count):
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        
        return (prev, tail)
            
        
