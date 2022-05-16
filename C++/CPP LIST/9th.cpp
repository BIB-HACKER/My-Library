#include<iostream>
using namespace std;

int main(){
    
    //**************what is pointer?----------------->data type which holds the address of other data type

    int a =5;
    int* b;
    b = &a;
    
   //cout<<b;
    
    //  &a ------>(address of) operator
    
    cout<<"The address of a is "<<&a<<endl;
    cout<<"The address of b is "<<b<<endl;

    // * ------>(vbalue store) dereferance address operator

    cout<<"the value of b is "<<* b;
   
    return 0;    
}