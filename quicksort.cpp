//
//  quicksort.cpp
//  
//
//  Created by Austin Hammer on 11/17/14.
//
//

#include "quicksort.h"
#include <iostream>

int main()
{
    int arr[10] = {5,7,4,3,6,9,1,2,8,0};
    quicksort(arr,0,9);
    
    for(int i; i<10; i++)
    {
        std::cout << arr[i] << " ";
    }
}

void quicksort(int * arr,int left, int right)
{
    if(left < right)
    {
        int idx = partition(arr,left,right);
        quicksort(arr, left, idx-1);
        quicksort(arr,idx+1,right);
    }
}

int partition(int * arr,int left, int right)
{
    int endloc = left;
    
    int pivot = (left + right)/2;
        
    swap(arr, right, pivot);

    for(int i = left; i<right; i++)
    {
        if(arr[i]<arr[right])
        {
            swap(arr, i, endloc);
            endloc++;
        }
    }
    swap(arr, right, endloc);
    return endloc;
}

void swap(int * arr, int a, int b)
{
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
