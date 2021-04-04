class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        test = [2,3,4,5,5,6,7,12,14,15]
            #   0 1 2 3 4 5 6 7  8  9
        x = 4
        print(x,"---",bisect.bisect(test,x))
        print(x+1,"---",bisect.bisect(test,x+1))
        print(x+1,"---",bisect.bisect(test,x+1)-1)
        
        !!! biset 是TM一个一个元素比的 [1,2,3] 先比1 再比2 再比3
        我的天神坑

        """
                                       
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            # -1 是因为不是真的insert，只取最后一个
            # 反正就是找能符合的LAST一个
            i = bisect.bisect(dp, [s, float('inf')]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
        
        
        
        """   
    # DP n**2 solution with TLE (NO pass)
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v:v[1])
        n = len(jobs)
        dp = [j[2] for j in jobs] 
        
        for i in range(1, n):
            for j in range(i):
                if jobs[j][1]<=jobs[i][0]: # job j ends >= i starts
                    dp[i] = max(dp[i], dp[j]+jobs[i][2])
        print(dp)
        return max(dp)
    """
                
              
            
