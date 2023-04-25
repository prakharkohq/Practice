"""
Binary Subarrays With Sum
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.
Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15


Solution 1: HashMap
Count the occurrence of all prefix sum.

I didn't notice that the array contains only 0 and 1,
so this solution also works if have negatives.

Space O(N)
Time O(N)

Solution 2: Sliding Window


"""
import collections


"""
 count[i] represents how many start-from-index-zero (prefix) sub array that sums to i.
So when psum >= S happens, for current index i, 
what we are looking for is the number of sub array that sums to S (from 0 to i), not to psum.
But, the number of sub array that sums to S equals to the number of sub array that sums to psum - S.
Because after we extract all sub arrays that sum to psum - S from current array (0 ~ i), what is left is all 
sub arrays that sum to S, which means we only need to accumulate count[psum - S]. And of course count[psum - S] is
 something we have calculated before. Basically, it feels like we are keep cutting the prefix sub array out of the 
 whole array we've traversed so far to get the sub array that sums to S, and prefix sub array just keeps growing longer and longer.
Please note that count[i] is not the answer for S=i, it's only the answer for S=i AND BEFORE i grows to S + 1, and 
more important, sub array is continuous, and sub sequence is not.
"""

def numSubarraysWithSum1(A, S):
    c = collections.Counter({0: 1})
    psum = res = 0
    for i in A:
        psum += i
        res += c[psum - S]
        c[psum] += 1
    return res


"""
atMost(A, S) counts the number of the subarrays of A the sum of which is at most(less than or equal to) S. Therefore, 
we can use atMost(A, S) - atMost(A, S - 1) to get the number of the subarrays the sum of which is exactly S.
In the atMost function, the i to j window represents the subarrays. We use the j pointer to expand the window, 
when the sum of all numbers in the window is bigger than S, it's time for us to move the i pointer to shorten the 
window. Through this process, we can count the number of the subarrays.
"""

def numSubarraysWithSum( A, S):
    def atMost(S):
        if S < 0: return 0
        res = i = 0
        for j in range(len(A)):
            S -= A[j]
            while S < 0:
                S += A[i]
                i += 1
            res += j - i + 1
        return res

    return atMost(S) - atMost(S - 1)

if __name__ == "__main__":
    print(numSubarraysWithSum1([1,0,1,0,1], 2))