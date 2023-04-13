"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


# Approach 1 : Convert tree to string O(N) Traversal and decide

# Approach 2 : Recursive calls tp check at each level whether tree is same or not

# approach 2
class Solution:
    def isSameTree(self, p, q):
        if p and q:
            return (p.val == q.val) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
        return p is q
        # Just for accuracy. (p is q) checks if p and q reference to the same object. In this case, if both p and q
        # reference to None, then it is the same object so will return True, else False. It handles the part where p
        # or q isn't exist so isn't handled by the first condition.

# return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
class Solution:
    def isSameTree(self, p1, q):
        def convert(p):
            return "^"+ str(p.val)+ "#" + convert(p.left) + convert(p.right) if p else "$"
        return convert(p1) == convert(q)