#198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
                    skip = [max(skip[i-1],take[i-1])]
                    take = curr+skip[i-1]
                    
                6       1       2       7
        skip    [0]     [6,0]   [1,6]   [6,8]
        take    [6]     [1+(0)] [2+6]   [7+6]  <---ret =7+6
        --------------------------------------------
                6       1       1       1       7
        skip    [0]     [0,6]   [6,1]   [6,7]   [7,7]
        take    [6]     [1+0]   [1+6]   [1+6]   [7+7]   <---ret =14
        
        
        """
        
        N = len(nums)
        skip, take = 0, nums[0]
        
        for i in range(1,N):
            s, t = skip, take
            skip = max(s, t)
            take = nums[i]+s
            
        return max(skip, take)


    

# ================================================================== Another Q ===========
# 213. House Robber II    
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        """
                    skip = [max(skip[i-1],take[i-1])]
                    take = currnum+skip[i-1]
                    
                6       1       2       7
        skip    [0]     [6,0]   [1,6]   [6,8]  <-----[ok] 8 is ok
        take    [6]     [1+(0)] [2+6]   [7+6]  <-----[Invalid] 7+6
        
        skip0   [0]     [0,0]   [0,1]   [1,2]  <---- [ok] 2
        take0   [0]     [0+1]   [0+2]   [7+1]  <-----[ok] 8 ok too
                                                ___________________
                                                so ret = max(8,8,2) = 8
                                                    
        {same thing just one more initialization}
        --------------------------------------------
                6       1       1       1       7
        skip    [0]     [0,6]   [6,1]   [6,7]   [7,7]
        take    [6]     [1+0]   [1+6]   [1+6]   [7+7]   
        skip0   ....
        take0   ....
        
        """
        
        N = len(nums)
        
        skip, take, skip0, take0 = 0, nums[0] if len(nums)>0 else 0, 0, 0
        
        for i in range(1, N):
            s, t, s0, t0 = skip, take, skip0, take0
            skip = max(s, t)
            take = nums[i]+s
            skip0 = max(s0, t0)
            take0 = nums[i]+s0
        
        return max(skip0, take0, skip) if N>1 else take    




# ================================================================== Another Q ===========
# 337. House Robber III
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        
        def helper(node):
            if not node: return (0,0)
            
            takeL, skipL = helper(node.left)
            takeR, skipR = helper(node.right)
            
            return (node.val+skipL+skipR, max(skipL,takeL)+max(skipR,takeR))
        
        take, skip = helper(root)
        return max(take, skip)
