# 基本性质：
# 1.根节点不包含字符，除根节点外每一个节点都只包含一个字符
# 2.从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串
# 3.没个节点的所有子节点包含的字符都不相同
class TrieNode:
  # Trie node class
  def __init__(self):
    self.children = [None] * ALPHABET_SIZE

    # isEndOfWord is True if node represent
    # the end of the word
    self.isEndOfWord = False

class Trie(object):
  def __init__(self):
    self.root = {}
    self.end_of_word = '#'

  def insert(self, word):
    node = self.root
    for char in word:
      node = node.setdefault(char, {})
    node[self.end_of_word] = self.end_of_word

  def search(self, word):
    node = self.root
    for char in word:
      if char not in node:
        return False
      node = node[char]
    return self.end_of_word in node

  def startWith(self, prefix):
    node = self.root
    for char in prefix:
      if char not in node:
        return False
      node = node[char]
    return True 