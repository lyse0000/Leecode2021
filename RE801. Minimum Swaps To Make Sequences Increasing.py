class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        """
        觉得更象hard

        https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/161887/Bottom-up-DP-with-Optimization-(Java-Python)
        
        
        
        """
        N = len(A)
        keep = [0]*N
        change  = [1]*N
        
        
        for i in range(1, N):
            increasing = A[i-1]<A[i] and B[i-1]<B[i]
            interchangeIncreasing = A[i-1]<B[i] and B[i-1]<A[i]
            
            if increasing and interchangeIncreasing:
                keep[i] = min(keep[i-1],change[i-1])
                change[i] = min(change[i-1], keep[i-1])+1
            elif increasing:
                keep[i] = keep[i-1]
                change[i] = change[i-1]+1
            else: # interchangeIncreasing
                keep[i] = change[i-1] # 要么之前换
                change[i] = keep[i-1] + 1 #要么这个换
                
        return min(keep[N-1], change[N-1])
