class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        table = collections.Counter([char for char in t])
        
        missing = len(t)
        counter = collections.Counter()
        minStart, minLen = len(s)-1, -1
        start, end = 0, 0
        
        idx, i = [], 0 # index for all valid chars in s
        # increase end to find all missing
        # increase start to find min
        while end < len(s):
            while missing>0 and end<len(s):
                if s[end] in t:
                    counter[s[end]]+=1
                    idx.append(end)
                    if counter[s[end]] <= table[s[end]]:
                        missing -= 1
                end+=1
                
            # now missing == 0
            
            if not idx or i>=len(idx): break #no valid char
            
            while missing == 0 and i<len(idx): # missing = 0 i就可以一直往前
                if (minLen > end-idx[i] or minLen < 0):
                    minLen = end-idx[i]
                    minStart = idx[i]
                counter[s[idx[i]]]-=1
                if counter[s[idx[i]]] < table[s[idx[i]]]:

                    missing+=1
                i+=1
                
        return s[minStart:minStart+minLen]
