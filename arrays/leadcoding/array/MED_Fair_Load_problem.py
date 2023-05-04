"""

"""
from typing import List


def shipWithinDays(self, weights, D):
    left, right = max(weights), sum(weights)
    while left < right:
        mid, need, cur = (left + right) / 2, 1, 0
        for w in weights:
            if cur + w > mid:
                need += 1
                cur = 0
            cur += w
        if need > D:
            left = mid + 1
        else:
            right = mid
    return left


"""
Explanation of this solution:

The key is left = max(weights), right = sum(weights),
which are the minimum and maximum possible weight capacity of the ship.

Therefore the question becomes Binary Search to find the minimum weight capacity of the ship between left and right.
We start from
mid = (left + right) / 2 as our current weight capacity of the ship.
need = days needed == 1
cur = current cargo in the ship == 0

Start put cargo into ship in order.
when need > D, it means the current ship is too small, we modify left = mid + 1 and continue
If all the cargo is successfully put into ships, we might have a chance to find a smaller ship, so let right = mid and continue.
Finally, when our left == right, we reach our answer



Time complexity: O(n * logSIZE), where SIZE is the size of the search space (sum of weights - max weight).


"""




def findDuplicate(nums: List[int]) -> int:
    slow = nums[nums[0]]
    fast = nums[nums[nums[0]]]

    while slow != fast:
      slow = nums[slow]
      fast = nums[nums[fast]]

    slow = nums[0]

    while slow != fast:
      slow = nums[slow]
      fast = nums[fast]

    return slow


if __name__ == "__main__":
    findDuplicate([1,3,4,2,2])