class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n>0:
            return self.helper(x, n)
        else: 
            return self.helper(1/x, -n)
        
    def helper(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        half = self.helper(x, n//2)

        return half*half if n%2 == 0 else half*half*x
    
# ============================================================================================
# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0: 
            return 0
        if 3>=x:
            return 1
        
        low, hi = 2, x//2
        
        while low<=hi:
            mid = (hi+low)//2
            if mid**2<=x and (mid+1)**2>x:
                return mid
            if mid**2>x:
                hi = mid-1
            else:
                low = mid+1
        return low
