# 이진 탐색트리의 구현
class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def setRoot(self, value):
        self.root = Node(value)

# 이진탐색트리 탐색
    def find(self, value):
        if (self.findNode(self.root, value) is False):
            return False
        else:
            return True

    def findNode(self, currentNode, value):
        if (currentNode is None):
            return False
        elif (value == currentNode.value):
            return currentNode
        elif (value < currentNode.value):
            return self.findNode(currentNode.leftChild, value)
        else:
            return self.findNode(currentNode.rightChild, value)

# 이진 탐색트리 삽입
    def insert(self, value):
        if (self.root is None):
            self.setRoot(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self, currentNode, value):
        if (value <= currentNode.value):
            if (currentNode.leftChild):
                self.insertNode(currentNode.leftChild, value)
            else:
                currentNode.leftChild = Node(value)
        elif (value > currentNode.value):
            if (currentNode.rightChild):
                self.insertNode(currentNode.rightChild, value)
            else:
                currentNode.rightChild = Node(value)

    def traverse(self):
        return self.traverseNode(self.root)

    def traverseNode(self, currentNode):
        result = []
        if (currentNode.leftChild is not None):
            result.extend(self.traverseNode(currentNode.leftChild))
        if (currentNode is not None):
            result.extend([currentNode.val])
        if (currentNode.rightChild is not None):
            result.extend(self.traverseNode(currentNode.rightChild))
        return result