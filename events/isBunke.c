
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


int isBunkerArray(int *arr, int n) {
    int i, j, k, max, count, maxCount;
    char str[100];
    char *p;
    if (n < 0) {
        return 0;
    }
    if (n == 0) {
        return 0;
    }
    sprintf(str, "%d", n);
    p = str;
    maxCount = 0;
    max = 0;
    while (*p != '\0') {
        count = 0;
        for (i = 0; i < 10; i++) {
            for (j = 0; j < strlen(p); j++) {
                if (i == *(p + j) - '0') {
                    count++;
                }
            }
        }
        if (count > maxCount) {
            maxCount = count;
            max = *p - '0';
        }
        p++;
    }
    if (maxCount == 1) {
        return 0;
    }
    return 1;
}


// main function to print if a number ifBunkerArray or not
int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    if (isBunkerArray(n)) {
        printf("The number is a binker array\n");
    } else {
        printf("The number is not a binker array\n");
    }
    return 0;
}

// // The function signature is int isBunkerArray(int a[], int len) where len is the number elements in the array.
// // i

// int isMeera(int a[]) {
//     int n = a.length-1, start=0, end=0; 
//     boolean odd = false; 
//     if(a[0]%2!=0 || a[n]%2!=0) 
//     return 0; 
//     for(int i=0; i<a.length; i++){ 
//         if(a[i]%2!=0) odd=true; 
//         break; 
//     }
//     for(int i=0; i<a.length; i++){ 
//         if(a[i]%2==0) start++; 
//         else break; 
//     } 
//     for(int j=n; j>=0; j--){
//         if(a[j]%2==0)
//         end++; 
//         else break; 
//     } 
//     if(start == end && odd) 
//     return 1; 
//     return 0; 
//     }


// int main() {
//     int n;
//     printf("Enter a number: ");
//     scanf("%d %d", &n);
//     if (isMeera(n)) {
//         printf("The number is a binker array\n");
//     } else {
//         printf("The number is not a binker array\n");
//     }
//     return 0;
// }
