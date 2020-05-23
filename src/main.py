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
        output = []

        if command[0] == "DEPEND":
            # depend
            self.graph, self.edges, output = Depend().process(command[1:], self.graph, self.edges)
        elif command[0] == "INSTALL":
            self.installOrder, output = Install().process(command[1:], self.graph, self.installOrder)
        elif command[0] == "LIST":
            output = List().process(command[1:], self.installOrder)
        elif command[0] == "REMOVE":
            # remove
            self.graph, output = Remove().process(command[1:], self.graph, self.edges, self.installOrder)
        else:
            self.file.close()
        if output:
            self.file.writelines(output)

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
    main = Main(outFile)
    with open(inputFilePath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            main.process_command(line.strip())
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1


if __name__ == "__main__":
    run()