class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        while zero<len(nums) and nums[zero]!=0:
            zero+=1
            
        for i in range(zero+1, len(nums)):
            if nums[i] != 0:
                # move forward 
                nums[zero], nums[i] = nums[i], nums[zero]
                zero+=1
