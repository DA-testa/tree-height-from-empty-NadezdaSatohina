# python3

import sys
import threading



def compute_height(n, parents):
    def get_child_nodes(nodes_to_find, initial_input, level):
        level += 1
        child_nodes = []
        for node in nodes_to_find:
            for index, pointer in enumerate(initial_input):
                if pointer == node:
                    child_nodes.append(index)
        if child_nodes:
            level = get_child_nodes(child_nodes, initial_input, level)
        return level

    height = get_child_nodes([parents.index(-1)], parents, 0)
    return height

def main():
    input_type = input()
    if "F" in input_type:
        filename = input()
        if ".a" in filename:
            print("Files with letter 'a' are not allwed")
            return
        if "test/" not in filename:
            filename = "test/" + filename
        if "test/" in filename:    
            with open(filename) as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
                height = compute_height(n, parents)
    elif "I" in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)

    print(height)


#def compute_height(n, parents):
    # Write this function
    #max_height = 0
    # Your code here
    #return max_height


#def main():
   
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
