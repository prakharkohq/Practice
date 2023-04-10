"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

"""
from Tree.Node import TreeNode
"""
By definition diameter is longest distance between leaf nodes so we can assume to include root or reject root
"""


def diameter_of_tree(root):
    # if we notice properly this function executes each block again and again causing it to run (N + N + N +N ) -> O(N^2)
    if root is None:
        return 0
    d_left = diameter_of_tree(root.left)
    d_right = diameter_of_tree(root.right)
    cr = 1 + height_of_Tree(root.left) + height_of_Tree(root.right)

    return max(cr, max(d_left, d_right))


def height_of_Tree(root):
    if root is None:
        return 0
    return 1 + max(height_of_Tree(root.left), height_of_Tree(root.right))

    # Just take a variable which will keep in check the maximum height seen by the node which shall be a global variabl
    # O(N) Code will look like this


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0

        def height(p):
            if not p: return 0
            left, right = height(p.left), height(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        height(root)
        return self.ans



if __name__ == "__main__":
    node = TreeNode(1)
    node.insert(2)
    node.insert(3)
    node.insert(4)
    node.insert(5)
    sol = Solution()
    print(sol.diameterOfBinaryTree(node))
