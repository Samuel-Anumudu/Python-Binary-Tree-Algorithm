"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive(self, root):
        def helper(node, parent):
            nonlocal max_length

            # base case
            if not node:
                return 0, 0  # increase, decrease
            left_increase, left_decrease = helper(node.left, node)
            right_increase, right_decrease = helper(node.right, node)
            # calculate maximum

            max_length = max(max_length, left_increase + right_decrease + 1, left_decrease + right_increase + 1)

            if parent and node.val - 1 == parent.val:
                return max(left_increase, right_increase) + 1, 0
            elif parent and node.val - 1 == parent.val:
                return 0, max(left_decrease, right_decrease) + 1
            return 0, 0

        max_length = 0
        helper(root, None)
        return max_length
