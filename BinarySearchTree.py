class TNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None
    def search1(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None
    def search2(self, key):
        return self._searchBst(self.root, key)
    def _searchBst(self, node, key):
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self._searchBst(self.left, key)
        else:
            return self._searchBst(self.right, key)
    def maximum(self):
        node = self.root
        if node is None:
            return None
        while node is not None:
            node = node.right
        return node.key
    def minimum(self):
        node = self.root
        if node is None:
            return None
        while node is not None:
            node = node.right
        return node.key
    def _minNode(self, node):
        if node.left == None:
            return node
        else:
            return self._minNode(node.left)
    def insert(self,key,value):
        self.root = self._insertBst(self.root, key, value)
    def _insertBst(self, node,key,value):
        if node is None:
            return TNode(key,value)
        elif key < node.key:
            node.left = self._insertBst(node.left,key,value)
        elif key > node.key:
            node.right = self._insertBst(node.right,key,value)
        else:
            pass
        return node
    def delete(self, key):
        self.root = self._deleteNode(self.root,key)
    def _deleteNode(self, node, key):
        if node == None:
            return node
        if key < node.key:
            node.left = self._deleteNode(self.left, key)
            return node
        elif key > node.key:
            node.right = self._deleteNode(self.right, key)
            return node
        else:
            if node.left == None:
                return node.right
            if node.right == None:
                return node.left

            rightminNode = self._minNode(node.right)
            node.key = rightminNode.key
            node.value = rightminNode.value
            node.right = self._deleteNode(node.right, key)
            return node

