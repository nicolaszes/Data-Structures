# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


# class Solution:
#     # O(N)
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """

#         # DFS
#         if not root: return []
#         self.result = []
#         self._dfs(root, 0)
#         return self.result
#     def _dfs(self, node, level):
#         if not node: return
        
#         if len(self.result) < level + 1:
#             self.result.append([])
#         self.result[level].append(node.val)
#         self._dfs(node.left, level + 1)
#         self._dfs(node.right, level + 1)

class Solution:
    # O(N)
    def levelOrder(self, root): 
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS
        if not root: return []
        
        result = []
        queue = deque()
        queue.append(root)
        
        # 图的遍历
        # visited = set(root)
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # 处理每一层的数据
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                # 判断当前node是否还有子节点，如果有，则插入 queue当中，进行下一次遍历
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            result.append(current_level)
        return result

solu = Solution()
solu.levelOrder([3,9,20,None,None,15,7])