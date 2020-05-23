class Depend:
    def process(self, commandArr, graph):
        commandArr = self.sanitize(commandArr)
        parent = commandArr[0]
        for i in range(1, len(commandArr)):
            package = commandArr[i]
            if package != " ":
                graph[parent].append(package)

        return graph

    def sanitize(self, arr):
        i = 0
        while arr[i] == " ":
            i += 1

        return arr[i:]