// A Bunker array is defined to be an array in which at least one odd number is immediately followed by its square. So {4, 9, 6, 7, 49} is a Bunker array because the odd number 7 is immediately followed by 49. But {2, 4, 9, 3, 15, 21} is not a Bunker array because none of the odd numbers are immediately followed by its square.

// Write a function named isBunkerArray that returns 1 if its array argument is a Bunker array, otherwise it returns 0.

// If you are programming in Java or C#, the function signature is
//    int isBunkerArray(int [ ] a)

// If you are programming in C or C++, the function signature is
//    int isBunkerArray(int a[ ], int len) where len is the number of elements in the array.


int isBunkerArray(int a[], int len) {
    int n = len-1, start=0, end=0; 
    bool odd = false; 
    if(a[0]%2!=0 || a[n]%2!=0) 
    return 0; 
    for(int i=0; i<len; i++){ 
        if(a[i]%2!=0) odd=true; 
        break; 
    }
    for(int i=0; i<len; i++){ 
        if(a[i]%2==0) start++; 
        else break; 
    }
    for(int j=n; j>=0; j--){
        if(a[j]%2==0)
        end++; 
        else break; 
    }
    if(start == end && odd)
    return 1;
    return 0;
}


int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    if (isBunkerArray(n)) {
        printf("The number is a bunker array\n");
    } else {
        printf("The number is not a bunker array\n");
    }
    return 0;
}
