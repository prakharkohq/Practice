"""
Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Naive apporach shall be using the counter

Bruteforce approach shall be to have a Counter over keys to have top frequent items arranged

"""
# Results are unordered because of the keys can be in any orders
from _ast import List
from collections import Counter
def top_k_frequent_items(arr, count):
    dict = Counter(arr)
    print(dict)
    results = list(dict.keys())
    print(results)
    return results[0:count]


"""
O(n) Solution 
"""

# bucket sort jaisa hai ye
def topKFrequent(nums, k):
    # For Input -> [1000,1000,1000,2,2,3]
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    # count --> {1000: 3, 2: 2, 3: 1}
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    # Freq --> [[], [3], [2], [1000], [], [], []]
    # ab bas reverse mein bucket khaali karte jaao right se left mein
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    # O(n)


if __name__ == "__main__":
    print("Top K frequent element")
    print(topKFrequent([1000,1000,1000,2,2,3], 3))