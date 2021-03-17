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
