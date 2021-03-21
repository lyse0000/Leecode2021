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

      
# =========================================================================================              
# 515. Find Largest Value in Each Tree Row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        level, ret = [root] if root else [], []
        
        while level:
            nextlevel, _max = [], float('-inf')
            for n in level:
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
                _max = max(n.val, _max)
            level = nextlevel
            ret.append(_max)
            
        return ret



# =========================================================================================              
# 513. Find Bottom Left Tree Value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue, ret = [root] if root else [], root
        while queue:
            nextqueue = []
            ret = queue[0].val
            for n in queue:
                if n.left: nextqueue.append(n.left)
                if n.right: nextqueue.append(n.right)
            queue = nextqueue
        return ret


# =========================================================================================    
# 429. N-ary Tree Level Order Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret, q = [], [root] if root else []
        
        while q:
            nextq = []
            for n in q:
                for c in n.children:
                    nextq.append(c)
            ret.append([n.val for n in q])
            q = nextq
            
        return ret
        
