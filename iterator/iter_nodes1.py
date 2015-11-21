class Node:
    def __init__(self, value):
        self.left = []
        self.value = value
        self.right = []

    def iterate(self):
        for node in self.left:
            yield node.value
        yield self.value
        for node in self.right:
            yield node.value


def main():
    root = Node(0)
    root.left = [Node(i) for i in [1, 2, 3]]
    root.right = [Node(i) for i in [4, 5, 6]]
    for value in root.iterate():
        print(value)


if __name__ == "__main__":
    main()
