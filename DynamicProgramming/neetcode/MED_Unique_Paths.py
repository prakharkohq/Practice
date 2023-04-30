"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-
right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

"""
Time Complexity : O(2 ^ (m+n)), where m and n are the given input dimensions of the grid
Space Complexity : O(m+n), required by implicit recursive stack
"""
class Solution:
    def uniquePaths(self, m, n, i=0, j=0):
        if i >= m or j >= n:      return 0
        if i == m-1 and j == n-1: return 1
        return self.uniquePaths(m, n, i+1, j) + self.uniquePaths(m, n, i, j+1)

"""
Solution - II (Dynamic Programming - Memoization)

The above solution had a lot of redundant calculations. There are many cells which we reach multiple times and calculate
the answer for it over and over again. However, the number of unique paths from a given cell (i,j) to the end cell is
always fixed. So, we dont need to calculate and repeat the same process for a given cell multiple times. We can just 
store (or memoize) the result calculated for cell (i, j) and use that result in the future whenever required.

Thus, here we use a 2d array dp, where dp[i][j] denote the number of unique paths from cell (i, j) to the end cell
 (m-1, n-1). Once we get an answer for cell (i, j), we store the result in dp[i][j] and reuse it instead of recalculating it.
"""

class Solution:
    def uniquePaths(self, m, n):
        @cache
        def dfs(i, j):
            if i >= m or j >= n:      return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)
# Time Complexity : O(m*n), the answer to each of cell is calculated only once and memoized. There are m*n cells in
# total and thus this process takes O(m*n) time.
# Space Complexity : O(m*n), required to maintain dp.