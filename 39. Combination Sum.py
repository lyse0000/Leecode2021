class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        def _combin(elements, combined, next_target):
            if next_target == 0:# and combined not in ret:
                ret.append(combined)
                return
            if len(elements)<1 or next_target<elements[0]:
                return
            for i, e in enumerate(elements):
                if next_target>=e:
                    _combin(elements[i:], combined+[e], next_target-e)
            
        _combin(candidates, [], target)   
        return ret
    """
    [i:] not [i+1:] means take current again. 
    example: [2,3,6,7], target = 7
    [2,2,|2|] [2,2,|3|], [2,2,|[4,6,7]|], [2,|3|], [2,|4|]
    "|x|" means current dfs level
    """
