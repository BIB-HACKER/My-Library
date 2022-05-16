#include <iostream>
using namespace std;

/********************************* Single Inheritance Deep Dive ********************************/ 

class base
{
    int data1; //private by default and is not innheritable
public:
    int data2;
    void setdata();
    int getdata1();
    int getdata2();
};

// THIS IS BASE CLASS OF THREE METHOD

void base ::setdata(void)
{
    data1 = 11;
    data2 = 21;
}

int base ::getdata1(void)
{
    return data1;
}

int base ::getdata2(void)
{
    return data2;
}
/////////////////////////////////////////////////////////

class derived : public base
{ //class is beang derived publically
    int data3;
public:
    void process();
    void display();
};

void derived ::process()
{
    data3 = data2 * getdata1();
}

void derived ::display()
{
    cout << " value of data 1 is " << getdata1() << endl;
    cout << " value of data 2 is " << data2 << endl;
    cout << " value of data 3 is " << data3 << endl;
}

int main()
{
    derived der;
    der.setdata();
    der.process();
    der.display();

    return 0;
}