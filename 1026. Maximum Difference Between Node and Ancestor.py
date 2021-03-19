# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ret = 0
        
        def helper(node):
            if not node: return 
            if not node.left and not node.right:
                return (node.val, node.val)
            
            val, _min, _max = node.val, node.val, node.val
            left, right = helper(node.left), helper(node.right)
            if left:
                _min, _max = min(_min, left[0]), max(_max, left[1])
            if right:
                _min, _max = min(_min, right[0]), max(_max, right[1])  
            self.ret = max(self.ret, abs(val-_min), abs(val-_max))
            return _min, _max
        
        helper(root)
        return self.ret
