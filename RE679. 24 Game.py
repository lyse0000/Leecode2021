class Solution:
    # solution 1
    def judgePoint24(self, nums: List[int]) -> bool:
        
        """ 
        operate(a, b): a*b, a-b, b-a, a+b, a/b or 0, b/a or 0 
        
        1, 2, 3, 4
        
        for x in [1,2,3,4]
            每一个x给他一个当base的机会 -》 permutation ABC ACB BAC BCA CAB CBA
            for y in [1,2,3,4]:
                backtrack([ (x operate y), others])
                    ...
        """
        
        if len(nums) == 1:
            return round(nums[0], 4) == 24

        def operation(a, b):
            return set([a*b, a-b, b-a, a+b, a/b if b else 0, b/a if a else 0])
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if i!=j:
                    nextnums = nums[:i] + nums[i+1:j] + nums[j+1:]
                    values = operation(nums[i], nums[j])
                    for v in values:
                        if self.judgePoint24(nextnums+[v]): return True
        return False
            
            class Solution:

  
  # solution 2
  def judgePoint24(self, nums: List[int]) -> bool:
   
        if len(nums) == 1:
            return round(nums[0], 4) == 24

        def operation(a, b):
            return set([a*b, a-b, b-a, a+b, a/b if b else 0, b/a if a else 0])
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if i!=j:
                    #values = operation(nums[i], nums[j])
                    nextnums = [x for k, x in enumerate(nums) if k!=i and k!=j]
                    if self.judgePoint24(nextnums + [nums[i] + nums[j]]): return True
                    if self.judgePoint24(nextnums + [nums[i] * nums[j]]): return True
                    if self.judgePoint24(nextnums + [nums[i] - nums[j]]): return True
                    if self.judgePoint24(nextnums + [nums[j] - nums[i]]): return True
                    if nums[j] != 0 and self.judgePoint24(nextnums + [nums[i] / nums[j]]): return True
                    if nums[i] != 0 and self.judgePoint24(nextnums + [nums[j] / nums[i]]): return True
        return False
            
