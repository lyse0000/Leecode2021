class Solution:
    def exist(self, board: List[List[str]], word: str, steps = None) -> bool:
        self.m, self.n = len(board), len(board[0])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.helper(board, word, i, j):
                        return True
                    
        return False
    
    def helper(self, board, word, i, j):
        if len(word)<1:
            return True
        if not 0 <= i < self.m or not 0 <= j < self.n:
            return False
        if board[i][j] == word[0]:
            board[i][j] = "#"
            if (self.helper(board, word[1:], i+1, j) or
                self.helper(board, word[1:], i-1, j) or
                self.helper(board, word[1:], i, j+1) or
                self.helper(board, word[1:], i, j-1)):
                return True
            board[i][j] = word[0]
        return False
