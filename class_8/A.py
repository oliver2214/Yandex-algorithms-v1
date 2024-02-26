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
            if root.num > num:
                depth += 1
                if root.left is None:
                    root.left = Node(num)
                else:
                    return add_new_node(root.left, num, depth)
            elif root.num < num:
                depth += 1
                if root.right is None:
                    root.right = Node(num)
                else:
                    return add_new_node(root.right, num, depth)
            self.depth = max(self.depth, depth)

        if self.root is None:
            self.root = Node(num)
            self.depth = 1
        else:
            add_new_node(self.root, num, 1)


tree = Tree()

for num in map(int, input().split()):
    if num == 0:
        print(tree.depth)
    else:
        tree.add(num)
