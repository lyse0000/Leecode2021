class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        [[0,1,10],[1,0,1],[1,2,5],[2,0,5],[3,1,2]]
        0 -10+1+5= -4
        1 10-1-5+2 = 6
        2 0
        3 -2
        """
        
        """
        [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
        0 -4
        1 10-1-5 = 4
        2 0
        """
        
        m = collections.defaultdict(int)
        
        for t in transactions:
            m[t[0]] -= t[2]
            m[t[1]] += t[2]
        
        debt = [m[i] for i in m]
        
        def dfs(s):
            while (s < len(debt) and debt[s] == 0):
                s+=1
            if s == len(debt): return 0
            
            ret = float('inf')
            for i in range(s+1, len(debt)):
                if debt[i]*debt[s] < 0: # opposite signs
                    # try settle s with i
                    debt[i] += debt[s]
                    ret = min(ret, 1+dfs(s+1))
                    # backtrack
                    debt[i] -= debt[s]
            return ret
        
        return dfs(0)
         
