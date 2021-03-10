class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.right and not root.left):
            return root
        
        right = self.flatten(root.right)
        left = self.flatten(root.left)
        
        if left:
            while left.right:
                left = left.right
            left.right = right
            root.right = root.left
            root.left = None
        
        return root


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nodeList = []
        
        while head:
            nodeList.append(head)
            head = head.next
            
        def buildTree(L):
            if len(L)<1:
                return None
            mid = len(L)//2
            root = TreeNode(L[mid].val)
            root.left = buildTree(L[:mid])
            root.right = buildTree(L[mid+1:])
            return root
            
        head = buildTree(nodeList)
        return head
