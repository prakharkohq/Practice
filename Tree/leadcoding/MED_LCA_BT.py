"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as th
e lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


LCA ki 3 conditions ho sakti hai

1 :  left child aur right child mein p aur q mil jaaye to in that case root is lca
2 :  if one of the element is found in the path then he himself is lca (which is the smallest condition reused to find)
     other lca's
3 :  if either left child is found or right child is found we can return basis there location
"""

def lca_myattempt(root, p , q):
    if root.val == p or root.val == q:
        return root

    # now check for left and right subtree's for there respective values
    left, right = None, None

    if root.left:
        left = lca_myattempt(root.left, p , q)
    if root.right:
        right = lca_myattempt(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right

# added comments and class structure for LC submission
def lowestCommonAncestor(self, root, p, q):
    # If looking for me, return myself
    if root == p or root == q:
        return root

    left = right = None
    # else look in left and right child
    if root.left:
        left = self.lowestCommonAncestor(root.left, p, q)
    if root.right:
        right = self.lowestCommonAncestor(root.right, p, q)

    # if both children returned a node, means
    # both p and q found so parent is LCA
    if left and right:
        return root
    else:
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way,
        # because in such scenarios, node where 'p' found is LCA
        return left or right