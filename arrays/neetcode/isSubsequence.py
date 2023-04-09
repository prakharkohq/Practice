"""

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


from collections import deque


"""
MY Attempt
"""
def isSubsequence1(s: str, t: str) -> bool:
    orig = [ i for i in s ]
    target = [ i for i in t]
    if s == "":
        return True
    for item in target:
        if len(orig) > 0 and item == orig[0]:
            del(orig[0])

    if len(orig) == 0:
        return True

    return False


"""
Better Attempt 
Approach
In this solution, I begin with empty string sub = "" to put all subsequence of s that appear in t. 
and for every iteration in loop, I checked if every charcter in string t appear in string s and to check the
arrangement of appearing this character, I made this condition t[i] == s[len(sub)] to check if this character
appears in the correct location or not by len(sub) and if this condtion was true I added this character in string
sub. After all iterations in loop, I checked if sub == s , then s is subsequence of t otherwise s is not 
subsequence of t



"""


def isSubsequence(s, t):
    sub = ""
    for i in range(len(t)):
        if t[i] in s and t[i] == s[len(sub)]:
            sub += t[i]

    return sub == s


if __name__ == "__main__":
    print(isSubsequence("abc", "ahbgdc"))