class TNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self):
        self.root = None
    #전위순환
    def preorderPrint(self):
        self._preorder(self.root)
    def _preorder(self,p):
        if p is not None:
            print(p.data)
            self._preorder(p.left)
            self._preorder(p.right)
    #중위순환
    def inorderPrint(self):
        self._inorder(self.root)
    def _inorder(self, p):
        if p is not None:
            self._inorder(p.left)
            print(p.data)
            self._inorder(p.right)
    #후위순환
    def postorderPrint(self):
        self._postorder(self.root)
    def _postorder(self, p):
        if p is not None:
            self._postorder(p.left)
            self._postorder(p.right)
            print(p.data)
    def height(self):
        return self._subTheight(self.root)
    def _subTheight(self, p):
        if p is None:
            return 0
        else:
            hleft = self._subTheight(p.left)
            hright = self._subTheight(p.right)
            return max(hleft, hright)+1
    def size(self):
        return self._subTsize(self.root)
    def _subTsize(self, p):
        if p is None:
            return 0
        else:
            return 1 + self._subTsize(p.left) + self._subTsize(p.right)
    def leafCount(self):
        return self._subTleafCount(self.root)
    def _subTleafCount(self, p):
        if p is None:
            return 0
        elif p.left is None and p.right is None:
            return 1
        else:
            return self._subTleafCount(p.left) + self._subTleafCount(p.right)
