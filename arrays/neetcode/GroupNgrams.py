"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""
from collections import defaultdict

"""
My Approacch for 
"""


def group_anagrams(arr):
    # Find the numerical associativity of a string
    data_dict = {}
    for item in arr:
        count = ''.join(sorted(item))
        if count in data_dict.keys():
            lst = data_dict[count]
            lst.append(item)
        else:
            lst = list()
            lst.append(item)
            data_dict[count] = lst

    return list(data_dict.values())

"""
What this solution has better is 
we are using a default dict causing unnecessary check for matching string before entering 
"""
def group_anagrams_soln(strs):
    cnt = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        cnt[key].append(word)

    return list(cnt.values())


if __name__ == "__main__":
    results = group_anagrams(["duh","ill","eat","tea","tan","ate","nat","bat"])
    print(results)