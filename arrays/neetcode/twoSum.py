"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

"""
In this technique We are saving values 
"""


def two_sum(arr, sum):
    data_dict = {}
    # Lookup structure for the value traversal
    for index, item in enumerate(arr):
        data_dict[item] = index

    for index, item in enumerate(arr):
        desired = sum - item
        if desired in data_dict.keys():
            second_index = data_dict.get(desired)
            print(f"\n Two Sum found at index {index} and {second_index}")
            return {index, second_index}





if __name__ == "__main__":
    print(two_sum([1, 2, 43, 5, 6], 7))
