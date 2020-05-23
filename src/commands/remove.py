
class Remove:
    def process(self, commandArr, graph, edges, installed_packages):
        output = []
        commandArr = self.sanitize(commandArr)
        package = commandArr[0]

        if edges[package] > 0:
            output.append("  "+package+" is still needed. \n")
            return [graph, ["REMOVE "+package+" \n"]+output]

        dependencies = graph[package]
        for dep in dependencies:
            if edges[dep] == 0:
                output.append("  Removing "+ dep+ "\n")
                del installed_packages[dep]
                continue
            edges[dep] -= 1

        del graph[package]
        if package in installed_packages:
            del installed_packages[package]
        return [graph, ["REMOVE "+package+" \n"]+output]

    def sanitize(self, arr):
        i = 0
        while len(arr) and arr[i] == " ":
            i += 1

        return arr[i:]

