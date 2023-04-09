"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
import collections


def isAnagram(s, t):
    s_sorted = ''.join(sorted(s, key=str.lower))
    t_sorted = ''.join(sorted(t, key=str.lower))
    if s_sorted == t_sorted:
        return True
    return False

"""
Better solution will consume very less memory
"""


def isAnagram1( s, t):
    print(collections.Counter(s))
    return collections.Counter(s) == collections.Counter(t)

if __name__ == "__main__":
    print(isAnagram1("rat", "tar"))
