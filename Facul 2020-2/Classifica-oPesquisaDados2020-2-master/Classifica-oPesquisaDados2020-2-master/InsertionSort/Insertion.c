
#include <math.h> 
#include <stdio.h> 
 
void insertionSort(int arr[], int n) 
{ 
    int i, chave, j; 
    for (i = 1; i < n; i++) { 
        chave = arr[i]; 
        j = i - 1; 
        while (j >= 0 && arr[j] > chave) { 
            arr[j + 1] = arr[j]; 
            j = j - 1; 
        } 
        arr[j + 1] = chave; 
    } 
} 
  
void printArray(int arr[], int n) 
{
    for (int i = 0; i < n; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
}

int main() 
{ 
    int x = (rand() % 100);
    int arr[x];
    for (int i=0; i<x;i++){
        arr[i] = (rand() % 100);
    }
    
    printArray(arr, x);
    printf("-------------------------\n");
    insertionSort(arr, x); 
    printArray(arr, x); 
  
    return 0; 
} 