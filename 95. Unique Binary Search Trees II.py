# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.helper([i for i in range(1,n+1)])
        
    def helper(self, nodes) -> List[TreeNode]:
        if len(nodes) == 0:
            return [None]
        # for i [0:i-1]<-split->[i+1:-1] 每一个node给他一个当root的机会
        ret = []
        for i, x in enumerate(nodes):
            left = self.helper(nodes[:i])
            right = self.helper(nodes[i+1:])
            for l in left:
                for r in right:
                    root, root.left, root.right = TreeNode(x), l, r   
                    ret+=[root]
        return ret
