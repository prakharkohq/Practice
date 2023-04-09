"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Solve the problem in linear time and in O(1) space?
"""
import collections


# Trivial approach taking counter and getting most common element

def majority_element(nums):
    elem, count = collections.Counter(nums).most_common()[0]
    return elem


# This approach is better then previous and it stops . Space complexity is O(n) so unacceptable
def majorityElement2(nums):
    m = {}
    for n in nums:
        m[n] = m.get(n, 0) + 1
        if m[n] > len(nums) // 2:
            return n


# Approach first sorts the numbers and then returns the mid element which is always Nlogn time and Constant space
def majorityElement1(nums):
    nums.sort()
    return nums[len(nums) // 2]


def majorityElement(nums):
    # Boyer's Moore Algorithm --> O(1) Space, O(N) Time
    # video Link : https://www.youtube.com/watch?v=PqU48t80rn8&ab_channel=Fraz
    # We first assume that our first num is the majority element
    # So the count here is 1 as we have seen it 1 times, if the
    # count in the end is greater than 0 we are sure that this is majority element
    # as if you take count of majority element and subtract sum of all counts of non
    # Majority element, if that count is still positive that it proves that is
    # majority element. We do not need to check count in end over here as we are
    # sure that there exists a majority element.
    count = 1

    # Our Initial guess that this is the majority element
    result = nums[0]

    for num in nums[1:]:
        # If the next number is not same as prev
        # and count becomes 0 make this number as majority element and initialize
        # count to 1 again else just decrease the count
        if num != result:
            # decrease count by 1
            count -= 1
            # Make this element as majority element
            if count == 0:
                result = num
                count = 1
        else:
            # This is same element as previous one.
            count += 1

    return result

# Approach 3 could be to sort the given array and just return the n/2th element

if __name__ == "__main__":
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
