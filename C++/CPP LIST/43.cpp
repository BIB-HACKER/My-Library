//***********************Revisiting Pointers**********************************

#include <iostream>
using namespace std;

// WHAT IS POINTER?
//=> where{*(ptr/jaj)},datatype(int,char,float) address is stored, thats the call is a pointer.

int main()
{
    int a = 5;
    int *jaj = &a;
    *jaj = 888;

    cout << " the value of a is " << *(jaj) << endl;

    //new keyword operator-->
    // int *p = new int(40);
    float *j = new float(40.4324);
    cout << " the value at adress p is " << *(j) << endl;

//dynamic new keyword to block of memory allocate-->
    int *foll = new int[4];
    foll[0] = 10;
    *(foll+1) = 40;
    foll[2] = 20;
    foll[3] = 70;
    // delete[] arr;
    cout << " the value of foll[0] is " << foll[0] << endl;
    cout << " the value of foll[1] is " << foll[1] << endl;
    cout << " the value of foll[2] is " << foll[2] << endl;
    cout << " the value of foll[3] is " << foll[3] << endl;

    //delete operator

    return 0;
}