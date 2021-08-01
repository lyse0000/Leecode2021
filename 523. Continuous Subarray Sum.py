class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        1 2 3 4 5
        sum[1 2 3 4 5] - sum[1 2 3] = %k - %k => 0
        
        """
        
        reminders = {0:-1}
        prev = 0
        for i in range(len(nums)):
            prev += nums[i]
            if nums[i] != 0 and prev%k in reminders and i - reminders[prev % k]>1:
                return True
            if i>0 and nums[i]==0 and nums[i-1]==0:
                return True
            if prev%k not in reminders:
                reminders[prev%k] = i
        return False
        
