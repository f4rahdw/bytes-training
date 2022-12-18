#Unique Paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1: return 1
        if m==0 or n==0: return 0

        grid = [[0]*n for i in range(m)]

        for i in range(m):
            grid[i][0] = 1
        for j in range(n):
            grid[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j]+grid[i][j-1]
        return grid[-1][-1]