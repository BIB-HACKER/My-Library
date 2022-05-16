#include <iostream>

using namespace std;

int main()
{

    int a = 4;
    int b = 5;
    cout << " operator in c++:" << endl;
    cout << " folowing are the types of operator in c++:" << endl;
    //  Arithmetic operator
    cout << " the value of a+b is " << a + b << endl;
    cout << " the value of a-b is " << a - b << endl;
    cout << " the value of a/b is " << a / b << endl;
    cout << " the value of a*b is " << a * b << endl;
    cout << " the value of a%b is " << a % b << endl;
    cout << " the value of a++ is " << a++ << endl;
    cout << " the value of a-- is " << a-- << endl;
    cout << " the value of ++a is " << ++a << endl;
    cout << " the value of --a is " << --a << endl;
    cout << " the value of ++a is " << ++a << endl;
    cout<<endl;


    /*assigment operators --> used to assigen values to variables
    int a = 7, b = 9;
    char h = i;

    COMPARISION OPERATOR*/
    cout << " the following of comparision operator in c++"<<endl;
    cout << " the value of a == b is " << (a == b) << endl;
    cout << " the value of a != b is " << (a != b) << endl;
    cout << " the value of a >= b is " << (a >= b) << endl;
    cout << " the value of a <= b is " << (a <= b) << endl;
    cout << " the value of a > b is " << (a > b) << endl;
    cout << " the value of a < b is " << (a < b) << endl;
    cout<<endl;

    /* logical operator*/

    cout<<" following are the logical operator is c++"<<endl;    
    cout<<" following are the logical operator ((a==b) && (a<b)) is c++ "<<((a==b) && (a<b))<<endl;    
    cout<<" following are the logical operator ((a==b) || (a<b)) is c++ "<<((a==b) || (a<b))<<endl;    
    cout<<" following are the logical operator (!(a==b)) is c++ "<<(!(a==b))<<endl;    


    return 0;
}