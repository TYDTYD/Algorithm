# 노드 구현
class Node(object):
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

# 이진트리 구현
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root=self._insert_value(self.root,data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

# 전위 순회
    def PreOrder(self, root):
        if root is None:
            pass
        else:
            print(root.data,end=' ')
            self.PreOrder(root.left)
            self.PreOrder(root.right)

# 후위 순회
    def PostOrder(self, root):
        if root is None:
            pass
        else:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data,end=' ')

# 중위 순회
    def InOrder(self, root):
        if root is None:
            pass
        else:
            self.InOrder(root.left)
            print(root.data,end=' ')
            self.InOrder(root.right)


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

bst.InOrder(bst.root)