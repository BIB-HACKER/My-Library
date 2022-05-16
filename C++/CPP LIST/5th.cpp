#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    // int a = 44;
    // cout << " the valiue was: "<<a<<endl;

    // a = 77;
    // cout<<" the value is "<<a;

    // ******************constants c++******************

    // const int c = 99;
    // cout<<" the value was "<<c<<endl;

    // c = 11;       //this c value get a error, because c is a constant
    // cout <<" the value is "<<c;

    // ****************mainpuletors c++*********************

    // int a = 12;
    // int b = 3456;
    // int c = 178765;
    // cout << " the value of a wiehout setw is: " << a << endl;
    // cout << " the value of b wiehout setw is: " << b << endl;
    // cout << " the value of c wiehout setw is: " << c << endl;

    // cout << " the value of a ia: " <<setw(6) <<a << endl;
    // cout << " the value of b ia: " <<setw(6) <<b << endl;   
    // cout << " the value of c ia: " <<setw(6) <<c << endl;   

// ******************operator precedence**************

int a= 6;
int b = 7;
int c = ((((a*9)+b)-45)+12);
cout<<c;

    return 0;
}