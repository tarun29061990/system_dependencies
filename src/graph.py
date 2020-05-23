class Graph:

    def topologicalSortUtil(self, v, visited, stack, graph):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack, graph)
        stack.insert(0, v)



    def topologicalSort(self, V, graph):
        visited = [False] * V
        stack = []

        for i in range(V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack, graph)
        print(stack)
        return stack