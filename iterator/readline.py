# coding=utf-8


def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line


def grep(pattern, lines):
    return (line for line in lines if pattern in line)


def printlines(lines):
    for line in lines:
        print(line, end='')
    print('')


def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)


if __name__ == '__main__':
    main('--', ['a.txt', 'b.txt'])
