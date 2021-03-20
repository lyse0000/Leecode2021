# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        # If a node has val = 0. It means it need 1 move
        # So abs(1-val) will be the move needed for that child, at root's position
        
        self.ret = 0
        def bfs(node):
            if not node:
                return 0
            l_balance, r_balance = bfs(node.left), bfs(node.right)
            
            balance = (node.val-1) + l_balance + r_balance

            self.ret+= abs(l_balance) + abs(r_balance)
            
            return balance
        bfs(root)
        return self.ret
