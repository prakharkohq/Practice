"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""



"""
Approach 1:
In this question, we need need to return the count of subarray that equals K.
What we can do is generate all the possible subarray(which will takes O(n^2)) and than we can run another loop within 
that to find out the sum (O(n) time complexity). If the sum mathces the K , than BINGO we found one occurance. 
In total , the overall complexity is O(n^3) which is bad specially when you have huge data points.
We will quickly go for pseudo code :

for(i=start to end)
   for(j=start+1 to end)
       for(i to j)
	       check the total sum and compare with against K
"""
def solution(nums, k):
    result = 0
    for index, item in enumerate(nums):
        curr_sum = 0
        temp_index = index
        while temp_index < len(nums) and curr_sum <= k+1:
            curr_sum += nums[temp_index]
            if curr_sum == k:
                result+=1
                break
            temp_index += 1
    return result


def subarraySum(nums, k):
    d = {
        0: 1}  # key-value pair of (0, 1), where 0 is the sum of the empty subarray and 1 is the frequency of the empty subarray
    count = 0  # initialize count of subarrays whose sum equals k to 0
    sum_so_far = 0  # initialize sum_so_far to 0

    for num in nums:
        sum_so_far += num  # update the sum_so_far by adding num to it
        diff = sum_so_far - k  # compute the difference between the sum_so_far and k

        if diff in d:  # if diff is in the dictionary d, increment the count by the value of d[diff]
            count += d[diff]

        if sum_so_far in d:  # if sum_so_far is in the dictionary d, increment its value by 1, otherwise
                             # add a new key-value pair to d
            d[sum_so_far] += 1
        else:
            d[sum_so_far] = 1

    return count  # return the count of subarrays whose sum equals k


if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    print(subarraySum(nums, k=6))