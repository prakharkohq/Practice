"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of
all the values of the nodes in the tree.
"""

"""
TRAVERSE INORDER AND THEN RETURN THE KTH ELEMENT FROM THERE 
Possible downsides first i am traversing complete array and then i am returning kth element if for any big tree
results in wastage of resources 
"""
def solution_primitive(root, k):
    def in_order(root):
        return in_order(root.left) + [root.val] + in_order(root.right) if root else []

    in_order_list = in_order(root)
    return in_order_list[k-1]

# O(K) Solution
def solution_optimised(root, k):
    # iterative solution as we start traversal we can decide to return or not return that element
    if root:
        curr, stack = root, []
        stack.append(root)
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = root.right
