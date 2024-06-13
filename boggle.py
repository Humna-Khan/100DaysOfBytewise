class Boggle:
    def __init__(self, board, words):
        self.board = board
        self.words = set(words)
        self.rows = len(board)
        self.cols = len(board[0])
        self.result = set()

    def solveBoggle(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def dfs(r, c, currword):
            if not (0 <= r < self.rows and 0 <= c < self.cols) or self.board[r][c] == '#':
                return
            
            currword += self.board[r][c]
            
            if currword in self.words:
                self.result.add(currword)
            
            temp, self.board[r][c] = self.board[r][c], '#'
            for dr, dc in directions:
                dfs(r + dr, c + dc, currword)
            self.board[r][c] = temp
        
        for r in range(self.rows):
            for c in range(self.cols):
                dfs(r, c, "")

    def getResult(self):
        return list(self.result)

if __name__ == "__main__":
    board = [
        ['a', 'b', 'c', 'e'],
        ['s', 'f', 'c', 's'],
        ['a', 'd', 'e', 'e']
    ]
    words = ["abc", "cf", "see", "abfs", "sees"]

    solver = Boggle(board, words)
    solver.solveBoggle()
    result = solver.getResult()
    print("Words found in Boggle board:")
    for word in result:
        print(word)
