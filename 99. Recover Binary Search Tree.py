# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        """
        In-order:

            1,2,3,4,5,6

            prev>=root
            1,[|5|,3],[4,|2|],6

            first not right we record [prev]
            second not right we record [root]
        """
        
        self.prev, self.firstWrong, self.secondWrong = TreeNode(float('-inf')), None, None
        self.inorder(root)
        self.firstWrong.val, self.secondWrong.val = self.secondWrong.val, self.firstWrong.val
        
    def inorder(self, node):
        if None == node: return 
        
        self.inorder(node.left)
        if self.prev.val>=node.val:
            if not self.firstWrong:
                self.firstWrong = self.prev
            # 有可能是连着的 1 2 [4 3] 5 6
            # 一直更新第二个node
            self.secondWrong = node

        self.prev = node
        self.inorder(node.right)
