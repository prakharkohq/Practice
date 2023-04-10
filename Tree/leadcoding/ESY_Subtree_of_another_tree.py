"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.
"""
from Tree.Node import TreeNode


# Complexity : O(ST)

def subtree_of_another_tree(root, subroot):
    def check_equal(r, s):
        # If Both are None return True
        if r is None and s is None:
            return True
        # If One is None it is false
        if (r is None) or (s is None):
            return False

        if r.data == s.data and check_equal(root.left, subroot.left) and check_equal(root.right, subroot.right):
            return True

    if subroot is None:
        return  # USING RETURN HERE AS IT COULD BE A SUBSTACK CALL , RETURN IS TO ABORT

    if check_equal(root, subroot):
        return True

    if subtree_of_another_tree(root.left, subroot) or subtree_of_another_tree(root.right, subroot):
        return True

    return False


"""
naive method converting a tree to a string and then checking the substring alot of problems with this approach
"""


def isSubtree(s, t):
    def convert(p):
        return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"

    return convert(t) in convert(s)


## LC Submitted Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Optional:
    pass


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(r, s):
            if (r is None) and (s is None):
                return True
            if (r is None) or (s is None):
                return False

            return ((r.val == s.val) and check(r.left, s.left) and check(r.right, s.right))

        if not subRoot:
            return

        if check(root, subRoot):
            return True

        if not root:
            return False

        if (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot)):
            return True

        return False


if __name__ == "__main__":
    node = TreeNode(5)
    node.insert(2)
    node.insert(3)
    node.insert(44)
    node.insert(15)