"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

 * clockwise rotate
 * first reverse up to down, then swap the symmetry
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3

"""


def solution(matrix):  # Clockwise
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

"""
/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
"""


def solution_anticlockwise(nums):
    # First Reverse the matrix
    for i in range(len(nums)):
       nums[i].reverse()
    # Transpose the matrix
    for i in range(len(nums)):
        for j in range(i,len(nums),1):
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]

    print(nums)

if __name__ == "__main__":
    print(solution_anticlockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))