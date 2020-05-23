import os, sys, getopt
from collections import defaultdict, OrderedDict
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../src/commands")

from commands.depend import Depend
from commands.install import Install
from commands.list import List
from commands.remove import Remove


class Main:
    def __init__(self, outFile):
        self.graph = defaultdict(list)
        self.installOrder = OrderedDict()
        self.edges = defaultdict(int)

        self.file = outFile

    def process_command(self, command):
        command = self.sanitize_command(command)
        print(command)

        if command[0] == "DEPEND":
            # depend
            self.graph, self.edges, output = Depend().process(command, self.graph, self.edges)
        elif command[0] == "INSTALL":
            self.installOrder = Install().process(command, self.graph, self.installOrder)
        elif command[0] == "LIST":
            self.graph = List().process(command, self.graph, self.installOrder)
        else:
            # remove
            self.graph = Remove().process(command, self.graph, self.installOrder)

        self.file.writeLines(output)

    def sanitize_command(self, command):
        i = 0
        # remove initial spaces
        while command[i] == " ":
            i += 1
        res = ""
        while i < len(command):
            res += command[i]
            i += 1

        return res.split(" ")

def run():
    inputFilePath = '../input.txt'
    outFilePath = "../output.txt"
    outFile = open(outFilePath, "w")
    main = Main(outFile=outFile)
    with open(inputFilePath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            main.process_command(line.strip())
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
    outFile.close()


if __name__ == "__main__":
    run()