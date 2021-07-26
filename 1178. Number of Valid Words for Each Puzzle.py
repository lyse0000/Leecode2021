"""
subMask = originalMask = 1011 // [d, b, a]
(subMask - 1) & originalMask = (1011 - 1) & 1011 = 1010 & 1011 = 1010 // [d, b]
(subMask - 1) & originalMask = (1010 - 1) & 1011 = 1001 & 1011 = 1001 // [d, a]
(subMask - 1) & originalMask = (1001 - 1) & 1011 = 1000 & 1011 = 1000 // [d]
(subMask - 1) & originalMask = (1000 - 1) & 1011 = 0111 & 1011 = 0011 // [b, a]
(subMask - 1) & originalMask = (0011 - 1) & 1011 = 0010 & 1011 = 0010 // [b]
(subMask - 1) & originalMask = (0010 - 1) & 1011 = 0001 & 1011 = 0001 // [a]
(subMask - 1) & originalMask = (0001 - 1) & 1011 = 0000 & 1011 = 0000 // []
"""

class Solution:
    def getBitMask(self, string):
        bit = 0
        for c in string:
            i = ord(c) - ord('a')
            bit = bit | (1 << i)
        return bit
        
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        
        ans = [0]*len(puzzles)
        wordsCount = collections.Counter([self.getBitMask(w) for w in words]) 
        
        for i, p in enumerate(puzzles):
            mask = self.getBitMask(p)
            submask = mask
            fistLetter = ord(p[0]) - ord('a')
            
            while submask:
                if submask >> fistLetter & 1 :
                    ans[i] += wordsCount[submask]
                    
                #print(bin(submask), bin((submask - 1)))
                #if submask == 0:
                #    print("---------", bin(submask), bin((submask - 1)), bin ((submask - 1) & mask))
                #    break
                
                submask = (submask - 1) & mask
                
        return ans
