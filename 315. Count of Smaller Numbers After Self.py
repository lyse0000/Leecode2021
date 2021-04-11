class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        ret = [0]
        arr = [nums[-1]]
        
        for i in range(len(nums)-2, -1, -1):
            idx = self.binarysearch(arr, nums[i])
            ret.append(idx)
            arr.insert(idx, nums[i])
            
        return ret[::-1]
            
        
    def binarysearch(self, arr, n):
        lo, hi = 0, len(arr)
        
        while lo<hi: 
            if arr[lo]>=n: return lo
            m = (lo+hi)//2
            if arr[m]>=n and (m == 0 or arr[m-1]<n):
                return m
            if arr[m]<n: # all idx left need to be stricktly smaller than n
                lo=m+1
            else: # arr[m]>=n 
                hi=m
                
        return lo
