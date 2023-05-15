"""
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the
right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
"""


def countSmaller(self, nums) :
    res = [0] * len(nums)  # NOTE 1
    enum = list(enumerate(nums))  # NOTE 2
    """
    we initialize another list of tuple to have each tuple stores the index and value as (index, nums[index]). This 
    list serves as the bridge to link the array element which is under the sorting process to the result list
     initialized in NOTE 1
    """
    self.mergeSort(enum, 0, len(nums) - 1, res)
    return res


def mergeSort(self, enum, start, end, res):
    if start >= end: return

    mid = start + (end - start) // 2
    self.mergeSort(enum, start, mid, res)
    self.mergeSort(enum, mid + 1, end, res)
    self.merge(enum, start, mid, end, res)


def merge (enum, start, mid, end, res):
    p, q = start, mid + 1
    inversion_count = 0  # NOTE 3
    #  we create a variable to count the how many numbers from the right half is smaller than the current number
    #  from the left half.
    temp = []

    while p <= mid and q <= end:
        if enum[p][1] <= enum[q][1]:
            temp.append(enum[p])
            res[enum[p][0]] += inversion_count  # NOTE 5
            """
            when we first find a number from the right half that is bigger than the current left number, 
            we know that there will not be any number from the right half to be smaller than this current left number. 
            Thus we add this inversion_count to the final result through the bridge of enum list.
            """
            p += 1
        else:
            temp.append(enum[q])
            inversion_count += 1  # NOTE 4
            """
            when we find that nums[left_index] > nums[right_index], we add 1 to the inversion_count,
            but we dont add the current inversion_count to the final result yet. Because it is still possible that the 
            next number(s) in the right half is still smaller than this current left number.
            """
            q += 1

    while p <= mid:
        temp.append(enum[p])
        res[enum[p][0]] += inversion_count  # NOTE 6
        """
        when we finish iterating the numbers in the right half but there are still numbers left in the left half, we 
        know that the number in the remaining left half should be bigger than all numbers in the right half, thus we 
        need to add the current inversion_count to the corresponding index of all remaining left numbers. To help you 
        understand this better, you can also use end-mid which gives the length of the right half array instead of 
        inversion_count in this step.
        """
        p += 1

    while q <= end:
        temp.append(enum[q])
        q += 1

    enum[start:end + 1] = temp  # NOTE 7
    """
    we swap the start to end segement from the enum list with the sorted segement,
     to ensure the merge() function in the next level is also dealing with a sorted array.
    
    Time complexity: O(nlogn). This is the same as conventional merge sort. 
    Space complexity: O(n). This comes from the temp list that we initialized to temporarily store the sorted array segment.



    """