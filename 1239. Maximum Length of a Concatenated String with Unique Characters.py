class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Python set operations:
        # https://www.geeksforgeeks.org/python-set-operations-union-intersection-difference-symmetric-difference/
        
        ret = [set()] # list of sets
        
        for s in arr:
            if len(set(s)) == len(s):
                s = set(s)
                for r in ret:
                    if len(r & s)<1:
                        ret.append(r | s)
        
        return max( len(r) for r in ret )
