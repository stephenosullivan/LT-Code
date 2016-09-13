class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.graph = dict()
        for index, couple in enumerate(equations):
            val = values[index]
            if couple[0] in self.graph:
                self.graph[couple[0]].append((couple[1], val))
            else:
                self.graph[couple[0]] = [(couple[1], val)]

            if couple[1] in self.graph:
                self.graph[couple[1]].append((couple[0], val))
            else:
                self.graph[couple[1]] = [(couple[0], 1. / val)]

        output = []
        for query in queries:
            output.append(self.value(query))

        return output

    def value(self, query):
        visited = set()
        start, end = query
        if start == end and start in self.graph:
            return 1.0
        visited.add(start)
        paths = [([start], 1)]
        while paths:
            path, weight = paths.pop()
            last = path[-1]
            if last in self.graph:
                for neighbor in self.graph[last]:
                    if neighbor[0] not in visited:
                        if neighbor[0] == end:
                            return weight * neighbor[1]

                        paths.append((path + [neighbor[0]], weight * neighbor[1]))
                        visited.add(neighbor[0])
        return -1.


if __name__ == '__main__':
    sol = Solution()
    equations = [["a", "e"], ["b", "e"]]
    values = [4., 3.]
    queries = [["a", "b"], ["e", "e"], ["x", "x"]]
    print(sol.calcEquation(equations, values, queries))
    print(sol.graph)
