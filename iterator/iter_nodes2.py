class Node:
    def __init__(self, value):
        self.left = []
        self.value = value
        self.right = []

    def iterate_left(self):
        for node in self.left:
            yield from node.iterate()

    def iterate_right(self):
        for node in self.right:
            yield from node.iterate()

    def iterate(self):
        yield from self.iterate_left()
        yield self.value
        yield from self.iterate_right()


def main():
    root = Node(0)
    root.left = [Node(i) for i in [1, 2, 3]]
    root.right = [Node(i) for i in [4, 5, 6]]
    for value in root.iterate():
        print(value)


if __name__ == "__main__":
    main()
