#include <iostream>
using namespace std;

// int sum(int a, int b){
//     int c = a+b;
//     return c;
//}

                 //*****************function prototype*********************

// int sum(int a, int b); //----------->acceptable
// int sum(int a, b); //-----------> not acceptable
int sum(int, int);   // -----------> acceptable
// void g();

int main()
{
    int a;
    int b;
    cout << " the first value is " << endl;
    cin >> a;
    cout << " the second value is " << endl;
    cin >> b;
    // num1 and num2 are actual parameter
    cout << "the sum value is " << sum(a, b);  
    // void g();  

    return 0;
}

int sum(int a, int b)
// formal parameter a and b will be taking values from actual parameter num1 and num2
{
    int c = a + b;
    return c;  
}

// void g(){
//     cout<<"you are best ";
// }