"""
Given a string s, partition s such that every substring of the partition is a palindrome . Return all possible
palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]

"""

class Solution:
  def partition(self, s: str) :
    ans = []

    def isPalindrome(s: str) -> bool:
      return s == s[::-1]

    def dfs(s: str, j: int, path, ans ) -> None:
      if j == len(s):
        ans.append(path)
        return

      for i in range(j, len(s)):
        if isPalindrome(s[j: i + 1]):
          dfs(s, i + 1, path + [s[j: i + 1]], ans)

    dfs(s, 0, [], ans)
    return ans


class Solution:
  def partition(self, s: str) :
    ans = []

    def isPalindrome(s: str) -> bool:
      return s == s[::-1]

    def dfs(s: str, j: int, path, ans) -> None:
      if j == len(s):
        ans.append(path)
        return

      for i in range(j, len(s)):
        if isPalindrome(s[j: i + 1]):
          dfs(s, i + 1, path + [s[j: i + 1]], ans)

    dfs(s, 0, [], ans)
    return ans


"""

The number of possible partitions is O(2^N). considering a string of n same chars, like, 'aaaaaa...', the number of 
possible partitions is the sum of (choose 0 from n-1), (1 from n-1), (n from n-1)... (n-1 from n-1) == 2^(n-1).
Therefore.... the time complexity cannot be better than O(2^N)... My guess is something like O(N*2^N),
like checking each substring may take O(N) on average? Not sure though.

"""