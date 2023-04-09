"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""

# Bruteforce solution Will only pass limited testcases as this solution can not scale
def solution(nums):
    solution = []
    for i in range(0, len(nums)-2):
        for j in range(i, len(nums)-1):
            for k in range(j, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and i != j != k:
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.append(nums[k])
                    temp = sorted(temp)
                    if temp not in solution:
                        solution.append(temp)
    return solution

# Best Solution https://leetcode.com/problems/3sum/solutions/725950/python-5-easy-steps-beats-97-4-annotated/
"""

apni problem ko 5 steps mein tod lete hai pehle steps

step 1 : Negative positive alag alag set mein aur zero ko alag list mein daalo
Step 2 : teen cases agar ek bhi zero hai to positive negative ka ek pair dhundho
step 3 : agar zero ke teen count hai to triplet possible ahi aur uske aage agar hoga to us mein repetition hoga so leave
step 4 : kinhi 2 negative number ka sum agar positive number ke barabar aa jaaye dusre array mein to solved
step 5 : kinhi 2 positive number ka sum agar negative number ke barabar aa jaaye dusre array mein to solved

Note : always insert triplets sorted in set to avoid repetation 

"""

def solution_3Sum(nums):
    # Step 1
    n, p, z = list(), list(), list()
    result = set()
    for item in nums:
        if item > 0:
            p.append(item)
        elif item < 0:
            n.append(item)
        else:
            z.append(item)
    N, P = set(n), set(p)
    # Step 2
    if z:
        for item in p:
            if item*-1 in N:
                result.add((item*-1, 0, item))

    # Step 3
    if len(z) >= 3:
        result.add((0, 0, 0))

    # Step 4
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            target = n[i]+n[j]
            target *= -1
            if target in P:
                result.add(tuple(sorted([n[i], n[j], target])))

    # Step 5
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            target = p[i]+p[j]
            target *= -1
            if target in N:
                result.add(tuple(sorted([p[i], p[j], target])))

    return result

#Editoralist : 5120766
if __name__ == "__main__":
    print(solution_3Sum([-1,0,1,2,-1,-4]))