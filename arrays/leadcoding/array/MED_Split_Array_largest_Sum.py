"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of
any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.



Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
"""
import functools
import itertools
import math
from _ast import List

from collections import defaultdict

#
class Solution_Bruteforce(object):
    def helper(self, nums, m):
        if nums == []:
            return 0
        elif m == 1:
            return sum(nums)
        else:
            min_result = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[:j]), self.helper(nums[j:], m - 1)
                min_result = min(min_result, max(left, right))
            return min_result

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        return self.helper(nums, m)

# Memoization
class Solution_memo(object):
    def helper(self, i, nums, m, cache):
        if i == len(nums):
            return 0
        elif m == 1:
            return sum(nums[i:])
        else:
            if i in cache and m in cache[i]:
                return cache[i][m]
            cache[i][m] = float('inf')
            for j in range(1, len(nums) + 1):
                left, right = sum(nums[i:i + j]), self.helper(i + j, nums, m - 1, cache)
                cache[i][m] = min(cache[i][m], max(left, right))
                if left > right:
                    break
            return cache[i][m]

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        cache = defaultdict(dict)
        return self.helper(0, nums, m, cache)



class Solution:
    # top down
    def splitArray_top_down(self, nums, m: int) -> int:
        n = len(nums)
        prefix = [0] + list(itertools.accumulate(nums))

        # dp(i, k) := min of largest sum to split first i nums into k groups
        @functools.lru_cache(None)
        def dp(i: int, k: int) -> int:
            if k == 1:
                return prefix[i]

            ans = math.inf

            # Try all possible partitions
            for j in range(k - 1, i):
                ans = min(ans, max(dp(j, k - 1), prefix[i] - prefix[j]))

            return ans

        return dp(n, m)
    #bottom up
    def splitArray(self, nums, m: int) -> int:
        n = len(nums)
        # dp[i][k] := min of largest sum to split first i nums into k groups
        # [7,2,5,10,8], m = 2
        dp = [[math.inf] * (m + 1) for _ in range(n + 1)]
        prefix = [0] + list(itertools.accumulate(nums))
        # [[inf, inf, inf], [inf, 7, inf], [inf, 9, inf], [inf, 14, inf], [inf, 24, inf], [inf, 32, inf]]
        for i in range(1, n + 1):
            dp[i][1] = prefix[i]

        for k in range(2, m + 1):
            for i in range(k, n + 1):
                for j in range(k - 1, i):
                    dp[i][k] = min(dp[i][k], max(dp[j][k - 1], prefix[i] - prefix[j]))
        # [[inf, inf, inf], [inf, 7, inf], [inf, 9, 7], [inf, 14, 7], [inf, 24, 14], [inf, 32, 18]]
        return dp[n][m]


if __name__ == "__main__":
    sol = Solution_memo()
    print(sol.splitArray(nums=[7,2,5,10,8], m = 2))


