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

    def is_balanced(self):
        def _is_balanced(root, depth):
            if root is None:
                return depth, True
            else:
                depth += 1
                depth_left, fl_l = _is_balanced(root.left, depth)
                depth_right, fl_r = _is_balanced(root.right, depth)

                return max(depth, depth_left, depth_right), fl_l and fl_r and not abs(depth_left - depth_right) > 1

        return _is_balanced(self.root, 0)


tree = Tree()
seq = []

for num in map(int, input().split()):
    if num == 0:
        continue
    else:
        tree.add(num)

ans = tree.is_balanced()
print("YES") if ans[1] else print("NO")
