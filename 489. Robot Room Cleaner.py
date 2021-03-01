# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        """
        https://leetcode.com/problems/robot-room-cleaner/discuss/150132/Very-clear-Python-DFS-code-beat-99-%2B
        
         (dx, dy) is direction, for example (0, 1) is up, and by using dx, dy = -dy, dx, (0,1) becomes (-1, 0), which is a left vector in x-y axis plane.
        (0,1) -> (-1, 0) -> (0,-1) -> (1,0)
        
        
                (0，1)
         (-1,0)  _|_ (1,0)
                  |
                (0，-1)
        Turn_left  = (-curry, currx) from (currx, curry)
        """
        
        cleaned = set()
        def dfs(x, y, dx, dy):
            # 1. clean current
            robot.clean()
            cleaned.add((x,y))
            
            # 2. go down 4 direction DFS_ly
            for i in range(4):
                if (x+dx, y+dy) not in cleaned and robot.move():
                    dfs(x+dx, y+dy, dx,dy)
                robot.turnLeft()
                dx, dy = -dy, dx
                
            # 3. go back to previous cell, and go back to facing diection 
            robot.turnLeft(); robot.turnLeft()
            robot.move()
            robot.turnLeft(); robot.turnLeft()
        
        dfs(0,0,0,1)
            
