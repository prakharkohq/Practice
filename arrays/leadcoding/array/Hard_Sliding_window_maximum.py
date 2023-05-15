"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of
the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by
one position. Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
import collections
from _ast import List


class Solution:
  def maxSlidingWindow(self, nums, k: int):
    ans = []
    q = collections.deque()  # Max queue

    for i, num in enumerate(nums):
      # clean the queue
      while q and q[-1] < num:
        q.pop()
      q.append(num)
      if i >= k and nums[i - k] == q[0]:  # Out of bound
        q.popleft()
      if i >= k - 1:
        ans.append(q[0])

    return ans


class Solution:
  def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
      let, temp, count = s[0], '', 0
      for l in s:
        if let == l:
          count += 1
        else:
          temp += str(count) + let
          let = l
          count = 1
      temp += str(count) + let
      s = temp
    return s


if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(3322251))