class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # idea is one time can only have one
        
        stack = []
        prevtime = 0
        
        ans = [0]*n
        
        for log in logs:
            idx, startend, time = log.split(':')
            idx, time = int(idx), int(time)
            
            if startend == "start":
                # 1234
                # aaaB
                if stack:
                    ans[stack[-1]] +=  time - prevtime
                prevtime = time
                stack.append(idx)
            else:
                # end
                # 123456
                # aaaBB_
                ans[stack[-1]] += time - prevtime + 1
                prevtime = time + 1
                stack.pop()
                
        return ans
        
