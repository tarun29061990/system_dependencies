import os, sys, getopt
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../tests")
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "../")

filepath = '../input.txt'

def process_command(command):
    command = sanitize_command(command)
    print(command)

    if command[0] == "DEPEND":
        # depend
    elif command[0] == "INSTALL":

    elif command[0] == "LIST":

    else:
        # remove


def sanitize_command(command):
    i = 0
    # remove initial spaces
    while command[i] == " ":
        i += 1
    res = ""
    while i < len(command):
        res += command[i]
        i += 1

    return res.split(" ")

def main():
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:

            process_command(line.strip())
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1

if __name__ == "__main__":
    main()