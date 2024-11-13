import numpy as np
import matplotlib.pyplot as plt


class Node:
    name: str
    p: int
    d: int


class DAG:
    nodes: tree[Node]


    def __init__(self, node: Node) -> None:
        self.nodes = [node]


    def C(self):
        return sum([node.p for node in self.nodes])


    def g(self, j: int):
        return max(0, self.C() - self.nodes[j].d)


    def pick_next(self) -> Node:
        node: Node = min( [self.g(j) for j in range(self.len())] )


def main():
    return