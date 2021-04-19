class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        N = len(heights)
        
        left, stack = [i for i in range(N)], []
        for i in range(0, N):
            if len(stack) == 0: 
                left[i] = 0
            while stack and heights[stack[-1]]>=heights[i]:
                left[i] = left[stack.pop()]
            stack.append(i)
        
        right, stack = [i for i in range(N)], []
        area = 0
        for i in range(N-1, -1, -1):
            if len(stack) == 0:
                right[i] = N-1
            while stack and heights[stack[-1]]>=heights[i]:
                right[i] = right[stack.pop()]
            stack.append(i)
            area=max(area,((right[i]-left[i]+1)*heights[i]))
        
        return area
        
# solution 2        
def largestRectangleArea(self, height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans
