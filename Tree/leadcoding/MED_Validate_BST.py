"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.

The right subtree of a node contains only nodes with keys greater than the node's key.

Both the left and right subtrees must also be binary search trees.

"""


def isValidBST(root) -> bool:
    if root is None:
        return False

    def rec(root, left, right):
        # if root is None:
        #     return True  --> Do Not write conditions like this because this disturbs the flow for recursive calls
        # Convert this call to a if stmt
        if root:
            if root.val <= left or root.val >= right:
                return False
            return rec(root.left, left, root.val) and rec(root.right, root.val, right)

        return True # default case


    return rec(root, -float('inf'), -float('inf'))


def recursive(self, root):
    def rec(node, left, right):
        if node:
            if node.val <= left or node.val >= right: return False
            return rec(node.left, left, node.val) and rec(node.right, node.val, right)
        return True

    return rec(root, -float('inf'), float('inf'))