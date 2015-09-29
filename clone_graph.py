__author__ = 'stephenosullivan'

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        self.visited = dict()
        if node:
            return self.recursiveBuild(node)

    def recursiveBuild(self, node):
        if node not in self.visited:
            newnode = UndirectedGraphNode(node.label)
            self.visited[node] = newnode
            newnode.neighbors = [self.recursiveBuild(neighbor) for neighbor in node.neighbors]
        else:
            newnode = self.visited[node]

        return newnode
