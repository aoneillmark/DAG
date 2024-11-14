import numpy as np
import matplotlib.pyplot as plt
from paradag import DAG


class Node:
    name: str
    p: int
    d: int

    def __init__(self, name: str, p: int, d: int):
        self.name = name
        self.p = p
        self.d = d



def C(l_nodes: DAG, l_schedule: np.ndarray) -> int:
    return sum([node.p for node in l_nodes.vertices() if node not in l_schedule])


def g(l_nodes: DAG, j: int) -> int:
    return max(0, C(l_nodes) - l_nodes[j].d)

def g(l_nodes: DAG, node: Node) -> int:
    return max(0, C(l_nodes) - node.d)


def pick_next(l_nodes: DAG, l_schedule: np.ndarray):
    min_index: int = min([g(l_nodes, j) 
                          for j in range(l_nodes.vertices().len()) 
                          if l_nodes[j] not in l_schedule 
                          and l_nodes.successors(l_nodes[j]) in l_schedule ])
    
    l_schedule.insert(0, l_nodes.vertices()[min_index])



def main():
    J1 = Node("J1", 3, 2)
    J2 = Node("J2", 4, 1)
    J3 = Node("J3", 2, 3)
    J4 = Node("J4", 1, 4)
    
    nodes = DAG()
    nodes.add_vertex(J1, J2, J3, J4)
    nodes.add_edge(J1, J3)
    nodes.add_edge(J3, J4)
    nodes.add_edge(J2, J4)
    
    schedule = np.empty(nodes.vertices().len())
    
    while schedule.len() < nodes.vertices().len():
        pick_next(nodes, schedule)
        
    print(schedule)
