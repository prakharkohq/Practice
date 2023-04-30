"""
Given a string s, find the length of the longest  substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.a

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        """
        This is a sliding window technique where we just want to findout the maximum window of unseen characters from 
        left and right and at each iteration we are removing 
        """
        for r in range(len(s)):
            while s[r] in charSet:  # Yaha tak ke jitne repeated character they before this repating one sabko hata dena hai
                # which ideally means yaha tak ki sliding window ki length record ho gayi we will recreate our sliding window
                # so need not carrying this baggage with us
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res



if __name__ == "__main__":
    solution = Solution()
    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))