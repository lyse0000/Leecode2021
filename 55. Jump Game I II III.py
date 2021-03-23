# 55. Jump Game I
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        IDX  0  1  2  3  4
            [2, 0, 1, 1, 4]
        m =  2
        m =     2 
        m =        3
        m =           4 <- return True
        """         
        
        max_location, N, i = nums[0], len(nums), 0
        
        while i<= max_location:
            max_location = max(max_location, i+nums[i])
            if max_location+1 >= N: 
                return True
            
            i += 1
            
        return False
