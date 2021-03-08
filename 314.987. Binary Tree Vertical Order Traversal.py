# 314. Binary Tree Vertical Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return
        G, q = collections.defaultdict(list), [(root, 0)]
        
        while q:
            node, l = q.pop(0)
            G[l].append(node.val)
            if node.left:
                q.append((node.left, l-1))
            if node.right:
                q.append((node.right, l+1))
                
        return [G[i] for i in sorted(G)]
      
      
# 987. Vertical Order Traversal of a Binary Tree      
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        levelmap = collections.defaultdict(list)
        
        q = [(root, 0)]
        
        while q:
            tempq, tempmap = [], collections.defaultdict(list)
            
            for i in range(len(q)):
                node, l = q.pop(0)
                tempmap[l].append(node.val)
                if node.left:
                    tempq.append((node.left, l-1))
                if node.right:
                    tempq.append((node.right, l+1))
            q+=tempq
            for i in tempmap:
                levelmap[i]+=(sorted(tempmap[i]))
            
        return [levelmap[i] for i in sorted(levelmap)]
