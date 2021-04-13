class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i]==ret:
                count+=1
            elif nums[i]!=ret:
                if count>0:
                    count-=1
                else:
                    ret = nums[i]
                    count = 1
        return ret
