class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        nums.sort()
        self.dfs(nums, [])
        return self.ret
        
    def dfs(self, nums, path):
        self.ret.append(path)
        for i, x in enumerate(nums):
            if i == 0 or nums[i]!=nums[i-1]:
                self.dfs(nums[i+1:], path+[x])
                
        """
        1,2,2,3
        
        for
        -[1] (2,2,3) 
            [1,2](2,3), skip, [1,3]()
                [1,2,2](3), [1,2,3]() 
                    [1,2,2,3]
                
        -[2] (2,3)
            [2,2](3), [2,3]()
                [2,2,3]
        -skip since nums[i] == nums[i-1] skip
        
        -[3] ()
        """      
