#include<stdio.h>

int main(){

    int a,b;
    printf("enter the value of a\n->");
    scanf("%d", &a);  // user input scanf(&i==addres of i)
    printf("enter the value of b\n->");
    scanf("%d", &b);  // user input scanf(&j==addres of j)
    printf("the sum of a and b is %d",a+b);
    return 0;
}