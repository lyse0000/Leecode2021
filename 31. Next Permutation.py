class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find last [k] that [k]<[k+1] 有交换价值
        # B : B is find from n-1 -> 0, the first element > [k]
        # swap
        # rotate list[k+1:]
        
        # https://www.dcode.fr/permutations-generator
        
        # ... 4 5 2 4 3 9 7
        
        n, k, B = len(nums), -1, 0
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                k = i
                break
        
        # case 4 3 2 1
        if k == -1:
            nums.reverse()
            return
        
        for i in range(n-1, k, -1):
            if nums[i] > nums[k]:
                B = i
                break
                
        nums[B], nums[k] = nums[k], nums[B]
        L, R = k+1, n-1
        print(k, B)
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L+=1
            R-=1
        
        return 
