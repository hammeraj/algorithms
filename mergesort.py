#!/usr/bin/env python

"""Mergesort algorithms and tests"""
"""Austin Hammer"""
"""5.7.2014"""

comp = 0

##############################################
# An algorithm that divides up an array into
# progressively smaller parts, until it is left
# with arrays of only one element. Then it 
# recursively merges the lists back together,
# sorting as it goes. It is not an in-place
# algorithm.
def mergesort(array):
    if(len(array) <= 1):
        return array

    left = []
    right = []
    mid = (int)(len(array) / 2)
    for x in range(0, mid):
        left.append(array[x])
    for x in range(mid, len(array)):
        right.append(array[x])
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


##############################################
# The merging part of the algorithm. Comparisons
# are done here. If the algorithm detects one
# list has finished merging, it adds the rest of
# the elements of the other list (which should
# already be sorted) and returns. Equality ties
# go to the B side, not a stable algo
def merge(A, B):
    result = []
    idxA = 0
    idxB = 0
    while(idxA < len(A) or idxB < len(B)):
        if(idxB == len(B)):
           for x in range(idxA, len(A)):
               result.append(A[x])
           return result
        if(idxA == len(A)):
           for x in range(idxB, len(B)):
               result.append(B[x])
           return result
        if(A[idxA] <= B[idxB]):
            result.append(A[idxA])
            idxA+=1
            comp_add()
        elif(A[idxA] > B[idxB]):
            result.append(B[idxB])
            idxB+=1
            comp_add()
    return result;

def comp_add():
    global comp
    comp += 1

def print_comp():
    print(comp)
        

def main():
    array = [4,1,5,9,3,6,7,2,8,0]
    newarray = mergesort(array)
    print(newarray)
    print_comp()

if __name__ == "__main__":
    main()
