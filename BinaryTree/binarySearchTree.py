class BinarySearchTree:
  def preorder(self, root):
    if root:
      self.traverse_path.append(root.val)
      self.preorder(root.left)
      self.preorder(root.right)
  
  # 二叉搜索树下，inorder是一个有序数组
  def inorder(self, root):
    if root:
      self.inorder(root.left)
      self.traverse_path.append(root.val)
      self.inorder(root.right)
    
  def postorder(self, root):
    if root:
      self.postorder(root.left)
      self.postorder(root.right)
      self.traverse_path.append(root.val)