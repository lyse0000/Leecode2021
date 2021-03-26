class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        """  
                  #
                  #
                # #
                # #
                # #
                # #
            #   # # 
            # # # # #
            # # # # # #
            0 1 2 3 4 5

        """

        i, j, ret = 0, len(height)-1, 0
        
        while i<j:
            ret = max(ret, (j-i)*min(height[i] ,height[j]))
            if height[i]<=height[j]:
                i+=1
            else: j-=1
            
        return ret
