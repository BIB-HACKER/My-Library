#include<iostream>
using namespace std;

//******************************initialization list**********************************

/*
syntax for initialization list in constructor:
constructor (argument_list) : initialization-section
{
    assigment + other code;
}
*/

class test
{
    int b;
    int a;

    public:
    // test(int i, int j) : a(i), b(j)
    // test(int i, int j) : a(i), b(j+i)
    // test(int i, int j) : a(i*j), b(j+i)
    // test(int i, int j) : a(i*j), b(j+a)
    // test(int i, int j) : a(i*j), b(i+a)
    // test(int i, int j) :  b(j), a(b+i) --> red flag this will create problem a will be initialized first
    test(int i, int j) : /*a(i),*/ b(j+i) 
    {
        a = i;
        // b = j;
    
        cout << " constructor executed "<< endl;
        cout << " value of a is "<<a<< endl;
        cout << " value of b is "<<b<< endl;
    }
};
int main(){
  test t(5,8);  
    return 0;
}