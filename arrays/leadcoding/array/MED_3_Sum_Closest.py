"""
Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""


"""
3 Sum ko karne ke lie ya to usko sort kar dena chaahiye ya segregation waala clean method use karna chaahiye to 
decrease the time complexity yaha pr pehle sort karne mein O(nlogn + n2)

n^3 ko n^2 mein badal ne ke lie isme sabse pehle sort kar lia aur 2 pointer use kar ke o(N) mein le aaye isko 

Python O(N^2) solution

thoda memorize karne waala solutions
"""


def solution(num, target):
    # check solution as such first sort the array
    num.sort()
    result = num[0] + num[1] + num[2]   # sabse pehle teeno ko sum kar lo
    # loop chalate hai saare elements pr 1 se leke ant tak ke
    # i ke aage ek value set karo j pr aur peeche se last value k jis se double pointer ban jaayega
    for i in range(len(num) - 2):
        j, k = i+1, len(num) - 1
        sum = num[i] + num[j] + num[k]
        if sum == target:
            return sum # sabse seedha case aur saare cases ka baap return result wo aakhri case hai

        # kyoki cheeze sorted hai to hum yaha pr abosulute difference dekhenge sum aur result ka target se jo jyada paas
        # hoga us par hum correct value ko assign kar denge
        val_left  = abs(sum - target)
        val_right =  abs(result - target)
        if abs(sum - target) < abs(result-target):
            result = sum
        if sum < target:
            j += 1
        if sum > target:
            k -= 1

    return result


if __name__ == "__main__":
    print(solution([-1,2,1,-4], 1))


