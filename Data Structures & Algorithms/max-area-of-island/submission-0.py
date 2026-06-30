class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(grid: List[List[int]], row, col) -> int:
            currSize = 0
            grid[row][col] = 0
            if (row >= 1 and grid[row-1][col] == 1):
                currSize = currSize + helper(grid, row-1, col)
            if (row < len(grid)-1 and grid[row+1][col] == 1):
                currSize = currSize + helper(grid, row+1, col)
            if (col >= 1 and grid[row][col-1] == 1):
                currSize = currSize + helper(grid, row, col-1)
            if (col < len(grid[i])-1 and grid[row][col+1] == 1):
                currSize = currSize + helper(grid, row, col+1)
            return currSize + 1
        currSize = 0
        maxSize = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 1):
                    currSize = helper(grid, i, j)
                    if (currSize > maxSize):
                        maxSize = currSize
                currSize = 0
        return maxSize
    
