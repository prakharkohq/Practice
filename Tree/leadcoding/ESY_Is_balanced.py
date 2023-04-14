"""
Given a binary tree, determine if it is
height-balanced
.
"""

class Solution:
    def isBalanced(self, root) -> bool:
        self.isBalanced = True

        def check(root):
            if root is None : return 0

            left, right = check(root.left), check(root.right)

            if abs(left-right) > 1:
                self.isBalanced = False

            return max(left, right) + 1

        check(root)

        return self.isBalanced