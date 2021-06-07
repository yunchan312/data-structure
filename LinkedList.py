class Node:
    def __init__(self, e):
        self.data = e
        self.link = None

class LinkedList:
    def __init__(self, e):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def clear(self):
        self.head = None
    def size(self):

    def getNode(self, pos):
        if pos<0:
            return None
        node = self.head
        while pos > 0 and node != 0:
            node = node.link
            pos -= 1
        return node
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
    def replace(self, pos ,e):
        node = self.getNode(pos)
        if node == None:
            print("Position Error")
        node.data = e
    def nodeCount(self, node):
        if node == None:
            return 0
        else:
            return self.nodeCount(node.link)+1
    def size(self):
        return self.nodeCount(self.head)
    def insert(self, pos, e):
        node = Node(e)
        before = self.getNode(pos-1)
        if before == None:
            node.link = self.head
            self.head = node
        else:
            node.link = before.link
            before.link = node
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

    def printAll(self, node):
            if node is not None:
                print(node.data)
                self.printAll(node.link)
    def printList(self):
            printAll(self.head)

    def recurGetNode(self, ptr, pos):
        if pos < 0:
            return None
        elif pos == 0:
            return ptr
        else:
            return self.recurGetNode(ptr.link,pos-1)

    def getNode(self, pos):
        node = self.head
        return self.recurGetNode(node, pos)


'''    def printList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.link'''

    # def find(self, val):

    '''def size(self):
            count = 0
            current = self.head
            while current is not None:
                count += 1
                current = current.link
            return count'''