class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        curr = 1 if player == 1 else -1
        self.rows[row] += curr
        self.cols[col] += curr
        if row == col:
            self.diagonal += curr
        
        if col == self.n - row -1:
            self.antidiagonal += curr
        n = self.n
        if (abs(self.rows[row]) == n or abs(self.cols[col]) == n or 
        abs(self.diagonal) == n or abs(self.antidiagonal) == n):
            return player
        return 0


        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
