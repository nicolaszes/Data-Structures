# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # dfs O(N)
    def minDepthDFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left = self.minDepthDFS(root.left)
        right = self.minDepthDFS(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        else:
            return min(left, right) + 1
	
	# bfs O(N)
	# 当左子树深度为 1，右子树深度为 10000，此时用 BFS 更优
	def minDepthBFS (self, root: TreeNode) -> int:
		if not root: return 0
		queue, level = [], 0
		queue.append(root)

		while queue:
			level += 1

			for i in range(len(queue)):
				node = queue.pop(0)
				if node.left: queue.append(node.left)
				if node.right: queue.append(node.right)
				# 若有一个子节点为叶子结点
				if node.left == None and node.right == None:
					return level
