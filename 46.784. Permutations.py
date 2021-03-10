class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        ret = []
        
        for i in range(len(nums)):
            others = nums[0:i]+nums[i+1:]
            other_permutation = self.permute(others)
            for p in other_permutation:
                ret.append([nums[i]]+p)
        return ret


#784. Letter Case Permutation
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ret = []
        def bfs(s, path):
            if len(s)<1 or s.isnumeric():
                ret.append(path+s)
                return
            for i, x in enumerate(s):
                if x.isalpha():
                    bfs(s[i+1:], path+s[:i]+x.lower())
                    bfs(s[i+1:], path+s[:i]+x.upper())
                    break
        bfs(S, "")
        return ret
