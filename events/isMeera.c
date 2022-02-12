// A Meera array is defined to be an array such that for all values n in the array, the value 2*n is not in the array. So {3, 5, -2} is a Meera array because 3*2, 5*2 and -2*2 are not in the array. But {8, 3, 4} is not a Meera array because for n=4,2*n=8 is in the array.

// Write a function named isMeera that returns 1 if its array argument is a Meera array. Otherwise it returns 0.


int isMeera(int a[], int len) {
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
    if (isMeera(n)) {
        printf("The number is a Meera array\n");
    } else {
        printf("The number is not a Meera array\n");
    }
    return 0;
}

