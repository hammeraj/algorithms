//
//  quicksort.h
//  
//
//  Created by Austin Hammer on 11/17/14.
//
//

#ifndef ____quicksort__
#define ____quicksort__

#include <stdio.h>

void quicksort(int * arr,int left, int right);
int partition(int * arr,int left, int right);
void swap(int * arr, int a, int b);

#endif /* defined(____quicksort__) */
