class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        p, q = nums[0], nums[0]
        
        while(p):
            p = nums[p]
            q = nums[nums[q]]
            
            if p == q:
                break
                
        p = nums[0]
        
        while p!=q:
            p = nums[p]
            q = nums[q]
            
        return q
