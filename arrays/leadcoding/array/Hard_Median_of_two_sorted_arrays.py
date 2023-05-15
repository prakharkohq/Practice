"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

O(log (m+n)) Time complexity
"""

class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            """
            Simply because the sub function kth is getting the element at index k in his context, 
            which would be the k+1-th small element in A+B. You can see it from when l = len(A)+len(B) is odd, 
            he is getting the element at index l/2.
            """
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]
        """"
        Some notes from my understanding, please feel free to correct me.

ia, ib = len(a) / 2 , len(b) / 2
a[ia] = ma, b[ib] = mb
supposed all the elements that are at left of ma are la, right of ma are ra , same for lb, rb

if ia + ib < k: means the k-th element still exist in some larger part of the array
if ma < mb => la < ma < mb: solution can't exist in la
if ma > mb => lb < mb < ma: solution can't exist in lb
since we are deleted some smaller part, original we are seeking for the k-th, now we are seeking for the
 k- (len(smaller part)) th in the remaining two array
if ia + ib > k: means the k-th element still exist in some smaller part of the array
if ma < mb => ma < mb < rb: solution can't exist in rb
if ma > mb => mb < ma < ra: solution can't exist in la
since we are deleted some larger part, we are still finding the k-th element in the array
So personally I don't think the two indexing part you mentioned are supposed to ensure the recursion terminate. 
It's simply how the algorithm goes.
        """
        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays(A = [1,2,3], B=[4,5]))