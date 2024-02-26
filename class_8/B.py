class Node:
    def __init__(self, num=None):
        self.num = num
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.depth = 0

    def add(self, num):
        def add_new_node(root, num, depth):
            depth += 1
            if root.num == num:
                return 0
            elif root.num > num:
                if root.left is None:
                    root.left = Node(num)
                else:
                    return add_new_node(root.left, num, depth)
            elif root.num < num:
                if root.right is None:
                    root.right = Node(num)
                else:
                    return add_new_node(root.right, num, depth)
            self.depth = max(self.depth, depth)
            return depth

        if self.root is None:
            self.root = Node(num)
            self.depth = 1
            return self.depth
        else:
            return add_new_node(self.root, num, 1)


tree = Tree()
seq = []

for num in map(int, input().split()):
    if num == 0:
        continue
    else:
        depth = tree.add(num)
        if depth:
            seq.append(depth)

print(*seq)
