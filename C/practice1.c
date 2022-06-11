#include<stdio.h>
//user input program
int main(){
    int length, breadth;
    // int area=length * breath;
    printf("what is the length\n->");
    scanf("%d",&length);
    printf("what is the breadth\n->");
    scanf("%d",&breadth);
    printf("the area is a %d", length*breadth);
    return 0;
}

////////////////////////////////////////////////////

#include<stdio.h>
// calculate area of circle
int main(){
    int radius=3;
    float pi=3.14;
    printf("the area of this circular is %f\n", pi*radius*radius);
    int height=3;
    printf("volume of this cylinder %f", pi*radius*radius*height);
    return 0;
}

///////////////////////////////////////////////////////

#include<stdio.h>
//calculte celsius to fahrenheit
int main(){
    float celsius=37, far;
    far=(celsius* 9/5) +32;
    printf("the vlaue of this celsius temperature in fahrenhite is %f",far);
    return 0;
}

//////////////////////////////////////////////

#include<stdio.h>
// interest in year in back
int main(){
    int principal=100, rate=4, years=1;
    int simpleinterest= (principal * rate * years)/100;
    printf("the of simple interest %d", simpleinterest);
    return 0;
}