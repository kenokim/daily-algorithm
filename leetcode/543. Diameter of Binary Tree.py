# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_diameter = 0

    def inspect_node(self, node: Optional[TreeNode]) -> (int, int):
        """returns (diameter, height)"""
        if not node:
            return 0, -1

        left_diameter, left_height = self.inspect_node(node.left)
        right_diameter, right_height = self.inspect_node(node.right)

        diameter = left_height + right_height + 2
        height = max(left_height + 1, right_height + 1)

        self.max_diameter = max(self.max_diameter, diameter)

        return diameter, height

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.inspect_node(root)
        return self.max_diameter  
        

# node -> diameter = max(left.height + 1 + right.height + 1, diameter(left), diameter(right))