class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
      
        # https://www.youtube.com/watch?v=mKUsbABiwBI&t=802s&ab_channel=%E5%B0%8F%E5%B0%8F%E7%A6%8FLeetCode
        
        graph = collections.defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        degree = [-1]*n
        ret = []
        def dfs(parent, node, level):
            # init
            degree[node] = level+1
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if degree[neighbor] == -1:
                    # travel this neighbor
                    degree[node] = min(degree[node], dfs(node, neighbor, level+1))
                else:
                    # visited node, just rade its degree
                    degree[node] = min(degree[node], degree[neighbor])
            #print(parent,node)   
            if degree[node] == level+1 and parent in graph:
                # not in cycle
                # parent to node only touch once
                ret.append([parent, node])
            return degree[node]
        dfs(-1,0,0)
        return ret
