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
