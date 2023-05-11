"""
Given a string s, partition s such that every substring of the partition is a palindrome .

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1

"""

class Solution:
  def minCut(self, s: str) -> int:
    n = len(s)
    cut = [0] * n
    # dp[i][j] , which is whether s[i..j] forms a pal [[True, True, False], [False, True, False], [False, False, True]] aab
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
      mini = i
      for j in range(i + 1):
        if s[j] == s[i] and (j + 1 > i - 1 or dp[j + 1][i - 1]):
          dp[j][i] = True
          mini = 0 if j == 0 else min(mini, cut[j - 1] + 1)
      cut[i] = mini

    return cut[n - 1]


if __name__ == "__main__":
  sol = Solution()
  print(sol.minCut("aab"))