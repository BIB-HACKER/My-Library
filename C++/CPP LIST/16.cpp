#include<iostream>
using namespace std;


       //********************************* function OVERLOADING**********************************
       
int/*call return value is int*/ add(int a, int b){
    return a*b;
}

int/*call return value is int*/ add(int a, int b, int c)/*the values called a argument*/{
    return (a/b)+c;
}
// calculate the volume of a cylinder
int volume(double r, int h){
    return (3.14 * r * r * h);
}
// calculate the volume of a cube
int volume(int a){
    return (a * a * a);
}
// rectengular box
int volume(int l, int a, int h){
    return (l*a*h);
}
int main(){
    cout<<" the add of 6 and 9 is "<<add(6,9)/*argument*/<<endl;
    cout<<" the add of 3,6 and 9 is "<<add(3, 6 ,9)/*argument*/<<endl;
    cout<<" the volume of cylinder is "<<volume(3, 6)/*argument*/<<endl;
    cout<<" the volume of a cube value is "<<volume(3)/*argument*/<<endl;
    cout<<" the rectengular box value is "<<volume(3, 6 ,9)/*argument*/<<endl;

    return 0;
}  