import numpy as np
import matplotlib.pyplot as plt
from paradag import DAG


class Node:
    name: str
    p: int
    d: int

    def __init__(self, name: str, p: int, d: int, predecessors: np.ndarray = [], successors: np.ndarray = []):
        self.name = name
        self.p = p
        self.d = d



def C(l_nodes: DAG, l_schedule: np.ndarray) -> int:
    return sum([node.p for node in l_nodes.vertices() if node not in l_schedule])


def g(l_nodes: DAG, j: int) -> int:
    return max(0, C(l_nodes) - l_nodes[j].d)

def g(l_nodes: DAG, node: Node) -> int:
    return max(0, C(l_nodes) - node.d)


def pick_next(l_nodes: DAG, l_schedule: np.ndarray[Node]) -> Node:
    min_index: int = min([g(l_nodes, j) 
                          for j in range(l_nodes.vertices().len()) 
                          if l_nodes[j] not in l_schedule 
                          and l_nodes.successors(l_nodes[j]) in l_schedule ])
    
    l_schedule.insert(0, l_nodes.vertices()[min_index])



def main():
    nodes = DAG()
    schedule = np.empty()
