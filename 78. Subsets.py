class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.dfs(nums, [])
        return self.ret
        
    def dfs(self, nums, path):
        self.ret.append(path)
        for i, x in enumerate(nums):
            self.dfs(nums[i+1:], path+[x])78. Subsets
