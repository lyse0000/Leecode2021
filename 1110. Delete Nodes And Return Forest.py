# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Very Good explanation:
    https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328854/Python-Recursion-with-explanation-Question-seen-in-a-2016-interview
    """
    
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        deleteset = set(to_delete)
        ret = []
        
        def backTrack(node, parentIsDeleted):
            if not node: return None
            
            # append to ret when this node is not in deletd and its parent is deletd
            thisIsToBeDleted = node.val in deleteset
            
            if parentIsDeleted and not thisIsToBeDleted:
                ret.append(node)
                
            node.left = backTrack(node.left, thisIsToBeDleted)
            node.right = backTrack(node.right, thisIsToBeDleted)
            
            return None if thisIsToBeDleted else node
          
        root = backTrack(root, True)
        return ret
