"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in
the array if you can flip at most k 0's.


Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Long story short: i, j is like a moving "memory" sliding frame. (Note: i, j definity NOT the exact index for the
largest range!) Whenever there's a better choice, the span of the frame will fit for the larger range. So you can
directly return the final span/length of the frame as the final output.

More detailed version: as you can see from the code, j is constantly moving right. K here can be considered as the
remaining feasible amount of flips, and reflects the current range (i.e., from i to j). When K<0, it's not a feasible
solution and when K>=0, it'll be a feasible solution. If currently range is not yet a feasible solution or better than
current "memory" frame (i.e., K<0 judgement) , i will try follow up the j and j-i (the frame size) remains unchanged,
keeping the current maximum size intact. Whenever the flip count K of current range (i.e., still i to j) is greater or
equals to 0, it means we can possibly expand our frame, and that's exactly what the code does. (i remains unchanged
since it will not goes into K<0 clauses, and j keeps moving when K>=0). Eventually, when j comes to the end, the
"memory" frame will automatically (by design of course) give us the maximum range throughout the array.
"""


def longestOnes(self, A, K):
    i = 0
    for j in range(len(A)):
        K -= 1 - A[j]
        if K < 0:
            K += 1 - A[i]
            i += 1
    return j - i + 1