"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each
character in this substring is greater than or equal to k.
Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


If every character appears at least k times, the whole string is ok. Otherwise split by a least frequent character
(because it will always be too infrequent and thus can't be part of any ok substring) and make the most out of the splits.

"""


def longestSubstring(s, k):
    if len(s) < k:
        return 0
    c = min(set(s), key=s.count)
    if s.count(c) >= k:
        return len(s)
    return max(longestSubstring(t, k) for t in s.split(c))


if __name__ == "__main__":
    print(longestSubstring("aaabb", 3))