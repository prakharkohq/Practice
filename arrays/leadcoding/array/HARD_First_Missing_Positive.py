
def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within
         the range [1,...,l+1]
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)):  # delete those useless elements
        if nums[i] <0 or nums[i ] >= n:
            nums[i ] =0
    for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
        nums[nums[i] % n] += n
    for i in range(1 ,len(nums)):
        if nums[i ] / n == 0:
            return i
    return n



def letterCombinations(digits: str):
    if not digits:
      return []

    ans = ['']
    digitToLetters = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    for d in digits:
      temp = []
      for s in ans:
        for c in digitToLetters[ord(d) - ord('0')]:
          temp.append(s + c)
      ans = temp

    return ans


if __name__ == "__main__":
    print(letterCombinations("23"))