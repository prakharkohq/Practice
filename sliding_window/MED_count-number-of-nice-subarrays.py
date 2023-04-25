"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.



Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Replace even elements with 0 and odd elements with 1.
The problem is then reduced to the number of subarrays with sum k.

class Solution {
public:
    int numberOfSubarrays(vector<int>& a, int k) {
        for(int &x:a)
            x=x%2;
        unordered_map <int,int> mp;
        mp[0]=1;
        int csum=0;
        int ans=0;
        for(int i=0;i<a.size();i++){
            csum+=a[i];
            if(mp.count(csum-k))
                ans+=mp[csum-k];
            mp[csum]++;
        }
        return ans;
    }
};
"""


def solution(nums, k):
    runsum, ans = 0, 0
    sumdict = {0: 1}
    for num in nums:
        runsum += num % 2
        if runsum - k in sumdict:
            ans += sumdict[runsum - k]
        sumdict[runsum] = sumdict.get(runsum, 0) + 1
    return ans

def subarraySum(nums, k: int) -> int:
    result = 0
    for index, item in enumerate(nums):
        curr_sum = 0
        temp_index = index
        while temp_index < len(nums) and curr_sum < k + 1:
            curr_sum += nums[temp_index]
            if curr_sum == k:
                result += 1
                break
            temp_index += 1
    return result
