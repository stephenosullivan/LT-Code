# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        output = ""
        for elem in self.getElems(root):
            output += str(elem)
            output += " "
        return output[:-1]

    def getElems(self, root):
        if root:
            yield root.val
            for val in self.getElems(root.left):
                yield val
            for val in self.getElems(root.right):
                yield val
        else:
            yield None

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodeVals = data.split()
        if nodeVals[0] == 'None':
            return

        prehead = TreeNode(0)
        nodestack = [prehead]

        index = 0
        while nodestack:
            current = nodestack.pop()
            if nodeVals[index] != 'None':
                print("r", nodeVals[index])
                current.right = TreeNode(int(nodeVals[index]))
                current = current.right
                nodestack.append(current)
                index += 1

                while nodeVals[index] != 'None':
                    current.left = TreeNode(int(nodeVals[index]))
                    current = current.left
                    nodestack.append(current)
                    index += 1
            index += 1

        return prehead.right


if __name__ == '__main__':
    myTree = TreeNode(1)
    myTree.left = TreeNode(2)
    myTree.right = TreeNode(3)

    sol = Codec()
    serialized = sol.serialize(myTree)
    print(serialized)
    deserialized = sol.deserialize(serialized)

    print(deserialized.val)
    print(deserialized.left.val)
    print(deserialized.right.val)
