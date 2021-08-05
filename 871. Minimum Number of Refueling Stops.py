class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        """
        [[10,60],[20,30],[30,30],[60,40]]
        target = 100, startFuel = 10, 
        """
        ret = 0
        i = 0
        curr = startFuel
        heap = []
        while curr < target:
            while i <len(stations) and curr>=stations[i][0]:
                heapq.heappush(heap, -stations[i][1])
                i+=1
            if len(heap) == 0:
                return -1
            ret+=1
            curr-=heapq.heappop(heap)  # 0,2   1,2     2,1,    5,0
       
        return ret
            
