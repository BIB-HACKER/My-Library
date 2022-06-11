#include<stdio.h>
#include<math.h>

int main(){
    // int a; b=a; // error
    int a; int b=a; 

    int v=3^3; //output = 0
    printf("%f\n",pow(3,3));

    // char dt='yughg'; --> error
    char dt='y';

    0.33; // gcc belive all decimail number are DUBBLE
    printf("%c\n",dt);

    float d= 3.0/8;
    printf("%f\n",d);

    int num;
    printf("enter the number\n->");
    scanf("%d", &num);
    printf("divisibility test returns: %d\n", num%100); // its output is reminder.

    int x=2 , y=3, z=3, k=1;
    int result = 3 * x / y - z + k;
    // 3 * 2 / 3 - 3 + 1
    // 6 / 3 - 3 + 1
    // 2 - 3 + 1                // arithmatics operator work on  LEFT TO RIGHT 
    // -1 + 1               
    // 0
    printf("%d", result);
    return 0;
}