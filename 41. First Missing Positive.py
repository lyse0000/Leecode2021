class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        """
    [3,4,-1,1,6,2]
    
    [3,4,-1,1,6,2]  0  while  A[A[i]-1]!=A[i]  <- 当前的element是他该在的位置吗？ 不是？ 换！
    [-1,4,3,1,6,2]  0  while  A[A[i]-1]!=A[i] and A[i] > 0
    
    [-1,1,3,4,6,2]  1  while  A[A[i]-1]!=A[i] and A[i] > 0
    [1,-1,3,4,6,2]  1  while  A[A[i]-1]!=A[i] and A[i] > 0
    
    [1,-1,3,4,6,2]  2  while  A[A[i]-1]!=A[i] and A[i] > 0
    [1,-1,3,4,6,2]  3  while  A[A[i]-1]!=A[i] and A[i] > 0
    [1,-1,3,4,6,2]  4  while  A[A[i]-1]!=A[i] and A[i] > 0 and A[i]<=n
    
    [1,2,3,4,6,-1]  5  while  A[A[i]-1]!=A[i] and A[i] > 0 and A[i]<=n
    # 5 is missing
    
    
    1 2 3 4
    
    4 3 1 2    0  while  A[A[i]-1]!=A[i]
    2 3 1 4    0  while  A[A[i]-1]!=A[i]
    3 2 1 4    0  while  A[A[i]-1]!=A[i]
    
    3 2 1 4    1  while  A[A[i]-1]!=A[i]
    1 2 3 4    2  while  A[A[i]-1]!=A[i]
    
    """   
        n, A = len(nums), nums
        
        for i in range(n):
            while A[i]>0 and A[i]<=n and A[A[i]-1]!=A[i]:
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
                
        
        for i in range(n):
            if A[i]!= i+1:
                return i+1
        return n+1
