"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible
integer after removing k digits from num.



Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ## RC ##
        ## APPROACH : STACK ##
        ## IDEA : 1234, k= 2 => when numbers are in increasing order we need to delete last digits
        ## 4321 , k = 2 ==> when numbers are in decreasing order, we need to delete first digits
        ## so, we need to preserve increasing sequence and remove decreasing sequence ##
        ## LOGIC ##
        #	1. First think in terms of stack
        #	2. push num into stack IF num it is greater than top of stack
        #	3. ELSE pop all elements less than num

        ## TIME COMPLEXICITY : O(N)
        ## SPACE COMPLEXICITY : O(N)

        stack = []
        for n in num:
            while (stack and int(stack[-1]) > int(n) and k):
                stack.pop()
                k -= 1
            stack.append(str(n))

        # If no elements are removed, pop last elements, (increasing order)
        while (k):
            stack.pop()
            k -= 1

        # removing leading zeros
        i = 0
        while (i < len(stack) and stack[i] == "0"):
            i += 1

        return ''.join(stack[i:]) if (len(stack[i:]) > 0) else "0"
