class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        ans = 0
        _sum = 0
        for i in range(len(nums)):
            _sum+=nums[i]
            precount = dic.get(_sum%k, 0)
            ans+=precount
            dic[_sum%k] = precount + 1
        return ans
