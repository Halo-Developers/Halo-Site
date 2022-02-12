// write a function named maxOccurDigit that returns the digit that occur the most
// in a given integer.
//
// For example, maxOccurDigit(1234) should return 4.
//
// If there are multiple digits that occur the most, return the last one.
//
// If the number is 0, return 0.
//
// If the number is negative, return -1.
//
// If the number is not a valid integer, return -1.
//
// You may assume that the number is non-negative.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// int maxOccurDigit(int n) {
//     int i, j, k, max, count, maxCount;
//     char str[100];
//     char *p;
//     if (n < 0) {
//         return -1;
//     }
//     if (n == 0) {
//         return 0;
//     }
//     sprintf(str, "%d", n);
//     p = str;
//     maxCount = 0;
//     max = 0;
//     while (*p != '\0') {
//         count = 0;
//         for (i = 0; i < 10; i++) {
//             for (j = 0; j < strlen(p); j++) {
//                 if (i == *(p + j) - '0') {
//                     count++;
//                 }
//             }
//         }
//         if (count > maxCount) {
//             maxCount = count;
//             max = *p - '0';
//         }
//         p++;
//     }
//     return max;
// }


// int main() {
//     int n;
//     printf("Enter a number: ");
//     scanf("%d", &n);
//     printf("The max digit is %d\n", maxOccurDigit(n));
//     return 0;
// }


//
// Created by zheng_chen on 5/31/19.
//
//#include <stdio.h>
//#include <stdlib.h>
//#include <string.h>
//
//
//int maxOccurDigit(int n) {
//    int i, j, k, max, count, maxCount;
//    char str[100];
//    char *p;
//    if (n < 0) {
//        return -1;
//    }


int maxOccurDigit(int n) {
    int rem1 = 0, count = 0, rem2 = 0,
            temp = 0, maxCount = 0, maxNumber = 0;
            bool flag = false;

            if (n < 0)
                n = -1 * n;
            while (n != 0)
            {
                rem1 = n % 10;
                count = 1;
                temp = n = n / 10;
                while (temp != 0)
                {
                    rem2 = temp % 10;
                    temp = temp / 10;
                    if (rem1 == rem2)
                    {
                        count++;
                    }
                }
                if (maxCount < count)
                {
                    maxCount = count;
                    maxNumber = rem1;
                    flag = true;
                }
                else if (maxCount == count)
                {
                    flag = false;
                }
            }
            if (!flag) return -1;
            return maxNumber;
}



int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("The max digit is %d\n", maxOccurDigit(n));
    return 0;
}