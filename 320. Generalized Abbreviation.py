class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        # Undertand the question: https://leetcode.com/problems/generalized-abbreviation/discuss/77256/Could-anyone-help-to-understand-this-question
        ret = []
        def backTrack(w, path, count):
            if len(w) == 0:
                ret.append(path+str(count) if count>0 else path)
                return
            # skip and increase count
            backTrack(w[1:], path, count+1)
            # add curr char and zero the count
            backTrack(w[1:], path+(str(count) if count > 0 else "")+w[0], 0)
            
        backTrack(word, "", 0)
        return ret
