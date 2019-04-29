from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # dfs O(N)
    def maxDepthDFS(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return 1 + max(self.maxDepthDFS(root.left), self.maxDepthDFS(root.right))

    # bfs O(N)
    def maxDepthBFS(self, root: TreeNode) -> int:
        if not root: return 0
        queue, level = [], 0
        queue.append(root)

        while queue:
            level += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level