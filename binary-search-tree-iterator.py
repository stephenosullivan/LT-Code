__author__ = 'stephenosullivan'

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIteratorUsingYield:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.it = self.recursive_inorder(root)
        self._hasnext = None

    def recursive_inorder(self, node):
        if node:
            for node_data in self.recursive_inorder(node.left):
                yield node_data
            yield node.val
            for node_data in self.recursive_inorder(node.right):
                yield node_data

    #def __iter__(self):
    #    return self

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self._hasnext is None:
            try: self._thenext = next(self.it)
            except StopIteration: self._hasnext = False
            else: self._hasnext = True
        return self._hasnext


    # @return an integer, the next smallest number
    def next(self):
        if self._hasnext:
            result = self._thenext
        else:
            result = next(self.it)
        self._hasnext = None
        return result

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):

        self.inorder = []
        if root:
            nodes_to_visit = [root]
            node = root
            while node.left:
                nodes_to_visit.append(node.left)
                node = node.left

            while nodes_to_visit:
                node = nodes_to_visit.pop()
                self.inorder.append(node)
                if node.right:
                    node = node.right
                    nodes_to_visit.append(node)
                    while node.left:
                        nodes_to_visit.append(node.left)
                        node = node.left

            self.counter = len(self.inorder)
            self.iternode = iter(self.inorder)

        else:
            self.counter = 0

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        self.counter > 0

    # @return an integer, the next smallest number
    def next(self):
        self.counter -= 1
        return self.iternode.next().val


        # This solves a different problem. Given the root find the
        # next smallest node so that the iterator passes over a
        # decreasing set of values

class BSTIteratorDecreasing:
    # @param root, a binary search tree's root node

    def __init__(self, root):
        self.inorder_reverse = []
        if root:
            nodes_to_visit = [root]
            while nodes_to_visit:
                node = nodes_to_visit.pop()
                self.inorder_reverse.append(node)
                if node.left:
                    nodes_to_visit.append(node.left)
                    node = node.left
                while node.right:
                    nodes_to_visit.append(node.right)
                    node = node.right

            self.counter = len(self.inorder_reverse)
            self.iternode = iter(self.inorder_reverse)

        else:
            self.counter = 0

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        self.counter > 0

    # @return an integer, the next smallest number
    def next(self):
        self.counter -= 1
        return self.iternode.next().val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    #a = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(6)
    a.left = b
    a.right = c
    i, v = BSTIterator(a), []
    while i.hasNext():
        v.append(i.next())          # -> __next__ in 3.4
    print(list(v))
