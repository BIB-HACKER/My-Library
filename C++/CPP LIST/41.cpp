// *********************************** Constructor in Derived class ******************************

#include <iostream>
using namespace std;
/*
case1:
class b : public a{
    first b: publilc a
};
*/

class base1
{
    int data1, data11;

public:
    base1(int i, int l)
    {
        data1 = 33;
        data11 = l;
        cout << " base1 class constructor called " << endl;
    }
    void printdatabase1(void)
    {
        cout << "the value of data1 is " << data1 << endl;
        cout << "the value of data11 is " << data11 << endl;
    }
};

class base2
{
    int data2;

public:
    base2(int i)
    {
        data2 = i;
        cout << " base2 class constructor called " << endl;
    }
    void printdatabase2(void)
    {
        cout << "the value of data2 is " << data2 << endl;
    }
};

class derived : public base1, public base2
{
    int derived1, derived2;

public:
    derived(int a, int y, int b, int c, int d) : base1(a, y), base2(b)
    {
        derived1 = c;
        derived2 = d;
        cout << " derived class constructor called " << endl;
    }
    void printdataderived(void)
    {
        cout << " the value of derived1 is " << derived1 << endl;
        cout << " the value of derived2 is " << derived2 << endl;
    }
};
int main()
{
    derived papon(1, 2, 3, 4, 5);
    papon.printdatabase1();
    papon.printdatabase2();
    papon.printdataderived();
    return 0;
}