"""
You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.
A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length to make s
balanced. If s is already balanced, return 0.

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER".

"""
import collections
def balancedString(self, s):
    count = collections.Counter(s)
    res = n = len(s)
    i = 0
    for j, c in enumerate(s):
        count[c] -= 1
        while i < n and all(n / 4 >= count[c] for c in 'QWER'):
            res = min(res, j - i + 1)
            count[s[i]] += 1
            i += 1
    return res