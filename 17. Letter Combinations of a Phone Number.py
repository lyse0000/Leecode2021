class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        def backtrack(prevcombin, nextdigits):
            if len(nextdigits) == 0:
                if len(prevcombin)>0:   
                    ret.append(prevcombin)
                return
            for c in dic[nextdigits[0]]:
                backtrack(prevcombin+c, nextdigits[1:])
            
        ret = []
        backtrack("", digits)
        return ret
