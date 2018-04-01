

class BST:

    class Node:
        def __init__(self, key, value, N):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.N = N

    def __init__(self):
        self.root = None

    def size(self, node):
        if node is None:
            return 0
        else:
            return node.N

    def insert(self, key, value):
        def _insert(node, key, value):
            if node is None:
                return self.Node(key, value, 1)
            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            else:
                node.value = value

            return node

        self.root = _insert(self.root, key, value)

    def get(self, key):
        def _get(node, key):
            if node is None:
                return None
            if key < node.key:
                return _get(node.left, key)
            elif key > node.key:
                return _get(node.right, key)
            else:
                return node.value

        return _get(self.root, key)

    def min(self):
        return self._min(self.root).key

    def _min(self, node):
        if node.left is None:
            return node
        else:
            return self._min(node.left)

    def max(self):
        def _max(node):
            if node.right is None:
                return node
            else:
                return _max(node.right)

        return _max(self.root).key

    def floor(self, key):
        def _floor(node, key):
            if node is None:
                return None
            if key == node.key:
                return node
            if key < node.key:
                return _floor(node.left, key)
            t = _floor(node.right, key)
            if t is not None:
                return t
            else:
                return node

        node = _floor(self.root, key)
        if node is None:
            return None
        else:
            return node.key

    def ceiling(self, key):
        def _ceiling(node, key):
            if node is None:
                return None
            if key == node.key:
                return node
            if key > node.key:
                return _ceiling(node.right, key)
            t = _ceiling(node.left, key)
            if t is not None:
                return t
            else:
                return node

        node = _ceiling(self.root, key)
        if node is None:
            return None
        else:
            return node.key

    def deleteMin(self):
        self._deleteMin(self.root)

    def _deleteMin(self, node):
        if node.left is None:
            return node.right
        node.left = self._deleteMin(node.left)
        node.N = self.size(node.left) + self.size(node.right) + 1
        return node

    def deleteMax(self):
        def _deleteMax(node):
            if node.right is None:
                return node.left
            node.right = _deleteMax(node.right)
            node.N = self.size(node.left) + self.size(node.right) + 1
            return node

        _deleteMax(self.root)

    def delete(self, key):
        def _delete(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if node.right is None:
                    return node.left
                if node.left is None:
                    return node.right
                t = node
                node = self._min(t.right)
                node.right = self._deleteMin(t.right)
                node.left = t.left
            node.N = self.size(node.left) + self.size(node.right) + 1

            return node

        self.root = _delete(self.root, key)


    def __str__(self):
        def _print(text, node):
            if node.left:
                text = _print(text, node.left)
            text.append(str(node.value))
            if node.right:
                text = _print(text, node.right)
            return text

        text = ' '.join(_print([], self.root))

        return text
