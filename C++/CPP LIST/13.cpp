
//********************call by value & call by reference**********************

#include<iostream>
using namespace std;

int sum (int num1,int num2){
    int c = num1+num2;
    return c;
}
//this will not swap a and b
void swap(int a, int b){  //g  a  b 
    int g = a;           // 5  5  8 
    a = b;              //  5  8  8
    b = g;              //  5  8  5
}

//call by reference by pointer
void swapPointer(int* a, int* b){  //g  a  b 
    int g = *a;                   // 5  5  8 
    *a = *b;                     //  5  8  8
    *b = g;                      //  5  8  5
    }                     

    void swapreferenceVar(int &a, int &b){  //g  a  b 
    int g = a;                   // 5  5  8 
    a = b;                     //  5  8  8
    b = g;                      //  5  8  5
    }                     

    // int & swapreferenceVar(int &a, int &b){  //g  a  b 
    // int g = a;                   // 5  5  8 
    // a = b;                     //  5  8  8
    // b = g;        
    // return a;              //  5  8  5
    // }                     

int main(){
     int x = 5;
     int y = 8;
    //  cout<<" the total number of a and b is "<<sum(x, y)<<endl;
    cout<<" the value of x is "<<x<<" and the value of y is "<<y<<endl;
    //  swap(x, y);(this will not swap a and b = not working)
    // swapPointer(&x, &y);    //THIS WILL SWAP A AND B USING POINTER REFERENCE
    //  cout<<" the value of x is "<<x<<" and the value of y is "<<y<<endl;   
    swapreferenceVar(x, y);    //THIS WILL SWAP A AND B USING REFERENCE VARIABLE
     cout<<" the value of x is "<<x<<" and the value of y is "<<y<<endl;   
    // swapreferenceVar(x, y) = 555;    
    //  cout<<" the value of x is "<<x<<" and the value of y is "<<y<<endl;      

    return 0;
}