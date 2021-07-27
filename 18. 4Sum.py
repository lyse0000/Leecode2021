class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # -3 0 1 1 1 1 1 2 4 5 5 6 7 8
        
        def findNsum(N, l, r, innerT, prev, ans):
            # early determination
            if r-l+1 < N or N<2 or nums[l]*N>innerT or nums[r]*N<innerT:
                return
            
            if N == 2: # solve 2 sum
                while l < r:
                    s = nums[l] + nums[r]
                    
                    if s == innerT:
                        # find inner Targrt
                        ans.append(prev + [nums[l], nums[r]])
                        l += 1
                        # skip duplications
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        
                    elif s < innerT:
                        l+=1
                    elif s > innerT:
                        r-=1
            else: # N>2
                # nextIdx == l 第一个总是加上去 1 1 1 1
                findNsum(N-1, l+1, r, innerT-nums[l], prev+[nums[l]], ans)
                for nextIdx in range(l+1, r+1):
                    if nums[nextIdx] != nums[nextIdx-1]: # skip duplication in the loop
                        findNsum(N-1, nextIdx+1, r, innerT-nums[nextIdx], prev+[nums[nextIdx]], ans)
        
        
        nums.sort()
        ans = []
        findNsum(4, 0, len(nums)-1, target-0, [], ans)
        return ans
