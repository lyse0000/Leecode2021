# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if len(inorder) == 0:
            return None
        
        root = TreeNode(postorder.pop())
        i = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:])
        
        return root
