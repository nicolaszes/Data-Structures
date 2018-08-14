function BinarySearchTree () {
  var Node = function (key) {
    this.key = key
    this.left = null
    this.right = null
  }
  var root = null

  var insertNode = function (node, newNode) {
    if (newNode.key < node.key) {
      if (node.left === null) {
        node.left = newNode
      } else {
        insertNode(node.left, newNode)
      }
    } else {
      if (node.right === null) {
        node.right = newNode
      } else {
        insertNode(node.right, newNode)
      }
    }
  }

  this.insert = function (key) {
    var newNode = new Node(key)
    if (root === null) {
      root = newNode
    } else {
      insertNode(root, newNode)
    }
  }

  this.getRoot = function () {
    return root
  }

  var searchNode = function (node, key) {
    if (node === null) return false
    if (key < node.key) {
      return searchNode(node.left, key)
    }
    if (key > node.key) {
      return searchNode(node.right, key)
    }
    return true
  }

  this.search = function (key) {
    return searchNode(root, key)
  }

  var inOrderTraverseNode = function (node, cb) {
    if (node !== null) {
      inOrderTraverseNode(node.left, cb)
      cb(node.key)
      inOrderTraverseNode(node.right, cb)
    }
  }

  this.inOrderTraverse = function (cb) {
    inOrderTraverseNode(root, cb)
  }

  var preOrderTraverseNode = function (node, cb) {
    if (node !== null) {
      cb(node.key)
      preOrderTraverseNode(node.left, cb)
      preOrderTraverseNode(node.right, cb)
    }
  }

  this.preOrderTraverse = function (cb) {
    preOrderTraverseNode(root, cb)
  }

  var postOrderTraverseNode = function (node, cb) {
    if (node !== null) {
      postOrderTraverseNode(node.left, key)
      postOrderTraverseNode(node.right, key)
      cb(node.key)
    }
  }

  this.postOrderTraverse = function (cb) {
    postOrderTraverseNode(root, cb)
  }

  var minNode = function (node) {
    if (node) {
      while (node && node.left !== null) {
        node = node.left
      }
      return node.key
    }
    return null
  }

  this.min = function () {
    return minNode(root)
  }

  var maxNode = function (node) {
    if (node) {
      while (node && node.right !== null) {
        node = node.right
      }
    }
    return null
  }

  this.max = function () {
    return maxNode(root)
  }

  var removeNode = function (node, element) {
    if (node === null) return null

    if (element < node.key) {
      node.left = removeNode(node.left, element)
      return node
    }

    if (element > node.key) {
      node.right = removeNode(node.right, element)
      return node
    }

    /**
     * element is equal to node.item
     * handle 3 special conditions
     * 1 - a leaf node
     * 2 - a node with only 1 child
     * 3 - a node with 2 children
     */
    if (node.left === null && node.right === null) {
      node = null
      return node
    }

    if (node.left === null) {
      node = node.right
      return node
    }

    if (node.right === null) {
      node = node.left
      return node
    }

    var aux = findMinNode(node.right)
    node.key = aux.key
    node.right = removeNode(node.right, aux.key)
    return node
  }

  this.remove = function (element) {
    root = removeNode(root, element)
  }
}

var bTree = new BinarySearchTree()
bTree.insert(5)
bTree.insert(3)
bTree.insert(1)
bTree.insert(9)
bTree.insert(8)
console.log(bTree)