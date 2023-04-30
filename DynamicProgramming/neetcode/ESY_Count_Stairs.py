"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution(object):
    def climbStairs(self, n):
        # We will use bottom up approach to solve this problem starting from the last step calculating back to the
        # first step imagine we have 5 as n we will calculate from very last node
        #     0   1   2   3   4  5  --> Steps
        #     8   5   3   2   1  1  --> Ways to reach 5 from given number
        n1 , n2 = 1, 1
        for i in range(n-1):
            temp = n1+n2
            n2 = n1
            n1 = temp
        return n1

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(5))
