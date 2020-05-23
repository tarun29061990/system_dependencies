class Depend:
    def process(self, commandArr, graph):
        commandArr = self.sanitize(commandArr)
        package = commandArr[0]

        return graph

    def sanitize(self, arr):
        i = 0
        while arr[i] == " ":
            i += 1

        return arr[i:]