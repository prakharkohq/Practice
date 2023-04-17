"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""


def solution(grid):
    # First step is always clean validation
    if not grid:
        return 0

    row, col = len(grid), len(grid[0])
    visited = set()
    num_islands = 0
    valid_directions = [[0,1], [0,-1], [-1,0], [1,0]]

    def bfs(r,c):
        from collections import deque
        queue = deque()
        queue.append((r,c))

        while queue:
            row, col = queue.popleft()
            for dr,dc in valid_directions:
                r_n, c_n = dr + row, dc + col
                if r_n in range(len(grid)) and c_n in range(len(grid[0])) and grid[r_n][c_n] == "1" and (r_n, c_n) not in visited:
                    queue.append((r_n,c_n))
                    visited.add((r_n,c_n))



    # First step is to iterate over every element of the array and if it is a 1 we need to do a BFS for neighbouring
    # nodes to find out the nearest connected nodes , Before doing a BFS we need to check that node should not be in
    # visited list of nodes

    for r in range(row):
        for c in range(col):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)
                num_islands+=1

    return num_islands

if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(solution(grid))
