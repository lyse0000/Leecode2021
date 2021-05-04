class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        """
        # Paitient sort 
        https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
        
        tails = [-inf]*len(nums)
        
        (1) if x is larger than all tails, append x and increase ret+1
        (2) if tails[i]< x <= tails[i+1], updtae tails[i+1]
        """
        
        
        tails = [float(inf)] * len(nums)
        end = 0
        
        for x in nums:
            i, j = 0, end
            while i < j:
                m = (i+j)//2
                if tails[m]<x:
                    i = m+1
                else:
                    j = m
                    
            tails[i] = x
            end = max(end, i+1)
        return end
