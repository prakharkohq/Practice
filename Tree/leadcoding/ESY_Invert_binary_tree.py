"""
Given the root of a binary tree, invert the tree, and return its root.
Problem : https://leetcode.com/problems/invert-binary-tree/

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

"""
from Tree.Node import TreeNode


def invert_tree(root):
    ## Accepted Solution
    if root is None:
        return
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

"""
Other solution 
"""
def invertTree(self, root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # Here assignment happens pos
        return root

def in_order_traversal(root):
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.right)


if __name__ == "__main__":
    node = TreeNode(5)
    node.insert(2)
    node.insert(3)
    node.insert(44)
    node.insert(15)
    invert_tree(node)
    in_order_traversal(node)
