class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        
        """
        
        从k开始 ..... k+0, k+1, k+2,k+(i-1) = N
        i个
        N = i*k + (i-1 + 0)*i/2
        
        we know i>0, k>0, so i*k>0
        
        so,  N =  [i*k] + (i-1 + 0)*i/2 > (i-1 + 0)*i/2 - [i*k]
        
        so 2N > (i - 1)*i
        
        
        for i in range that (i-1)*i < 2N:
            if we can find a int k such that 
           ( N-(i-1)*i/2   ) /i is an int
            ans+=1
        
        #https://leetcode.com/problems/consecutive-numbers-sum/discuss/128959/JavaPython-3-5-liners-O(N-0.5)-Math-method-w-explanation-and-analysis.
        """
        ans = 0
        i = 1
        while (i-1)*i < 2*N:
            if (N - (i-1)*i//2)%i == 0:
                ans+=1
            i+=1
        return ans
                
            
