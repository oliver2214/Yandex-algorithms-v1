class Node:
    def __init__(self, num=None):
        self.num = num
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, num):
        def add_new_node(root, num):
            if root.num == num:
                return 0
            elif root.num > num:
                if root.left is None:
                    root.left = Node(num)
                else:
                    return add_new_node(root.left, num)
            elif root.num < num:
                if root.right is None:
                    root.right = Node(num)
                else:
                    return add_new_node(root.right, num)

        if self.root is None:
            self.root = Node(num)
        else:
            add_new_node(self.root, num)

    def deep_crawl(self):
        def _deep_crawl(root):
            if root is None:
                return []
            elif root.left is None or root.right is None:
                return [*_deep_crawl(root.left), *_deep_crawl(root.right)]
            else:
                return [*_deep_crawl(root.left), root.num, *_deep_crawl(root.right)]

        root = self.root
        return _deep_crawl(root)


tree = Tree()
seq = []

for num in map(int, input().split()):
    if num == 0:
        continue
    else:
        tree.add(num)

seq = tree.deep_crawl()
print(*seq, sep="\n")
