# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # fast
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        dic, ret = collections.defaultdict(list), []
        
        def level_dfs(node):
            if not node:
                return -1
            right = level_dfs(node.right)
            left = level_dfs(node.left)
            level = 1+max(right,left)
            dic[level].append(node.val)
            return level
        
        level_dfs(root)
        for level in dic:
            ret.append(dic[level])
        return ret          
    
        
    # slow
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        q = set()
        ret = []
        
        def dfs(node):
            if not node:
                return
            q.add(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        
        while q:
            cq = q.copy()
            for i in q:
                if i.left not in q and i.right not in q:
                    cq.remove(i)
            ret.append([x.val for x in (q-cq)])
            q = cq
        return ret

