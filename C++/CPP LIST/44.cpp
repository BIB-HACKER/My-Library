#include <iostream>
using namespace std;

//**************************pointer to object and arrow operator****************************
class complex
{
    int real, imiginary;

public:
    void getdata()
    {
        cout << " the real part is " << real << endl;
        cout << " the imiginary part is " << imiginary << endl;
    }
    void setdata(int a, int b)
    {
        real = a;
        imiginary = b;
    }
};
int main()
{
    // complex c;
    // complex *ptr = &c;
    complex *ptr = new complex;
    // (*ptr).setdata(3,6); //is exatly same as
    // (*ptr).getdata();

   /////////////////////////THIS CALL A ARROW OPERATOR////////////////////////////////////
    ptr->setdata(4, 6);
    ptr->getdata();

    return 0;
}

/*
pointer basics means:->
* = dereferance,
& = address,
(new) = new object,
*/