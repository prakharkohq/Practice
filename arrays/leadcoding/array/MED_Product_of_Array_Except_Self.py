"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

"""
Approach 1  -> Calculate two arrays left multiple and right multiple from those two arrays take the right values 
               of prefix sum and postfix sum to multiply the values and come to a solution
               
Approach 2 -> you can reduce the space complexity by reutalising the results array
"""

def solution_raw(nums):
    left_multiple = [1] * len(nums)
    right_multiple = [1] * (len(nums) + 1)
    answer = [1] * len(nums)
    for i in range(1, len(nums)):
        left_multiple[i] = left_multiple[i - 1] * nums[i-1]

    for i in range(len(right_multiple) - 2, 0, -1):
        right_multiple[i-1] = right_multiple[i] * nums[i]

    for i in range(len(answer)):
        answer[i] = left_multiple[i] * right_multiple[i]
    return answer

""" 

Optimisation 
we can optimize the space complexity to O(1) by using the result array to store the left_product array and computing the
right_product array on-the-fly during the final calculation. Here's the optimized solution.

In this optimized solution, we reuse the result array to store the left_product array. We then compute the product of 
elements to the right of each element on-the-fly by keeping track of a running product, right_product. We update the 
corresponding element in result with the product of the left and right products for that element. 
This way, we only need to use one extra variable (right_product) instead of a whole extra array (right_product).
"""


def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    # calculate the product of elements to the left of each element and store in result
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    # calculate the product of elements to the right of each element and update result
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result

if __name__ == "__main__":
    print(solution_raw([-1,1,0,-3,3]))
