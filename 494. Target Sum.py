class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # https://leetcode.com/problems/target-sum/discuss/97439/JavaPython-Easily-Understood
        
        count = collections.Counter({0:1})  
        
        for x in nums:
            temp = collections.Counter()
            for _sum in count:
                temp[_sum+x] += count[_sum]
                temp[_sum-x] += count[_sum]
            count = temp
            
        return count[S]
