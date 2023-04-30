"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is
the number of 1's in the binary representation of i.
Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Explanation :
All whole numbers can be represented by 2N (even) and 2N+1 (odd).
For a given binary number, multiplying by 2 is the same as adding a zero at the end (just as we just add a zero when
multiplying by ten in base 10).
Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's. Likewise,
doubling a number and adding one will increase the count by exactly 1. Or:

countBits(N) = countBits(2N)
countBits(N)+1 = countBits(2N+1)
Thus we can see that any number will have the same bit count as half that number, with an extra one if it's an
odd number. We iterate through the range of numbers and calculate each bit count successively in this manner:


"""
from typing import List


def check_counters(n):
    for i in range(1, n):
        print(f"\n {i} --> {(i&1)}")

class Solution:
  def countBits(self, n: int) -> List[int]:
    # Let f(i) := i's # Of 1's in bitmask
    # f(i) = f(i / 2) + i % 2
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
      ans[i] = ans[i // 2] + (i & 1)  # Bitwise and --> ( i & 1 ) which produces 

    return ans



if __name__ == "__main__":
    sol = Solution()
    print(check_counters(20))
    print(sol.countBits(5))