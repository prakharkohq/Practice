
# My Attempt
def remove_repeated_sorted_Array(nums):
    repeated, runner = 0, 1
    last_rep = -1
    while runner <= len(nums) - 1:
        if nums[runner] == nums[repeated] and nums[runner] > last_rep:
            repeated += 1
            runner += 1
        elif nums[runner] > last_rep:
            # SWAP IS UNNECESSARY BECAUSE WE CAN SIMPLY JUST COPY THE OLD VALUE
            last_rep = nums[runner]
            temp = nums[repeated]
            nums[repeated] = nums[runner]
            nums[runner] = temp
            repeated += 1
            runner += 1
        else:
            runner += 1

    nums = nums[0:repeated]
    return nums

# Solution using library
def remove_repeated_library(nums):
    nums[:] = sorted(set(nums))
    return len(nums)


# My Attempt 2 < After Solution USING INPLACE TRAVERSAL>
"""
Use a slow pointer to "lock" the "wanted" element, and use a fast pointer to move forward along the list and look for
 new unique elements in the list.
Or, in other words, the current slow pointer is used to locate the latest unique number for the results, and fast is 
used for iterating and discovery.

Have fast advanced in every iteration, but slow is only advanced when two pointers are onto two different elements.

That means, the elements after nums[slow] and before nums[fast] are numbers we've seen before and don't need anymore 
(one copy of these numbers is already saved before the current slow (inclusive)).

Therefore, in order to have this newly discovered (unseen) number pointed by the current fast to the front of the array 
for the final answer, we just need to swap this newly discovered number to the location that follows the current slow pointer, with one of the seen numbers (we don't need it for the answer regardlessly), and then advance the slow in the same iteration to lock this new number.
 # iterate fast in complete array and detect for two possibilites either two values can be same or different
        # if values are same only increase fast pointer(runner pointer) otherwise copy the fast value into slow+1
"""


def remove_repeated_sorted_array(nums):
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            nums[slow +1] = nums[fast]
            fast += 1
            slow += 1

    return slow + 1


if __name__ == "__main__":
    print("New Beginneing")
    nums = [1 ,1 ,2]
    print(remove_repeated_sorted_array(nums=nums))
    print(nums)
