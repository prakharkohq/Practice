"""
Range Sum of BST
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with
a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

One way to solve this problem is just iterate over our tree and for each element check if it is range or not. However
here we are given, that out tree is BST, that is left subtree is always lesser than node lesser than right subtree. So,
let us modify classical dfs a bit, where we traverse only nodes we need:

Check value node.val and if it is in our range, add it to global sum.
We need to visit left subtree only if node.val > low, that is if node.val < low, it means, that all nodes in left
subtree less than node.val, that is less than low as well.
Similarly, we visit right subtree only if node.val < high.
Complexity: time complexity is O(n), where n is nubmer of nodes in our tree, space complexity potentially O(n) as well.
We can impove our estimations a bit and say, that time and space is O(m), where m is number of nodes in our answer.
"""
from Tree.Node import TreeNode


class solution:
    def __init__(self):
        self.ans = 0

    def range_bst(self, root, l, h):
        self.ans = 0

        def bfs(root):
            if root is None:
                return
            if l <= root.data <= h:
                self.ans += root.data
            # Traversal according to BST Rules
            if h > root.data:
                bfs(root.right)
            if l < root.data:
                bfs(root.left)

        bfs(root)
        return self.ans

if __name__ == "__main__":
    node = TreeNode(11)
    node.insert(12)
    node.insert(13)
    node.insert(14)
    node.insert(15)
    sol = solution()
    print(sol.range_bst(node,1,14))