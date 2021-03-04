class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ret = []
        
        def dfs(nums, k, n, combin):
            if k == 0 and n == 0:
                ret.append(combin)
                return
            L = len(nums)
            if k<0 or n<0 or L<k or (L>0 and nums[0]*k>n): # 后面只可能比前面大 4*3>sum[4,6,7]
                return
            for i in range(L): 
                dfs(nums[i+1:], k-1, n-nums[i], combin+[nums[i]])

        dfs([i for i in range(1,10)],k,n,[])
        return ret
