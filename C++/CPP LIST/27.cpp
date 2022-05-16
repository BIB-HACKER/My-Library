#include <iostream>
using namespace std;

//************************************multiple constructor overloading***********************************

class complex
{
    int a, b;

public:
    /*constructor*/ complex()
    {
        a = 47;
        b = 53;
    }

    /*constructor*/ complex(int x, int y)
    {
        a = x;
        b = y;
    }
    void ketchnumber()
    {
        cout << "your talent is -> " << a << " + " << b << "i" << endl;
    }

    /*constructor*/ complex(int x)
    {
        a = x;
        b = 0;
    }
    void printnumber()
    {
        cout << "your number is -> " << a << " + " << b << "i" << endl;
    }
};

int main()
{
    complex o3;
    o3.ketchnumber();

    complex o1(2, 3);
    o1.ketchnumber();

    complex o2(5);
    o2.printnumber();

    return 0;
}