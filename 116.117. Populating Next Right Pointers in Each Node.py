"""
116. Populating Next Right Pointers in Each Node
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
        

    def connect(self, root: 'Node') -> 'Node':
        q = [root,]
        dummy, dummy.next = Node(0), root
        
        while q:
            n = len(q)
            for i in range(n):
                x = q.pop(0)
                if x:
                    x.next = q[0] if i<n-1 else None
                    q.append(x.left)
                    q.append(x.right)
        return dummy.next
      
      
"""
117. Populating Next Right Pointers in Each Node II
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        q = [root,]
        dummy, dummy.next = Node(0), root
        
        while q:
            n = len(q)
            for i in range(n):
                x = q.pop(0)
                x.next = q[0] if i<n-1 else None
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return dummy.next
