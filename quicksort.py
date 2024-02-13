#!/usr/bin/python3

""" https://www.geeksforgeeks.org/python-program-for-quicksort/ """

import time

# generate random integer values
from numpy.random import seed
from numpy.random import randint

# Function to find the partition position
def partition(arr, p, r):
 
    # choose the rightmost element as pivot
    x = arr[r]
 
    # pointer for greater element
    i = p - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(p, r):
        if arr[j] <= x:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (arr[i], arr[j]) = (arr[j], arr[i])
 
    # Swap the pivot element with the greater element specified by i
    (arr[i + 1], arr[r]) = (arr[r], arr[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
def quickSort(arr, p, r):
    if p < r:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        q = partition(arr, p, r)
 
        # Recursive call on the left of pivot
        quickSort(arr, p, q - 1)
 
        # Recursive call on the right of pivot
        quickSort(arr, q + 1, r)

# main
#def main():
# seed random number generator
seed(1)

# generate some integers
size = 1000000

#py_output = open('py_out.txt', 'w')

#s = "size:, time(ms):, time(ns):"
#py_output.write(s)
print("size:, time(ms):, time(ns):")

while (size <= 2147483647/2):
    arr = randint(0, 1000000, size)
    # start clock
    start = time.time()
    # sort
    quickSort(arr, 0, size - 1)
    # end clock
    end = time.time()
    cpu_time_used = end - start

    print("%d, %f, %f"%(size, cpu_time_used*1000, cpu_time_used*1000000000))

    size += 1000000

#file1.close(py_output)
print("done!")
