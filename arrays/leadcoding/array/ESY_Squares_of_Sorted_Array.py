"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in
non-decreasing order.
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Follow up: Squaring each element and sorting the new array is very trivial,

could you find an O(n) solution using a different approach?

"""
import collections

"""

Concept Pay closer attention to question here interviewer is giving us input array in sorted form which creates 
squared list such that negative to zero numbers are decreasing and later numbers are increasing 
squares of the negatives decrease, and then the squares of the positives increase, i.e.
[-4, -2, -1, 0, 1, 2, 3, 5] -> [16, 4, 1, 0, 1, 4, 9, 25]

"""


def sortedSquares(nums):
    """
    This approach uses O(1) memory beyond the input array, and is truely in-place. However,
    it is not always a good idea to overwrite inputs. Remember that because we passed it by reference,
    the original is actually lost. Often functions like this are a part of an API, and in a lot of cases,
    nobody wants an API that clobbers their input.

    I think it's best to ask your interviewer if they want something done in-place or not.
    It is a common misconception that we should always be trying to do things in-place, overwriting the inputs.

    """
    for index, item in enumerate(nums):
        nums[index] *= nums[index]
    # nums.sort() This is in place!
    return sorted(nums)


def sortedSquares_approach2(nums):
    # For numeric data types, double-asterisk (**) is defined as an Exponentiation Operator
    # It takes 3*N memory as becuase it allocates memory on list comprehension sorted and iteratio
    return sorted([item ** 2 for item in nums])


def sorted_square_attempt(nums):
    answer = []
    for index, item in enumerate(nums):
        nums[index] = nums[index] * nums[index]

def sorted_square_deque_my_Attempt(nums):
    queue = collections.deque(nums)
    temp_array = []
    while len(queue) > 0:
        left_square = queue[0] ** 2
        right_square = queue[-1] ** 2
        if left_square > right_square:
            temp_array.append(left_square)
            queue.popleft()
        else:
            temp_array.append(right_square)
            queue.pop()

    return temp_array[::-1]

#  It's O(n) time, and O(N) auxillary space.

def sorted_square_solution(A):
    return_array = [0] * len(A)
    write_pointer = len(A) - 1
    left_read_pointer = 0
    right_read_pointer = len(A) - 1
    left_square = A[left_read_pointer] ** 2
    right_square = A[right_read_pointer] ** 2
    while write_pointer >= 0:
        if left_square > right_square:
            return_array[write_pointer] = left_square
            left_read_pointer += 1
            left_square = A[left_read_pointer] ** 2
        else:
            return_array[write_pointer] = right_square
            right_read_pointer -= 1
            right_square = A[right_read_pointer] ** 2
        write_pointer -= 1
    return return_array


"""
This approach is the first of the trading-off-some-raw-performance-for-beauty=and-elegance approaches. 
It remains as O(n) time complexity like approach 2, but the heavy-weight nature of it will slow it down by a constant 
amount. If this doesn't matter though (and in a lot of cases it doesn't), then the elegance will reduce the risk of 
bugs and lead to more readable and maintable code. It is also important to note that it does use O(n) auxillary space.
"""


def sorted_square_solution_approach2(A):
    number_deque = collections.deque(A)
    reverse_sorted_squares = []
    while number_deque:
        left_square = number_deque[0] ** 2
        right_square = number_deque[-1] ** 2
        if left_square > right_square:
            reverse_sorted_squares.append(left_square)
            number_deque.popleft()
        else:
            reverse_sorted_squares.append(right_square)
            number_deque.pop()
    return reverse_sorted_squares[::-1]


if __name__ == "__main__":
    nums = [-7, -3, 2, 3, 11]
    print(sorted_square_deque_my_Attempt(nums=nums))
