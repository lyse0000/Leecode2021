class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        ret, A, n = [], candidates, len(candidates)
        
        def _combin(start, remaining, path):
            if remaining == 0:
                ret.append(path)
            if start>=n or A[0]>remaining:
                return
            for i in range(start, n):
                if i==start or A[i]!= A[i-1] and A[i]<=remaining:
                    _combin(i+1, remaining-A[i], list(path)+[A[i]])
                  
        _combin(0, target, [])
        return ret
    
        """
        ret = []
        candidates.sort()
        
        def _combin(elements, remaining, path):
            if remaining == 0:
                ret.append(path)
            if not elements or len(elements)<1:
                return
            for i, e in enumerate(elements):
                if i<1 or e!= elements[i-1] and e<=remaining:
                    _combin(elements[i+1:], remaining-e, list(path)+[e])
                  
        _combin(candidates, target, [])
        return ret
        """  
        
