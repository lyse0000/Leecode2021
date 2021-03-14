class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        if n == 0: return ""
        if n == 1: return "1"
        if n == 2: return "11"
        
        s = self.countAndSay(n-1)
        ret, i = "", 0
        
        while i<len(s):
            count = 1
            while i+1<len(s) and s[i+1]== s[i]:
                i+=1
                count+=1
            ret += str(count)+s[i]
            i+=1
    
        return ret
