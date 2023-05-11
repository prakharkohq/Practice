"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a
valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
"""
import functools


class Solution:
  def wordBreak(self, s, wordDict):
    wordSet = set(wordDict)

    @functools.lru_cache(None)
    def wordBreak(s: str) :
      ans = []

      # 1 <= len(prefix) < len(s)
      for i in range(1, len(s)):
        prefix = s[0:i]
        suffix = s[i:]
        if prefix in wordSet:
          for word in wordBreak(suffix):
            ans.append(prefix + ' ' + word)

      # Contains whole string, so don't add any space
      if s in wordSet:
        ans.append(s)

      return ans

    return wordBreak(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"] ) )