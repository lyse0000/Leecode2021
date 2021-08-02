class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        
        data = collections.defaultdict(list)
        rawdata = sorted(zip(username, timestamp, website), key = lambda x: (x[0], x[1]))
        
        for user, time, web in rawdata:
            data[user].append(web)
            
        pattern = collections.Counter()
        # combinations('ABCD', 2) --> AB AC AD BC BD CD
        for user in data:
            #print(combinations(data[user], 3))
            pattern.update(set(combinations(data[user], 3)))

        return min(pattern, key = lambda x: (-pattern[x], x))
