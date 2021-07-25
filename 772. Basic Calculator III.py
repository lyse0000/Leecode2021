class Solution:
    def calculate(self, s: str) -> int:
        stack = [0]
        prev = []            
        while s:
            if s[0] == '/':
                num, s = self.getNum(s[1:])
                stack[-1] = int(stack[-1]/num)
            elif s[0] == '*':
                num, s = self.getNum(s[1:])
                stack[-1] *= num
            elif s[0] == '+':
                num, s = self.getNum(s[1:])
                stack.append(num)
            elif s[0] == '-':
                num, s = self.getNum(s[1:])
                stack.append(-num)
            else: # num or "()"
                num, s = self.getNum(s)
                stack.append(num)
        
        return sum(stack)

    
    def getNum(self, s):
        if s[0] == '(':
            j = 1
            while s[j]!=')' or not self.isValidPara(s[0:j+1]): 
                j+=1
            return (self.calculate(s[1:j]), s[j+1:])
        num = ""
        i = 0
        while i<len(s) and s[i] in {'1','2','3','4','5','6','7','8','9','0'}:
            num += s[i]
            i += 1
        return (int(num), s[i:])
            
    
    def isValidPara(self, data):
        rightcount = 0
        for d in data:
            if d == ')':
                if rightcount<1: return False
                rightcount-=1
            elif d == '(':
                rightcount+=1
        return rightcount == 0
