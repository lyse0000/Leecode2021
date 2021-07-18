class TrieNode:
    def __init__(self):
        self.nexts = collections.defaultdict(TrieNode)
        self.word = ""
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, w):
        temp = self.root
        for c in w:
            temp = temp.nexts[c]
        temp.word = w
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.ret = []
        self.trie = Trie()
        self.troot = self.trie.root
        self.m, self.n = len(board), len(board[0])
        
        for w in words:
            self.trie.insert(w)
            
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(board, self.troot, i, j)
                
        return self.ret
        
    def dfs(self, board, tnode, i, j):
        if tnode.word:
            self.ret.append(tnode.word)
            tnode.word = None
        
        if not (0<=i<self.m and 0<=j<self.n) or (board[i][j] not in tnode.nexts):
            return
        
        char = board[i][j]
        
        tnode = tnode.nexts[char]
        board[i][j] = '#'
        self.dfs(board, tnode, i+1, j)
        self.dfs(board, tnode, i-1, j)
        self.dfs(board, tnode, i, j+1)
        self.dfs(board, tnode, i, j-1)
        board[i][j] = char
        return 
        
