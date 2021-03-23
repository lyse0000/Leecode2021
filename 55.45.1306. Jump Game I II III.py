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


# ========================================================================================
# 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
                IDX  0  1  2  3  4
                    [2, 0, 1, 1, 4]
        step 0      [2]                 m = 2
        step 1         [0, 1]           m = 3
        step 2               [3]        m = 4 <- return step 2
        
        """         
        
        m, next_m, N, step = nums[0], nums[0], len(nums), 1
        
        for i in range(1,N):
            if m+1>=N: return step
            while i <= min(m, N):
                next_m = max(next_m, i+nums[i])
                i+=1
            
            m = next_m
            step+=1
                
        return N if N>2 else 0



# ========================================================================================
# 1306. Jump Game III
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited, N = set(), len(arr)
        
        def dfs(i):
            if 0<=i<N and not i in visited:
                if arr[i] == 0:  return True
                visited.add(i)
                return dfs(i-arr[i]) or dfs(i+arr[i])
            return False
        
        return dfs(start)
