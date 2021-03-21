# 1161. Maximum Level Sum of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root] if root else []
        ret, level, _max = 0, 0, float('-inf')
        
        while queue:
            levelsum, nextqueue = 0, []
            level+=1
            for n in queue:
                if n.left: nextqueue.append(n.left)
                if n.right: nextqueue.append(n.right)
                levelsum+=n.val
            if levelsum>_max:
                _max = levelsum
                ret = level
            queue = nextqueue
        return ret
      
      
# =========================================================================================         
# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        ret, queue = [], [root] if root else []
        reverse = False
        
        while queue:
            nextqueue = []
            for node in queue:
                if node.left: 
                    nextqueue.append(node.left)
                if node.right: 
                    nextqueue.append(node.right)
            if reverse:
                queue.reverse()
            ret.append([n.val for n in queue])
            queue = nextqueue
            reverse = not reverse
        return ret
        
