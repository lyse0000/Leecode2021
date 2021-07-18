class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        while i<j:
            if s[i]!=s[j]:
                return self.checkPalindrome(s[i+1:j+1]) or self.checkPalindrome(s[i:j])
            i+=1
            j-=1
                
        return True
    
    def checkPalindrome(self, s):
        # 0  1  2 len//2 [-1:len//2:-1]
        # 0 1 2 3 len//2 [-1:len//2-1:-1]
        
        if len(s) == 1:
            return True
        if len(s)%2:
            return s[0:len(s)//2] == s[-1:len(s)//2:-1]
        else:
            return s[0:len(s)//2] == s[-1:len(s)//2-1:-1]
