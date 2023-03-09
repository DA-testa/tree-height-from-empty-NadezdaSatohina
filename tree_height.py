# python3

import sys
import threading



def compute_height(n, parents):
    heights = [-1] * n

    def dd(i):
        if parents[i] == -1:
            return 0

        if heights[i] > -1:
            return heights[i]

        heights[i] = 1 + dd(parents[i])

        return heights[i]

    for i in range(n):
        heights[i] = dd(i)

    return 1 + max(heights)

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

    height = compute_height(n, parents) #create list of tuples

    print(height)
    return height




# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
