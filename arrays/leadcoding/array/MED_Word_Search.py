"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

leetcode Link : https://leetcode.com/problems/word-search/
"""

# Solution 1 Backtracking with recursion
"""
Backtracking is basically Brute Force, where we check all possibilities using a Recursive Function.
The most important parts of backtracking using recursive function are:
(1) return when we reach to the end and no more states can be generated.
(2) restore the state after calling the recursive function.

def backtrack(state):
(1) if there are no more states that can be generated from the current state, return.

For loop
    (2) change the current state to its neighboring state
    (3) backtrack(state)
    (4) restore the state (backtrack)
https://leetcode.com/problems/word-search/solutions/2843530/python3-backtracking-not-tle-for-beginners-only/  

m * n * (3^K) -> where m,n are no of columns, no of rows and k is the word length. 
The given word can start from any cell.
So, We have to traverse each cell of the board. So, it will take nm time for two for loops.
For each cell we will try to find the given word, we have 3 direction to explore (as we can't go to the direction
from which we came so there are 3 posibilities)
The max depth of the recursion Tree can be the length of the given word (let length be k)
So, considering the depth (k) and and 3 direction to explore the TC for each cell will come out to be 3^k
So, the overall time complexity will be O(n * m * (3^k))  
"""


def solution_bktrck(words, target):
    m, n = len(words), len(words[0]) # dimension of matrix
    valid_directions = [[0,1],[1,0],[0,-1],[-1,0]]

    # K here is the index for which we are trying to generate all the permutations

    def backtrack(i, j , visited, k):
        # Base Condition or termination conditio
        if words[i][j] == target[k]:
            if k == len(target) - 1:  # we are at last word and that word is actually the termination word
                return True

            # check all the other direction for that word
            for xn, yn in valid_directions:
                # new Index
                x, y = xn+i, yn+j
                if 0 <= x < m and 0 <= y < n and (x,y) not in visited:  # jab ye ek valid value hai to recursive node mein isko visited mein daaliye
                    visited.add((x,y))
                    # aage isi node se backtrack karo agar response true aaye to true return kar do till last node is found
                    if backtrack(x,y, visited, k+1):
                        return True
                # otherwise visited se ye nikal lo yahi back tracking h
                    visited.remove((x,y))
        return False

    for i in range(m):
        for j in range(n):
            # Visisted is not dict rather a set
            if backtrack(i, j, {(i,j)},0):
                return True
    return False


if __name__ == "__main__":
    print(solution_bktrck([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))


# 8708927  -- > cyware