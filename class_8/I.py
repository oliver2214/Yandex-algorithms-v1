# WA: 2
import sys

sys.setrecursionlimit(100000)


class Person:
    def __init__(self, name):
        self.name = name
        self.kids = []


class Tree:
    def __init__(self):
        self.root = None
        self.adopted = []

    def find(self, person):
        def _find(root, person):
            if person.name == root.name:
                return root, True
            for kid in root.kids:
                target, fl = _find(kid, person)
                if fl:
                    return target, fl
            return self.root, False

        if self.root is None:
            return None, False
        else:
            return _find(self.root, person)

    def add(self, person, parent):
        root, fl = self.find(parent)
        if fl:
            root.kids.append(person)
        else:
            if self.root is None:
                self.root = parent
            else:
                parent.kids.append(self.root)
                self.root = parent
            return self.root.kids.append(person)

    def crawl(self):
        def _crawl(root):
            if len(root.kids) == 0:
                return [(root.name, 0)]
            cntr = 0
            lst = [None]
            for kid in root.kids:
                lst_kids = _crawl(kid)
                lst.extend(lst_kids)
                cntr = cntr + lst_kids[0][1] + 1
            lst[0] = (root.name, cntr)
            return lst

        return _crawl(self.root)


n = int(input())
tree = Tree()
people = []

for _ in range(n - 1):
    kid_name, parent_name = input().split()
    person = Person(kid_name)
    parent = Person(parent_name)
    tree.add(person, parent)

ans = tree.crawl()
ans.sort(key=lambda x: x[0])
for name, k in ans:
    print(f"{name} {k}")
