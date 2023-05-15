"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


https://www.youtube.com/watch?v=s7AvT7cGdSo
Complexity analysis : https://leetcode.com/problems/permutations/solutions/993970/python-4-approaches-visuals-time-complexity-analysis/

Strucutre

nums[0] : [1,2,3] -> [2,3],[3,2] -> [1,2,3],[3,2,1]
nums[1] : [2,3,1] -> [3,1],[1,3] -> [3,1,2],[1,3,2]
nums[2] : [3,1,2] -> [1,2],[2,1] ->

Recursion likhne ka tarika ye hai ki sabse pehle ek sabse chota sa case utha lo aur uske hisab se likhte chale jaao
aage tak jaise [2,3] -> [3,2] [2,3] kaise aayenge

Another way of looking at is we know from set theory that there are N! permutations of a list of size N.
We also know that the permutations are going to be the leaves of the Tree,
which means we will have N! leaves. In order to get to each one of those leaves, we had to go through N calls.
That's O(N*N!). Again a little more than the total number of nodes because some nodes are shared among more than one path.

Space: O(N!)

Because you still need to store the permutations and there are N! of them even if the depth of the stack is maxed out
at N+1 (depth of the recursion space-Tree is also N+1)

"""


def permute_attempt(nums):
    result = [] # isi array mein har final recursive call ka response add karte chalenge hum log

    #base condition
    if len(nums) == 0:
        return [nums[:]] # yaha pr nums ki ek copy bana ke bhej di kyoki agar nums bhej denge to usi array pr hum modification
                         # karte hai aur us se hame nuksaan hoga values mixed ho jaayengi

    for i in nums:  # ye number of times process ko repeat karne ke lie jite bhi elements each level pr hai
        n = nums.pop(0) #Head nikal lia list ka baaki ki permute karne bhej di reverse hoke aayegi
        perms = permute_attempt(nums)

        for perm in perms:
            perm.append(n) # Saare permutation mein last postfix number add kar do

        result.extend(perms)
        nums.append(n)

    return result


def permute(nums):
    result = []
    # base condition
    if len(nums) == 1:
        return [nums[:]] #when using line[:], it means you clone a new list line and append it to res.

    for i in range(len(nums)):
        n = nums.pop(0)  #removing first element from the array call
        perms = permute(nums)

        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)
    return result

class Solution:
  def permute(self, nums) :
    ans = []
    used = [False] * len(nums)

    def dfs(path) -> None:
      if len(path) == len(nums):
        ans.append(path.copy())
        return

      for i, num in enumerate(nums):
        if used[i]:
          continue
        used[i] = True
        path.append(num)
        dfs(path)
        path.pop()
        used[i] = False

    dfs([])
    return ans


if __name__ == "__main__":
    #print(permute_attempt([1,2,3]))
    sol = Solution()
    print(sol.permute([1,1,2]))

