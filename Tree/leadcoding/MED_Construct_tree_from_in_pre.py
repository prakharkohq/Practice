"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is
the inorder traversal of the same tree, construct and return the binary tree.

Inspiration of solution
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/34579/python-short-recursive-solution/

Solution is recursive where we will divide the problem at each stage by basic optimisations
"""
from Tree.Node import TreeNode


def solution(preorder, inorder):
    # first node in preorder is always root
    # making base condition as validation becoz we are trimming the inorder at every call
    if inorder:
         ind = inorder.index(preorder.pop(0))
         root = TreeNode(inorder[ind])
         # we will divide the inorder as that had root in middle
         root.left = solution(preorder, inorder[0:ind])
         root.right = solution(preorder, inorder[ind+1:])
         return root


