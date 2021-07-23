class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        """
        (())())))))()(((()())
        0123456789012345678901    
        """
        ret = 0
        stack = [0] + stack + [len(s)]
        for i in range(1, len(stack)):
            ret = max(ret, (stack[i] - stack[i-1])//2*2)
        return ret
        
