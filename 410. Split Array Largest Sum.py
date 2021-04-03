class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 这题binary的解法太经典 太难想了，而且为什么greedy是ok的？   
        # 花花讲解： https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-410-split-array-largest-sum/
        # Binary Search 
        """
        已知 lower bound = max(nums) <-分成N组
            upper bound = sum(nums) <-分成一组
            C = mind(upper, lower)
        """
        def calculateGroups(_max):
            _sum, groups = 0, 1
            for n in nums:
                if _sum+n > _max:
                    _sum = n
                    groups+=1
                else:
                    _sum+=n
            return groups
        
        L, R = max(nums), sum(nums)
        while(L < R):
            mid = (R-L)//2+L
            count = calculateGroups(mid)
            if count <= m:
                R = mid
            else:
                L = mid+1
            
        return L
        
        
        
    # ----------------------------------------------------------------------------------------------------
    # Sol 2: TML DP Soution(not passed)

    def splitArray(self, nums: List[int], m: int) -> int:
        N = len(nums)
        if N<=m: return max(nums)
        
        dp = [[float('inf')]*N for _ in range(m)]
        
        for i in range(N):
            dp[0][i] = nums[0] if i==0 else nums[i]+dp[0][i-1]
        
        print(dp)
        
        for mi in range(1, m):
            for i in range(mi, N):
                for j in range(mi-1, i):
                    value = max( dp[mi-1][j] , sum(nums[j+1:i+1]) )
                    dp[mi][i] = min(dp[mi][i], value)
        return dp[m-1][N-1]
