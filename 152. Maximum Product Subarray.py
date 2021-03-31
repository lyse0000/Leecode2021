
# 152. Maximum Product Subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _min, _max = nums[0], nums[0]
        ret = nums[0]
        
        for i in range(1, len(nums)):
            prev_min, prev_max = _min, _max
            _min = min(prev_min*nums[i], prev_max*nums[i], nums[i])
            _max = max(prev_min*nums[i], prev_max*nums[i], nums[i])
            ret = max(_max, ret)
        return ret
        
