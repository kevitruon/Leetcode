class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(0,m-2):
            for j in range(0,n-2):
                top = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                bot = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                res = max(res, top+bot+grid[i+1][j+1])
        return res

        