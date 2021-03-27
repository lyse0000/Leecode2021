class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        ""
        "()"
        "()()", "(())"
        "()()()", "()(())", "(())()", "((_))"
        
        
        n = 0   ""
        n = 1   "()"
        n = 2   "(" + [n=1] + ")" ,  "()" + [n=1]
        n = 3   "(" +[all n-1] + ")",  (( [n-2] )), ((( [n-3] )))
        
        """
        
        ret = []
        q = [("(", 1, 0)]
        
        while q:
            s, l, r = q.pop()
            if l==n and r==n:
                ret.append(s)
            if l>=r and l<=n and r<=n:
                q.append((s+"(", l+1, r))
                q.append((s+")", l, r+1))
        return ret
