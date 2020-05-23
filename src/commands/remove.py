from graph import Graph
import copy

class Remove:
    def process(self, commandArr, graph, edges, installed_packages):
        commandArr = self.sanitize(commandArr)
        package = commandArr[0]
        dependencies = graph[package]
        output = []
        for dep in dependencies:
            if edges[dep] == 0:
                output.append("Removing "+ dep+ "\n")
                del installed_packages[dep]
                continue
            edges[dep] -= 1

        del graph[package]
        del installed_packages[package]
        return [graph, output]

    def sanitize(self, arr):
        i = 0
        while arr[i] == " ":
            i += 1

        return arr[i:]

