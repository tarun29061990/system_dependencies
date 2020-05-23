class Install:
    def process(self, commandArr, graph, installed_packages):
        commandArr = self.sanitize(commandArr)
        package = commandArr[0]
        output = []
        if package in installed_packages:
            output.append(package+ " is already installed. \n")
        else:
            installed_packages[package] = 1
            dependencies = graph[package]
            for dep in dependencies:
                if dep not in installed_packages:
                    output.append("Installing "+dep+" \n")
            output.append("Installing "+package+" \n")

        return [installed_packages, output]

    def sanitize(self, arr):
        i = 0
        while arr[i] == " ":
            i += 1

        return arr[i:]