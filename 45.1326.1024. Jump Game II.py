# 1024. Video Stitching
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        hq = sorted([(i-r, i+r) for i, r in enumerate(ranges) if r>0])
        start, end, ret = 0, 0, 1
        
        for r in hq:
            if r[0] > start:
                if end<r[0]:
                    return -1
                ret+=1
                start = end
            end = max(end, r[1])
            if end >= n:  
                return ret
            
        return ret if n<=end else -1

# ============================================================================================================
# 1024. Video Stitching
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T<1: 
            return 0
        clips = sorted(clips)
        start, end, ret = 0, 0, 1
        
        for c in clips:
            if c[0]>start:
                if end < c[0]:
                    return -1
                ret += 1
                start = end
                
            end = max(end, c[1])
            if end >= T:
                return ret
        return -1 if end<T else ret

# ============================================================================================================
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
        
        if len(nums)<2:
            return 0

        curr, _next, ret = nums[0], 0, 1
        
        for i in range(1, len(nums)):
            if (curr>=len(nums)-1):
                return ret
            
            while(i<=curr):
                _next = max(_next, i+nums[i])
                i+=1
            
            ret+=1
            curr = _next
        
        return ret 
