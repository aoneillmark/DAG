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



def C(l: list, l_schedule: np.ndarray) -> int:
    return sum([node.p for node in l if node not in l_schedule])


def g(l: list, l_schedule: np.ndarray, j: int) -> int:
    return max(0, C(l, l_schedule) - l[j].d)


def pick_next(l_nodes: DAG, l_schedule: np.ndarray, current_index):
    set_copy = []
    for node in l_nodes.vertices():
        set_copy.append( node )
    
    min_index: int = 0
    
    for i in range(len(set_copy)):
        if (set_copy[i] not in l_schedule) and l_nodes.successors(set_copy[i]) and (g(set_copy, l_schedule, i) < g(set_copy, l_schedule, min_index)):
            min_index = i
    
    l_schedule[current_index] = set_copy[min_index]




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
    
    schedule = np.empty(len(nodes.vertices()), Node)
    
    for i in range(len(nodes.vertices())-1, 0, -1):
        pick_next(nodes, schedule, i)
        
    print([ node.name for node in schedule ])
