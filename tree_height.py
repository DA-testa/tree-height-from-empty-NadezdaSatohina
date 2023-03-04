# python3

import sys
import threading



def compute_height(n, parents):
    def get_child_nodes(nodes_to_find, node_input, level):
        level += 1
        child_nodes = []
        removable_nodes = []
        for og_index, parent in nodes_to_find:
            for index, node in enumerate(node_input):
                if node[1] == og_index:
                    child_nodes.append(node)
                    removable_nodes.append(index)
                    
        removable_nodes.sort(reverse = True)
        for index in removable_nodes:
            del node_input[index]
        if child_nodes:
            level = get_child_nodes(child_nodes, node_input, level)
        return level

    root_index = [i[0] for i in parents if i[1] == -1][0]
    nodes_to_find = parents.pop(root_index)
    height = get_child_nodes([nodes_to_find], parents, 0)
    return height

def main():
    input_type = input("Input Type: ")
    if "F" in input_type:
        filename = input("Input File Name: ")
        if "a" in filename:
            print("Files with letter 'a' are not allwed")
            return
        if "test/" not in filename:
            filename = "test/" + filename
        if "test/" in filename:    
            with open(filename) as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
    elif "I" in input_type:
        n = int(input("Input Number of Nodes: "))
        parents = list(map(int, input("Input Nodes: ").split()))
    
    node_input = []
    for index, node in enumerate(parents):
        node_input.append((index, node))
    height = compute_height(n, node_input) #create list of tuples

    print(height)
    return height




# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
