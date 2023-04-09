"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Bruteforce Approach

O(n^3)
lets have 3 loop and check complexity one by one
i will start from 0 -> n-1
    j will start from i to n
        k will take sum of all i to j and compare it with max sum


O(n^2)

i will start from 0 > n-1
 j will start from i to n
    initialize sum = 0 aur jaise jaise j ko move karo us value ko badhate jaao jis se O(n^2) mein solution aa jaayega


Kadane algorithm jo ki O(N) mein karti hai ise solve :
Explanation : https://youtu.be/2MmGzdiKR9Y -> Back to Back SWE Channel

"""


class Solution:
    def maxContiguousSubarraySum(self, nums):
        '''
        :type nums: list of int
        :rtype: int
        '''

        """
        We default to say the the best maximum seen so far is the first
        element.

        We also default to say the the best max ending at the first element
        is...the first element.
        """
        max_so_far = nums[0]
        max_ending_here = nums[0]

        # We will investigate the rest of the items in the array from index 1 onward.
        for i in range(1, len(nums)):
            """
            We are inspecting the item at index i.

            We want to answer the question:
            "What is the Max Contiguous Subarray Sum we can achieve ending at index i?"

            We have 2 choices:

            maxEndingHere + nums[i] (extend the previous subarray best whatever it was)
              1.) Let the item we are sitting at contribute to this best max we achieved
              ending at index i - 1.

            nums[i] (start and end at this index)
              2.) Just take the item we are sitting at's value.

            The max of these 2 choices will be the best answer to the Max Contiguous
            Subarray Sum we can achieve for subarrays ending at index i.

            Example:

            index     0  1   2  3   4  5  6   7  8
            Input: [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
                     -2, 1, -2, 4,  3, 5, 6,  1, 5    'maxEndingHere' at each point

            The best subarrays we would take if we took them:
              ending at index 0: [ -2 ]           (snippet from index 0 to index 0)
              ending at index 1: [ 1 ]            (snippet from index 1 to index 1) [we just took the item at index 1]
              ending at index 2: [ 1, -3 ]        (snippet from index 1 to index 2)
              ending at index 3: [ 4 ]            (snippet from index 3 to index 3) [we just took the item at index 3]
              ending at index 4: [ 4, -1 ]        (snippet from index 3 to index 4)
              ending at index 5: [ 4, -1, 2 ]     (snippet from index 3 to index 5)
              ending at index 6: [ 4, -1, 2, 1 ]  (snippet from index 3 to index 6)
              ending at index 7: [ 4, -1, 2, 1, -5 ]    (snippet from index 3 to index 7)
              ending at index 8: [ 4, -1, 2, 1, -5, 4 ] (snippet from index 3 to index 8)

            Notice how we are changing the end bound by 1 everytime.
            """
            max_ending_here = max(max_ending_here + nums[i], nums[i])

            # Did we beat the 'maxSoFar' with the 'maxEndingHere'?
            max_so_far = max(max_ending_here, max_so_far)

        return max_so_far


def solution(nums):
    max_sum, curr_sum = nums[0], nums[0]

    for i in range(1, len(nums)):
        curr_sum += nums[i]
        decision_factor = max(curr_sum, nums[i])
        if decision_factor == nums[i]:
            curr_sum = nums[i]
        else:
            curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxContiguousSubarraySum([5,4,-1,7,8]))