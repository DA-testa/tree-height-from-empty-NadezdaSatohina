# python3

import sys
import threading


tree_len = int(input("Node Count:"))
input_arr = [int(node) for node in input("Nodes: ").split(" ")]

def get_child_nodes(nodes_to_find, initial_input, level):
    level += 1
    child_nodes = []
    for node in nodes_to_find: #[0] -> [4] -> [1] -> [2, 5]
        for index, pointer in enumerate(initial_input): #[(0, -1), (1, 3), (2, 1), (3, 0), (4, 1), (5, 2)]
            if pointer == node:
                child_nodes.append(index)
    if child_nodes:
        level = get_child_nodes(child_nodes, initial_input, level)
    return level
    
result = get_child_nodes([input_arr.index(-1)], input_arr, 0)

#def compute_height(n, parents):
    # Write this function
    #max_height = 0
    # Your code here
    #return max_height


def main():
    print(result)
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
