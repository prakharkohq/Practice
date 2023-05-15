"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped
by mistake. Recover the tree without changing its structure.

"""
"""
    Brute force kind of thing
    -> Inorder Traversal returns sorted array
    -> find a swap btwn numbers to make sorted
    Make single swap to make array sorted
"""
from typing import Optional

from Tree.Node import TreeNode


class Solution:
  def recoverTree(self, root: Optional[TreeNode]) -> None:
    pred = None
    x = None  # 1st wrong node
    y = None  # 2nd wrong node

    def swap(x: Optional[TreeNode], y: Optional[TreeNode]) -> None:
      temp = x.val
      x.val = y.val
      y.val = temp

    def inorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      inorder(root.left)

      if self.pred and root.val < self.pred.val:
        self.y = root
        # If first element has not been found, assign it to prevElement (refer to 6 in the example above)

        if not self.x:
          self.x = self.pred
        else:
          return
      self.pred = root

      inorder(root.right)

    inorder(root)
    swap(self.x, self.y)

