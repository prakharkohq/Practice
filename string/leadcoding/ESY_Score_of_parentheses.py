"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
"""


def scoreOfParentheses( S):
    res, i = [0] * 30, 0
    for c in S:
        i += 1 if c == '(' else -1
        res[i] = res[i] + max(res[i + 1] * 2, 1) if c == ')' else 0
    return res[0]


def right_Shift_test():
    for i in range(1,10):
        print(i<<1)


print(right_Shift_test())