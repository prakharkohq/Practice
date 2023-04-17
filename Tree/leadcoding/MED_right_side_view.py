"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.


"""

from Tree.Node import TreeNode

"""
Problem is going to be an update of level order traversal where we will pickup the last items of the  level order 
traversal
"""
from collections import deque
def solution(root):
    if root is None:
        return []
    queue, result = deque(root), []
    while queue:
        result.append(queue[-1].val)  ## Right side view mein bas last element daal dete ahi
        for item in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


if __name__ =="__main__":
    node = TreeNode(5)
    node.insert(2)
    node.insert(3)
    node.insert(44)
    node.insert(15)
    solution(node)