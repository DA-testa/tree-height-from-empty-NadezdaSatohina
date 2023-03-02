# python3

import sys
import threading

import numpy as np

def compute_height(adj_list):
    def dfs(node, depth):
        nonlocal max_depth
        if not adj_list[node]:
            max_depth = max(max_depth, depth)
        else:
            for child in adj_list[node]:
                dfs(child, depth+1)

    max_depth = 0
    dfs(0, 0)
    return max_depth

max_children = max(len(children) for children in adj_list.values())
adj_array = np.full((n, max_children), -1)
for i, children in adj_list.items():
    adj_array[i,:len(children)] = children


def main():
    input_type = input()

    if "F" in input_type:
        filename = input()
        if ".a" in filename:
            return
        if "test/" not in filename:
            filename = "test/" + filename
        if "test/" in filename:    
            with open(filename) as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
                height = compute_height(adj_list)
    elif "I" in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(adj_list)

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
