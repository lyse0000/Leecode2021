class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        https://leetcode.com/problems/car-fleet/discuss/139850/C%2B%2BJavaPython-Straight-Forward
        visulization:
            https://youtu.be/H5w6doOXz10
        """
        
        
        group = (sorted(zip(position, speed)))
        group.reverse()
        print(group)
        t, ret = -1, 0
        
        for p, s in group:
            time = float(target-p)/s
            if time > t:
                t = time
                ret += 1
        return ret
