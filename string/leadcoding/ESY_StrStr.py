"""
Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1
if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


def solution(haystack, needle):
    # If needle is equal to haystack noway there can be a substring
    if needle == haystack:
        return 0
    i, j = 0, len(needle)
    while j <= len(haystack):
        current_needle = haystack[i:j] # Python Beauty
        if current_needle == needle:
            return i
        i += 1
        j += 1
    return -1



if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    print(solution(haystack, needle))