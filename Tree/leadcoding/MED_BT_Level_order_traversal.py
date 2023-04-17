"""
Level Order Traversal :
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

"""
from collections import deque


def sol_myattempt(root):
    if not root: return []
    # We will use priority queue for this purpose
    dq, result = deque([root]), []
    """
    On each step extract all nodes from queue and put their children to to opposite end of queue. In this way we will 
    have full level in the end of each step and our queue will be filled with nodes from the next level.
    """
    while dq:
        level = []
        """
        One thing I understood very late is, for i in range(len(q)): also works, len is computed at beginning of the 
        loop and it won't change even if you append something in the loop.
        """
        for item in range(len(dq)):
            # pull out each children and let there kids be insertd in the queue for next iteration
            node = dq.popleft()
            level.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        result.append(level)

    return result

if __name__ == "__main__":
    print(sol_myattempt)