class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        mapx = collections.defaultdict(list)
        mapy = collections.defaultdict(list)
        points = sorted(points)
        seen = set()
        
            
        ret = float('inf')
        
        # [[1, 1], [1, 3], [2, 2], [3, 1], [3, 3]]    
        for x, y in points:
            
            for xi in mapy[y]:
                for yi in mapx[x]:
                    if (xi, yi) != (x, y) and (xi, yi) in seen:
                        ret = min(ret, (y-yi)*(x-xi))
            mapx[x].append(y)
            mapy[y].append(x)
            seen.add((x,y))    
                
        return 0 if ret == float('inf') else ret
