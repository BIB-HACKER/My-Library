#include<stdio.h>
#include<math.h>

// operands can be int/float etc.
// (+,-,/,* are arithmatic operators)

int main(){
    int a =4;
    int b = 6;
    int x;
    x = a*b;   // legal
    // a*b=x; // illegal
    printf("the value of a + b -> %d\n", a + b);
    printf("the value of a - b -> %d\n", a - b);
    printf("the value of a / b -> %d\n", a / b);
    printf("the value of a * b -> %d\n", a * b);
    printf("the vlaue of z ->%d\n",x);

    printf("5 when divided by 2 leaves a areminder of %d\n",5%2);
    printf("-5 when divided by 2 leaves a areminder of %d\n",-5%2);
    printf("5 when divided by -2 leaves a areminder of %d\n",5%-2);

    // printf("the value of 4 * 5 is %d\n",(4)(5));  --> wrong , here no operator asume to paresent.
    printf("the value of 4 * 5 is %d\n",(4)*(5));

    //this is no operator to paerform exponentaion in c
    printf("the value of 4^5 is %d\n",4^5);  // will not produce 4 to the power 5
    printf("the value of 2 to the power 5 is %f\n",pow(2,5));

    printf("the value of 6 + 5.5 is %f\n", 6+5.5);
    printf("the value of 6 + 5 is %d\n", 6+5);
    printf("the value of 6.4 + 5.6 is %f\n", 6.4+5.6);
    float f=5;
    printf("%d\n", 5/2);
    printf("%f\n", f/2);
    printf("%d\n", 2/5);
    printf("%f\n", 2.0/5);

    float r = 3;
    printf("%f",r/9);
    return 0;
}