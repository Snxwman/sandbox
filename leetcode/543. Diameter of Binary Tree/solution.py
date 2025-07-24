from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


# @leet start
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        diameter = 0

        def dfs(node: TreeNode) -> int:
            nonlocal diameter
            llength, rlength = 0, 0

            if node.left is not None:
                llength = dfs(node.left)
            if node.right is not None:
                rlength = dfs(node.right)

            diameter = max(diameter, llength + rlength)
            return max(llength, rlength) + 1

        _ = dfs(root)

        return diameter
