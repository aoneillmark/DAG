import numpy as np
import matplotlib.pyplot as plt
from paradag import DAG
from solve_dag import Node


# Helper function to get a node by its name
def get_node_by_name(name, nodes):
    for node in nodes.vertices():
        if node.name == str(name):
            return node
    return None

# Function to add an edge between nodes by their names
def G(name1, name2, nodes):
    node1 = get_node_by_name(name1, nodes)
    node2 = get_node_by_name(name2, nodes)
    if node1 and node2:
        nodes.add_edge(node1, node2)
    else:
        print(f"Error: One or both nodes not found: {name1}, {name2}")

def main():
    p = [3, 10, 2, 2, 5, 2, 14, 5, 6, 5, 5, 2, 3, 3, 5, 6, 6, 6, 2, 3, 2, 3, 14, 5, 18, 10, 2, 3, 6, 2, 10]

    d = [172, 82, 18, 61, 93, 71, 217, 295, 290, 287, 253, 307, 279, 73, 355, 34, 233, 77, 88, 122, 71, 181, 340, 141, 209, 217, 256, 144, 307, 329, 269]

    nodes = DAG()
    for i in range(0,len(p)):
        nodes.add_vertex(Node(name=f"{i}", p=p[i], d=d[i]))

    # # Print out the nodes to ensure they have been added properly
    # for node in nodes.vertices():
    #     print(f"Node name: {node.name}, p: {node.p}, d: {node.d}")

    G(0, 30, nodes)
    G(1, 0, nodes)
    G(2, 7, nodes)
    G(3, 2, nodes)
    G(4, 1, nodes)
    G(5, 15, nodes)
    G(6, 5, nodes)
    G(7, 6, nodes)
    G(8, 7, nodes)
    G(9, 8, nodes)
    G(10, 0, nodes)
    G(11, 4, nodes)
    G(12, 11, nodes)
    G(13, 12, nodes)
    G(16, 14, nodes)
    G(14, 10, nodes)
    G(15, 4, nodes)
    G(16, 15, nodes)
    G(17, 16, nodes)
    G(18, 17, nodes)
    G(19, 18, nodes)
    G(20, 17, nodes)
    G(21, 20, nodes)
    G(22, 21, nodes)
    G(23, 4, nodes)
    G(24, 23, nodes)
    G(25, 24, nodes)
    G(26, 25, nodes)
    G(27, 25, nodes)
    G(28, 26, nodes)
    G(28, 27, nodes)
    G(29, 3, nodes)
    G(29, 9, nodes)
    G(29, 13, nodes)
    G(29, 19, nodes)
    G(29, 22, nodes)
    G(29, 28, nodes)

if __name__ == "__main__":
    main()
