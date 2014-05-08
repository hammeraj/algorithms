#!/usr/bin/env python

"""Bubblesort algorithms and tests"""
"""Explores bubblesort and 3 variations"""
"""Austin Hammer"""
"""5.7.2014"""



################################################
# bubblesort(array)
# A function that sorts a list using bubblesort
# algorithm. Worst and average cases are O(n^2).
# Best case is O(n)-the list is already sorted.
# It is an in-place sort, and stable
def bubblesort(arr):
    sorted = False
    comp = 0
    
    while not sorted:
        count = 0
        for x in range(0, len(arr)-1):
            comp += 1
            if(arr[x] > arr[x+1]):
                temp = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = temp
                count += 1
        if(count == 0):
            sorted = True
    print("Comparisons : " + str(comp))

################################################
# optbubblesort(array)
# An attempt to optimize bubblesort by observing
# that the largest element in a passthrough will
# always end up at the end of the list, so we can
# reduce the number of elements looked at each time
def optbubblesort(arr):
    sorted = False
    n = len(arr)-1
    comp = 0
    
    while not sorted:
        count = 0
        for x in range(0, n):
            comp += 1
            if(arr[x] > arr[x+1]):
                temp = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = temp
                count += 1
        
        if(count == 0):
            sorted = True

        n = n-1

    print("Comparisons : " + str(comp))

################################################
# moreoptbubblesort(array)
# An attempt to optimize bubblesort again by
# observing that everything past the last swapped
# element will be in order, so we can reduce the
# items swapped by more than one every passthrough
def moreoptbubblesort(arr):
    sorted = False
    n = len(arr)-1
    comp = 0
    
    while not sorted:
        count = 0
        for x in range(0, n):
            comp += 1
            if(arr[x] > arr[x+1]):
                temp = arr[x]
                arr[x] = arr[x+1]
                arr[x+1] = temp
                count += 1
                n = x
        
        if(count == 0):
            sorted = True

    print("Comparisons : " + str(comp))

################################################
# combsort(array)
# A variation of bubblesort which uses a comparison
# space greater than one. It attempts to address the
# issue of 'turtles' - small values near the end of
# the array. A gap shrink factor of 1.3 was determined
# to be the most efficient. Best case is still O(n) and
# worst case is still O(n^2), but average case is
# n^2 divided by 2^p, where p is the number of times
# the gap is reduced from x to 1. Can be comparable
# to more efficient sorting algorithms.
def combsort(arr):
    shrink = 1.3
    gap = len(arr)-1
    swapped = False
    comp = 0
 
    while ((gap > 1) or swapped):
        if (gap > 1):
            gap = (int)(gap / shrink)
         
        swapped = False
 
        for x in range(0, len(arr)-1):
            if(gap + x > len(arr)-1):
                break
            comp+=1
            if (arr[x] - arr[x + gap] > 0):
                swap = arr[x]
                arr[x] = arr[x + gap]
                arr[x + gap] = swap
                swapped = True
    print("Comparisons : " + str(comp))


def main():
    array = [4,1,5,9,3,6,7,2,8,0]
    bubblesort(array)
    print(array)
    array = [4,1,5,9,3,6,7,2,8,0]
    optbubblesort(array)
    print(array)
    array = [4,1,5,9,3,6,7,2,8,0]
    moreoptbubblesort(array)
    print(array)
    array = [4,1,5,9,3,6,7,2,8,0]
    combsort(array)
    print(array)


if __name__ == "__main__":
    main()
        
    
