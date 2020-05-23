class Depend:
    def process(self, commandArr):
        commandArr = self.sanitize(commandArr)

        return commandArr

    def sanitize(self, arr):
        i = 0
        while arr[i] == " ":
            i += 1

        return arr[i:]