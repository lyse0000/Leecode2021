class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
        counts = collections.Counter(hand)
        
        for n in sorted(hand):
            c = counts[n]
            if c > 0:
                for j in range(W):
                    counts[n + j]-=c
                    if counts[n + j] < 0: return False
                    
        return True
        
