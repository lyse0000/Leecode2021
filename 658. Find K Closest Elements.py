class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        # edge caese
        if arr[0] >= x:
            return arr[0:k]
        if arr[n-1] <= x:
            return arr[n-k:]
        
        # binary search on the i such that i ~ i+k is the ans
        
        """
                x - arr[mid] < arr[mid+k] - x
                right = mid - 1 
        ---x----[mid]--------[mid+k]----
        --------[mid]-x------[mid+k]----
        
        
                x - arr[mid] > arr[mid+k] - x
                left = mid + 1
        --------[mid]------x-[mid+k]----
        --------[mid]--------[mid+k]-x--
        
        [0,0,1,2,3,3,4,7,7,8]
        3
        5
        
        """
        
        left, right, mid = 0, n-k, 0
        
        while left < right:
            mid = left + (right - left)//2
            if  x - arr[mid] > arr[mid+k] - x:
                left = mid + 1 
            else: # x - arr[mid] >= arr[mid+k] - x:
                right = mid 
            
        return arr[left:left+k]
