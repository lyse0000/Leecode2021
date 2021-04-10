class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """
        第一种 nums[m] > nums[hi]: min 一定在 [m+1, hi]
        第二种 nums[lo] > nums[mi]: min 一定在 [lo+1, mi]
        第三种 nums[lo] <= nums[m] <= nums[hi]: min  == nums[lo]

        """
        lo, hi = 0, len(nums)-1
        
        while lo < hi:                # 1222 2 2234 
            m = (lo+hi)//2
            if nums[m] > nums[hi]:    # 2222 3 4122
                lo = m + 1
            elif nums[lo] > nums[m]:  # 3441 2 2222
                hi = m 
                lo += 1
            elif nums[lo]<=nums[m]<=nums[hi]:   # 也有可能是 2222 2 3412
                # lo+=1 就会错 eg. 22334
                hi-=1 
            
        
        return nums[lo]

# Method 2
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Method 1
        N = len(nums)
        
        lo, hi, mid = 0, N-1, (N-1)//2
        
        if nums[lo] < nums[hi]:
            # is sorted
            return nums[lo]
        else:
            mid = (lo+hi)//2
            return min(self.findMin(nums[lo:mid+1]), self.findMin(nums[mid+1:hi+1]))



# =================================================================================================================
# 81. Search in Rotated Sorted Array II
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        lo, hi = 0, len(nums)-1
        
        # 0018800
        # 0000230
        # 0120000
        # 8900123
        # 如果lo跟m一样，lo就往前走走到不一样
        
        
        while lo<hi:
            m = (lo+hi)//2
            
            if nums[m] == target:
                return True
            
            while lo<m and nums[lo] == nums[m]:
                lo+=1
            while hi>m and nums[hi] == nums[m]:
                hi-=1
                
            if nums[lo]<=nums[m]: #[lo:m] sorted or lo==m -> case [3,1]
                if nums[lo]<=target<nums[m]: # in the range
                    hi = m-1
                else: # not in the range, this delete this range
                    lo = m+1
                    
            elif nums[m]<nums[hi]: #[m:hi] sorted
                if nums[m]<target<=nums[hi]:
                    lo = m+1
                else:
                    hi = m-1
                print(lo,hi)
                
            else: #nums[m] == nums[lo] or nums[m] == nums[hi] 
                continue
        return nums[lo]==target
    

# ================================================================================================================= 
# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums)-1
        
        while lo<hi:
            m = (lo+hi)//2
            if nums[m] == target:
                return m
            if nums[lo]<=nums[m]: # 因为lo很有可能是 m 想到[3,1]
                if nums[lo]<=target<nums[m]:
                    hi = m-1
                else:
                    lo = m+1
            else:
                if nums[m]<target<=nums[hi]:
                    lo = m+1
                
                else:
                    hi = m-1
        
        return lo if nums[lo]==target else -1
