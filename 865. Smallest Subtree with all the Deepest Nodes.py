# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/discuss/146808/C%2B%2BJavaPython-One-Pass
        
        # return (depth, depth_subtree)
        def dfs(node):
            if node == None:
                return (0, None)
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)
            
            if left_depth == right_depth:
                return (left_depth+1, node)
            elif left_depth > right_depth:
                return (left_depth+1, left_subtree)
            else:
                return (right_depth+1, right_subtree)
            
        return dfs(root)[1]
