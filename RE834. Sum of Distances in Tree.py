class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """
        # https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130583/C%2B%2BJavaPython-Pre-order-and-Post-order-DFS-O(N)
        
        
             [TREE] |      [COUNT]     [RET]
                0   |       10          [ ] = (1+0) + (7+10) +(1+0)  = 19      
              / | \ |      / | \       / | \ 
             1  2  3|     1  7  1     0  10 0       <--- ret[root] = sum(count[child])+sum(count[child])
               /|\  |       /|\         /|\                 走count[child]遍 root->child 
              4 5 6 |      4 1 1       4 0 0                再+走child到每个子path的值
             /|     |     /|          /|   
            7 8     |    1 2         0 1    
             /      |     /           /         
            9       |    1           0           
            
            
            
             [RET]  |                  |                  
                19  |           19     |       19             
              / | \ |          / | \   |      / | \ 
             0  10 0| [19-1+10-1] 10 0 |  28 [19-7+10-7] 0       <---  = parent.ret - root.count 
               /|\  |           /|\    |       /|\                      + (N - root.count)*1 
              4 0 0 |          4 0 0   |      4 0 0                       每一个其他node都远了一步
             /|     |         /|       |     /|   
            0 1     |        0 1       |    0 1    
             /      |         /        |     /         
            0       |        0         |    0         
            
        # Ans = [19,27,15,27,17,23,23,25,23,31] 
        --------------Example--------------------------------------------    
            
            Count         Ret
              6            8            8              8     
             / \          / \          /  \           / \
            1   4        0   3    [8-1+N-1] 2       12   6
               /|\          /|\          /|\            /|\
              1 1 1        0 0 0        3 4 5        10 10 [6-1+N-1]   N=6
        """
        
        ret, count = [0]*N, [1]*N
        tree = collections.defaultdict(list)
        
        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)
            
        def dfsBase(i, parent):
            for child in tree[i]:
                if child!=parent: 
                    dfsBase(child, i)
                    count[i] += count[child]
                    ret[i] += count[child] + ret[child]
        
        def bfs(i, parent):
            if parent>-1:
                ret[i] = ret[parent] - count[i] + (N - count[i])
            for child in tree[i]:
                if child!=parent:
                    bfs(child, i)
            
        
        dfsBase(0, -1)
        bfs(0, -1)
        
        return ret
