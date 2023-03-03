# python3

import sys
import threading


def compute_height(n, parents):  
    adj_list = [[] for _ in range(n)]
    for i, par in enumerate(parents):
        if par != -1:
            adj_list[par].append(i)

    max_height = 0
    stack = [(None, parents.index(-1), 0)]
    while stack:
        parent, node, height = stack.pop()
        if height > max_height:
            max_height = height
        for child in adj_list[node]:
            if child != parent:
                stack.append((node, child, height + 1))

    return max_height

def main():
    input_type = input()

    if "F" in input_type:
        filename = input()
        if "a" in filename or "A" in filename:
            return
        if not filename.startswith("test/"):
            filename = "test/" + filename
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
