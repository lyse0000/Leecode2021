class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def ispal(w):
            return w == w[::-1]
        """
        ppere
        
        after:
        ppere||erepp
        pper|e|repp
        pp|ere|pp
        
        before:
        erepp||ppere
        erep|p|pere
        ere|pp|ere
        """
        wordset = {w:i for i,w in enumerate(words)}
        ret = []
        visited = set()
        for w in words:
            n = len(w)
            for i in range(n+1):
                after = w[:n-i]
                ap = w[n-i:]
                before = w[i:]
                bp = w[:i]
                
                afterR = after[::-1]
                if afterR!=w and ispal(ap) and afterR in wordset:
                    temp = (wordset[w],wordset[afterR])
                    if temp not in visited:
                        visited.add(temp)
                        ret.append([temp[0], temp[1]])
                        
                beforeR = before[::-1] 
                if beforeR!=w and ispal(bp) and beforeR in wordset:
                    temp = (wordset[beforeR],wordset[w])
                    if temp not in visited:
                        visited.add(temp)
                        ret.append([temp[0], temp[1]])
                
        return ret
        
        

        
