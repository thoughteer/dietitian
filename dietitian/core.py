import collections
import math
import sys


Item = collections.namedtuple("Item", ["index", "name", "protein", "fat", "carbohydrate", "score"])
Node = collections.namedtuple("Node", ["head", "tail"])


class Tensor:

    def __init__(self, shape, default=-math.inf):
        self.shape = shape
        self.data = [default] * math.prod(shape)

    def __getitem__(self, index):
        return self.data[self.__flatten(index)]

    def __setitem__(self, index, value):
        self.data[self.__flatten(index)] = value

    def __flatten(self, index):
        assert len(index) == len(self.shape)
        r = 0
        for i, s in zip(index, self.shape):
            r = r * s + i
        return r


def run(args):
    items = list(load(args.path))
    scores = Tensor((args.protein.high, args.fat.high, args.carbohydrate.high))
    scores[0, 0, 0] = 0
    nodes = {}
    nodes[(0, 0, 0)] = None
    for p in range(args.protein.high):
        for f in range(args.fat.high):
            for c in range(args.carbohydrate.high):
                for item in items:
                    p_, f_, c_ = p - item.protein, f - item.fat, c - item.carbohydrate
                    if p_ < 0 or f_ < 0 or c_ < 0:
                        continue
                    if (p_, f_, c_) not in nodes:
                        continue
                    score = scores[p_, f_, c_] + item.score
                    if score > scores[p, f, c]:
                        scores[p, f, c] = score
                        nodes[(p, f, c)] = Node(item.index, nodes.get((p_, f_, c_)))
    solution = None
    score = -math.inf
    for p in range(args.protein.low, args.protein.high):
        for f in range(args.fat.low, args.fat.high):
            for c in range(args.carbohydrate.low, args.carbohydrate.high):
                if (p, f, c) not in nodes:
                    continue
                if scores[p, f, c] > score:
                    score = scores[p, f, c]
                    solution = (p, f, c)
    if solution is None:
        fail()
    report(solution, unroll(nodes[solution], items))


def load(path):
    with open(path, "r") as stream:
        for index, line in enumerate(stream):
            fields = line.strip().split("\t")
            assert len(fields) == 5
            name = fields[0]
            protein, fat, carbohydrate = (int(field) for field in fields[1:-1])
            score = float(fields[-1])
            yield Item(index, name, protein, fat, carbohydrate, score)


def fail():
    sys.stderr.write("no solution found\n")
    sys.exit(1)


def unroll(node, items):
    result = []
    while node is not None:
        result.append(items[node.head].name)
        node = node.tail
    return collections.Counter(result)


def report(solution, menu):
    print("Protein: %dg" % solution[0])
    print("Fat: %dg" % solution[1])
    print("Carbohydrate: %dg" % solution[2])
    print("")
    for name in sorted(menu):
        print(name, "x%d" % menu[name])
