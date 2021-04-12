class Solution:
    
    """
    [1,2,3]
    [1,3,6] _> (0) (1,2), (3,4,5)
    weight重他的length'就越长
    
    """

    def __init__(self, w: List[int]):
        for i in range(1,len(w)):
            w[i]+=w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        n = random.randint(0,self.w[-1]-1)
        lo, hi = 0, len(self.w)-1
        while lo<hi:
            m = (lo+hi)//2
            if n >= self.w[m]:
                lo = m+1
            else:
                hi = m
        return lo
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
