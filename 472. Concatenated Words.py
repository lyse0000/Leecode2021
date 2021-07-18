class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words, key = lambda w: len(w))
        wordset = set([words[0]])
        
        ret = []
        
        def isValidate(w):
            dp = [True] + [False]*len(w)
            for i in range(1, len(w)+1):
                for j in range(i):
                    if dp[j] and w[j:i] in wordset:
                        dp[i] = True
                        break
            return dp[-1]

        for idx in range(1,len(words)):
            if isValidate(words[idx]):
                ret.append(words[idx])
            wordset.add(words[idx])
        return ret
