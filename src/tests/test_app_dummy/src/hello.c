#include <stdio.h>
#include "uselessCmp.h"
#include "uselessL2Cmp.h"
#include "uselessL0Cmp.h"
#include "uselessServicesCmp.h"


int sum(int a, int b) {
    return a + b;
}

void bubbleSort(int arr[], int n) {
    // Bubble sort algorithm
    int i, j;
    int a, b;

    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap elements
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}



void printArray(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main(void) {
    int a = 5;
    int b = 3;
    int result = sum(a, b);
    
    printf("Hello, world!\n");
    printf("Sum of %d and %d is: %d\n", a, b, result);
    
    // Bubble sort demonstration
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    printArray(arr, n);
    
    bubbleSort(arr, n);
    
    printf("Sorted array: ");
    printArray(arr, n);
    
    // Execute uselessCmp functions
    printf("\n--- uselessCmp functions ---\n");
    uselessCmp_PrintHello();
    uselessCmp_PrintVariant();
    
    // Execute uselessL2Cmp functions
    printf("\n--- uselessL2Cmp functions ---\n");
    uselessL2Cmp_PrintHello();
    uselessL2Cmp_PrintVariant();
    
    // Execute uselessL0Cmp functions
    printf("\n--- uselessL0Cmp functions ---\n");
    uselessL0Cmp_PrintHello();
    uselessL0Cmp_PrintVariant();
    
    // Execute uselessServicesCmp functions
    printf("\n--- uselessServicesCmp functions ---\n");
    uselessServicesCmp_PrintHello();
    uselessServicesCmp_PrintVariant();
    
    return 0;
}

