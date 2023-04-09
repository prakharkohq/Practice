"""

Sample Tree Class With basic CRUD operations and traversal techniques

"""


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Insertion is based on Binary Search Tree concept More Info : https://en.wikipedia.org/wiki/Binary_search_tree
        # To Insert values we only need value component
        if self.data:  # First check whether Data exists in the visited node or not if absent assign value in the node
            if self.data > value:  # If value is greater optimally check in left subtree
                if self.left is None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)  # Recursive call
            elif self.data < value:  # same logic is repeated for Right subtree
                if self.right is None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)
            else:
                return

        else:
            self.data = value

    def in_order_traversal(self, root):
        # Left -> Root -> Right ( Explanation : https://www.programiz.com/dsa/tree-traversal )
        if root:
            root.in_order_traversal(root.left)
            print(str(root.data) + "  ==> ", end=" ")
            root.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        # Root -> left -> right
        if root:
            print(str(root.data) + "  ==> ", end=" ")
            root.pre_order_traversal(root.left)
            root.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        # left -> right --> Root
        if root:
            root.post_order_traversal(root.left)
            root.post_order_traversal(root.right)
            print(str(root.data) + "  ==> ", end=" ")

if __name__ == "__main__":
    root = TreeNode(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.post_order_traversal(root)
    #print(result)