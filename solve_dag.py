import numpy as np
import matplotlib.pyplot as plt


class Node:
    name: str
    p: int
    d: int
    predecessors: list
    successors: list

    def __init__(self, name: str, p: int, d: int, predecessors: list = [], successors: list = []):
        self.name= name
        self.p = p
        self.d = d
        self.predecessors = predecessors
        self.successors = successors


class DAG:
    nodes: list[Node]


    def __init__(self, node: Node):
        self.nodes = [node]


    def C(self) -> int:
        return sum([node.p for node in self.nodes])


    def g(self, j: int) -> int:
        return max(0, self.C() - self.nodes[j].d)


    def pick_next(self, schedule: list[Node]) -> Node:
        min_index: int = min([self.g(j) for j in range(self.nodes.len())])
        
        schedule.insert(0, self.nodes[min_index])
        self.nodes.pop(min_index)


def main():
    return