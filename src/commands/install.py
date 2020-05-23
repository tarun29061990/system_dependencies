class Install:
    def process(self, commandArr, graph, installed_packages):
        commandArr = self.sanitize(commandArr)
        package = commandArr[0]

        if package in installed_packages:
            print(package+ " is already installed.")
        else:
            installed_packages[package] = 1
            dependencies = graph[package]
            for dep in dependencies:
                if dep not in installed_packages:
                    print("Installing "+dep)

        return installed_packages

    def sanitize(self, arr):
        i = 0
        while arr[i] == " ":
            i += 1

        return arr[i:]