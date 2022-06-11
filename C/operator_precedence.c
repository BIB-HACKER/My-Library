#include<stdio.h>

int main(){
    int x=4;
    int y=9;
    printf("the value of 3*x - 9*y -> %d\n", 3*x - 8*y);
    printf("the value of 3*x - 9*y -> %d\n", 3*(x - 8)*y);
    printf("the value of 3*x - 9*y -> %d\n", (3*x - 8)*y);
    printf("the value of 3*x - 9*y -> %d\n", 3*(x - 8*y));
    return 0;
}