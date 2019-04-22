# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 递归
        # if p.val < root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif p.val > root.val < q.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # return root

        # 非递归
        while root:
            # 如果 p小于 root，q也是小于 root
            if p.val < root.val > q.val:
                root = root.left
            # 如果 p大于 root，q也是大于 root
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root