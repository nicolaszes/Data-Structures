# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 中序遍历，性能不佳 O(N)，空间复杂度较高
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root. val] + self.inorder(root.right)


class Solution:
    # 递归 O(N)，内存利用率更高
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)


class Solution:
    # 递归变形
    def isValidBST(self, root, min, max):
        if root == None:
            return True
        if min != None and root.val <= min:
            return False
        if max != None and root.val >= max:
            return False

        return isValidBST(self, root.left, min, root.val) and isValidBST(self, root.right, root.val, max)
