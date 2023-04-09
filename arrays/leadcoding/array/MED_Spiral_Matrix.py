"""
Spiral Matrix :

Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""



def playground(matrix):
    top_left = [item[0] for item in matrix]
    print(top_left)

if __name__ == "__main__":
    print(playground(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))


def solution(matrix):
    result = list()
    while len(matrix) > 0:
        try:
            result += matrix.pop(0)  # remove the first nested list (top row)
            result += [x.pop(-1) for x in matrix]  # remove every last element of the lists (right row)
            result += matrix.pop(-1)[::-1]  # remove last nested list in reverse order (bottom row)
            result += [x.pop(0) for x in matrix][::-1]  # remove every last element of the lists (left row)
        except:
            break  # if at any moment the matrix is empty, break the loop and return the result array
    return result