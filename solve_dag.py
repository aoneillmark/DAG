import numpy as np
import matplotlib.pyplot as plt
from paradag import DAG

# Define a class representing a node with specific attributes
class Node:
    # Class attributes: name, processing time (p), and deadline (d)
    name: str
    p: int
    d: int

    def __init__(self, name: str, p: int, d: int):
        # Constructor for initialising a Node instance with name, processing time, and deadline
        self.name = name
        self.p = p
        self.d = d

# Function to calculate the total processing time of unscheduled nodes
def C(l: list, l_schedule: list) -> int:
    # Sum up the processing time of all nodes in the list l that are not in l_schedule
    return sum([node.p for node in l if node not in l_schedule])

# Function to compute the cost (tardiness) of a specific node j in a given schedule
def g(l: list, l_schedule: list, j: int) -> int:
    # Calculate the tardiness of the node at index j, ensuring it is non-negative
    return max(0, C(l, l_schedule) - l[j].d)

# Function to select the next node to add to the schedule
def pick_next(l_nodes: DAG, l_schedule: list):
    # Create a copy of the DAG vertices as a list for processing
    set_copy = []
    for node in l_nodes.vertices():
        set_copy.append(node)
    
    # Initialise the minimum index and minimum tardiness with large placeholder values
    min_index: int = 100000000000
    min_g: int = 100000000000

    # Iterate over the list of nodes to find the optimal next node to schedule
    for i in range(len(set_copy)):
        # Check if the node is not already scheduled
        if (set_copy[i].name not in [node.name for node in l_schedule]):
            # Check if the node has no successors (i.e., it is ready to be scheduled) OR all successors already in the schedule
            if l_nodes.successors(set_copy[i]) == set(): # or all(
            #     # all() checks if all items in an iterative are true
            #     # This is checking if all successors are already in the schedule
            #     succ in l_schedule for succ in l_nodes.successors(set_copy[i])
            # ):
                # Update the minimum index and tardiness if a lower tardiness is found
                if (g(set_copy, l_schedule, i) < min_g):
                    min_index = i
                    min_g = g(set_copy, l_schedule, i)
            
            # Check if all successors of the node are already in the schedule
            all_successors_in_schedule = True
            for node in l_nodes.successors(set_copy[i]):
                if node not in l_schedule:
                    all_successors_in_schedule = False
            
            # Update the minimum index and tardiness if conditions are met
            if all_successors_in_schedule:
                if (g(set_copy, l_schedule, i) < min_g):
                    min_index = i
                    min_g = g(set_copy, l_schedule, i)
    
    # Insert the selected node at the start of the schedule
    l_schedule.insert(0, set_copy[min_index])

# Main function to set up nodes, construct the DAG, and generate the schedule
def main():
    # Create nodes with their respective processing times and deadlines
    J1 = Node(name="J1", p=3, d=2)
    J2 = Node(name="J2", p=4, d=1)
    J3 = Node(name="J3", p=2, d=3)
    J4 = Node(name="J4", p=1, d=4)

    # Initialise a Directed Acyclic Graph (DAG) and add vertices
    nodes = DAG()
    nodes.add_vertex(J1, J2, J3, J4)

    # Add directed edges between nodes to represent dependencies
    nodes.add_edge(J1, J3)  # J1 must be completed before J3
    nodes.add_edge(J3, J4)  # J3 must be completed before J4
    nodes.add_edge(J2, J4)  # J2 must be completed before J4
    
    # Initialise an empty schedule list
    schedule = []

    # Loop to build the schedule in reverse order (starting from the last node)
    for i in range(len(nodes.vertices())-1, -1, -1):
        pick_next(nodes, schedule)
    
    # Print the names of the nodes in the scheduled order
    for node in schedule:
        print(node.name)

# Execute the main function when the script is run
if __name__ == "__main__":
    main()