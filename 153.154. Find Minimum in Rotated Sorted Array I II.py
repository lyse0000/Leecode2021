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
