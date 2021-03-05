class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n<2:
            return []
        
        ret, i = [], 2
        
        while n>=i*i: 
            if n % i == 0:
                ret.append([i,int(n/i)])
                otherFactors = self.getFactors(n/i)
                for f in otherFactors:
                    if f[0] >= i:           # case of n=32, [4,8], since [2,2,2,4] or [2,4,4] will be include previously
                        ret.append([i] + f)
            i+=1
        return ret
      
      
      """
        Input: 32
        Output:
        [
          [2, 16],
          [2, 2, 8],
          [2, 2, 2, 4],
          [2, 2, 2, 2, 2],
          [2, 4, 4],
          [4, 8]
        ]
      """
