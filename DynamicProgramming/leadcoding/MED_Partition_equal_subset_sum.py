"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
elements in both subsets is equal or false otherwise.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

"""

This problem is essentially let us to find whether there are several numbers in a set which are able to sum to a
specific value (in this problem, the value is sum/2).

Actually, this is a 0/1 knapsack problem, for each number, we can pick it or not. Let us assume dp[i][j] means whether
the specific sum j can be gotten from the first i numbers. If we can pick such a series of numbers from 0-i whose sum 
is j, dp[i][j] is true, otherwise it is false.

Base case: dp[0][0] is true; (zero number consists of sum 0 is true)

Transition function: For each number, if we don't pick it, dp[i][j] = dp[i-1][j], which means if the first i-1 elements 
has made it to j, dp[i][j] would also make it to j (we can just ignore nums[i]).
If we pick nums[i]. dp[i][j] = dp[i-1][j-nums[i]], which represents that j is composed of the current value nums[i] 
and the remaining composed of other previous numbers.
Thus, the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]


public boolean canPartition(int[] nums) {
    int sum = 0;
    
    for (int num : nums) {
        sum += num;
    }
    
    if ((sum & 1) == 1) {
        return false;
    }
    sum /= 2;

    int n = nums.length;
    boolean[][] dp = new boolean[n+1][sum+1];
    for (int i = 0; i < dp.length; i++) {
        Arrays.fill(dp[i], false);
    }
    
    dp[0][0] = true;
    
    for (int i = 1; i < n+1; i++) {
        dp[i][0] = true;
    }
    for (int j = 1; j < sum+1; j++) {
        dp[0][j] = false;
    }
    
    for (int i = 1; i < n+1; i++) {
        for (int j = 1; j < sum+1; j++) {
            dp[i][j] = dp[i-1][j];
            if (j >= nums[i-1]) {
                dp[i][j] = (dp[i][j] || dp[i-1][j-nums[i-1]]);
            }
        }
    }
   
    return dp[n][sum];
}
"""


class Solution:
  def canPartition(self, nums) -> bool:
    summ = sum(nums)
    if summ & 1:
      return False
    return self.knapsack_(nums, summ // 2)

  def knapsack_(self, nums, subsetSum: int) -> bool:
    n = len(nums)
    # dp[i][j] := True if j can be formed by nums[0..i)
    dp = [[False] * (subsetSum + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
      num = nums[i - 1]
      for j in range(subsetSum + 1):
        if j < num:
          dp[i][j] = dp[i - 1][j]
        else:
          dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]

    return dp[n][subsetSum]


if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartition(nums=[1,5,11,5]))
