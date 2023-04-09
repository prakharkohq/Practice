"""
Attempted and scored by me in first attempt
"""

"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation:

There are no elements to the right of index 0.
It's interesting how running forward causes O(N^2) runtime and backward O(N). Nice solution!


"""


def replaceElements(arr):
    n = len(arr)
    results = []
    max_so_Far = -1
    results.append(max_so_Far)

    for i in range(n-1, -1, -1):
        if arr[i] > max_so_Far:
            max_so_Far = arr[i]
            results.append(arr[i])
        else:
            results.append(max_so_Far)
    results = results[0:n]
    results.reverse()
    return results


if __name__ == "__main__":
    print(replaceElements([400,1,434,5,5,5]))
