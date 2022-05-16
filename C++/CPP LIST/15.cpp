#include<iostream>
using namespace std;

            //********************recursion*************************
int factorial(int n){
    if (n<=1){
    return 1;
    }
    return n*factorial(n-1);
}

//step by step calculation of factorial
//factorial(4) = 4* factorial(4-1 = 3);
//factorial(4) = 4*3 factorial(3-1 = 2);
//factorial(4) = 4*3*2 factorial(2-1 = 1);
//factorial(4) = 4*3*2*1 = 24

int main(){
    int a

    cout<<" enter the number "<<endl;
    cin>>a;
    cout<<"the factor of a is  "<<factorial(a)<<endl;

    return 0;

}    