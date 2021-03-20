# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 0 = not taken care of
        # 1 = taken care of
        # 2 = camera
        def dfs(node):
            if not node:
                return 1
            
            l, r = dfs(node.left), dfs(node.right)
            
            if l==0 or r==0:
                self.ret+=1
                return 2
            elif l==2 or r==2:
                return 1
            else: return 0
        
        self.ret = 0
        if dfs(root)==0:
            self.ret+=1
        return self.ret
