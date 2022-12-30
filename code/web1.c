#include<stdio.h>

int main(){
    int i=1;
    int j=0;
    while (i<100) i++; j+=2;
    
    printf("value of i = %d, and j=%d", i,j);
    return 0;
}