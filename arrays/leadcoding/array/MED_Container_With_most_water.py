"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case
the max area of water (blue section) the container can contain is 49.
"""


def solution_worst_n_square(arr):
    max_volume = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr), 1):
            height = min(arr[i], arr[j])
            width = j - i
            area = height * width
            if area > max_volume:
                max_volume = area
    return max_volume


""" 
Here Solutioning would be done using greedy approach where we will calculate the max_area and move untill left is less 
then right
"""


def solution(arr):
    max_volume = 0
    l = 0
    r = len(arr) - 1
    while l < r:
        height = min(arr[l], arr[r])
        width = r - l
        area = height * width
        if area > max_volume:
            max_volume = area

        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return max_volume


if __name__ == "__main__":
    print(solution([1, 8, 6, 2, 5, 4, 8, 3, 7]))
