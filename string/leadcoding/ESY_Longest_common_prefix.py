"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


def solution(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if len(s) == i or s[i] != strs[0][i]:
                return res
        res += strs[0][i]

    return res


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(solution(strs))