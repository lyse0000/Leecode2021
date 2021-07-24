class TicTacToe:

    """
            0 1 2 3 4
        0           0,4
        1         1,3
        2       2,2
        3     3,1
        4   0,4   -> row+colum = n-1
    """

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.colum = [0]*n
        self.rows = [0]*n
        self.diagno = 0
        self.antdi = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        addition = player*2 - 3
        self.colum[col] += addition
        self.rows[row] += addition
        
        if row == col:
            self.diagno += addition
        if row+col == self.n-1:
            self.antdi += addition
            
        if (abs(self.rows[row]) == self.n or
            abs(self.colum[col]) == self.n or
            abs(self.diagno) == self.n or
            abs(self.antdi) == self.n ):
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
