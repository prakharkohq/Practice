"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

"""

# Leetcode solution
def generate(numRows):
    output = [[1]]
    for i in range(1, numRows):
        curr = [1]
        j = 1
        while (j < i):
            # Calculate the elements of a row, add each pair of adjacent elements of the previous row in each step of
            # the inner loop save the prev for further processing
            curr.append(prev[j - 1] + prev[j])
            j += 1
        curr.append(1)
        output.append(curr)
        prev = curr
    return output


def pascal_triangle(nums):
    ## ACCEPTED ON LEETCODE
    result = []
    for i in range(nums):
        if i == 0:
            result.append([1])
            continue
        if i == 1:
            result.append([1,1])
            continue
        if i == 2:
            result.append([1,2,1])
            continue
        else:
            target_list = result[i-1]
            new_list = []
            for i in range(len(target_list)-1):
                new_list.append(target_list[i]+target_list[i+1])
            new_list.insert(0, 1)
            new_list.append(1)
            result.append(new_list)

    return result



if __name__ == "__main__":
    print(generate(3))
