# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def helper(node, _sum):
            if not node:
                return False
            if not node.left and not node.right:
                return node.val+_sum == targetSum
            return helper(node.left, node.val+_sum) or helper(node.right, node.val+_sum)
        
        return helper(root, 0)

    
# 113
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        ret = []
        def helper(node, _sum, prev):
            if not node:
                return 
            prev.append(node.val)
            if not node.right and not node.left:
                if node.val+_sum == targetSum:
                    ret.append(prev)
                    return
            
            helper(node.left, node.val+_sum, list(prev))
            helper(node.right, node.val+_sum, list(prev))
            
        helper(root, 0, [])
        return ret

# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
