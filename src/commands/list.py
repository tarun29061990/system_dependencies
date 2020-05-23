class List:
    def process(self, commandArr, installed_packages):
        output = []
        for k,v in enumerate(installed_packages):
            output.append("  "+v+" \n")

        return ["LIST \n"]+output

    def sanitize(self, arr):
        i = 0
        while arr[i] == " ":
            i += 1

        return arr[i:]