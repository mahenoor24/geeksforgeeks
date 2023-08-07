class Solution:
    def SolveSudoku(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for c in range(1, 10):
                        if self.isValid(grid, i, j, c):
                            grid[i][j] = c
                            if self.SolveSudoku(grid) == True:
                                return True
                            else:
                                grid[i][j] = 0
                    return False
        return True
    
    def isValid(self, grid, row, col, c):
        for i in range(9):
            if grid[i][col] == c:
                return False
            if grid[row][i] == c:
                return False
            if grid[3*(row//3)+(i//3)][3*(col//3)+(i%3)] == c:
                return False
        return True
    
    def printGrid(self, grid):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=" ")