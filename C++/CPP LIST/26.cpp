#include <iostream>
using namespace std;

//***************************PARAMETERIZD & DEFAULT CONSTRUCTOR************************

class complex
{
    int a, b;

public:
    complex(int, int);

    void printnumber()
    {
        cout << " your number is " << a << " + " << b << "i" << endl;
    }
};

complex :: complex(int x, int y)          /*-----> this is a parameterized constructor
                                       as it takes no parameter*/

{
    a = x;
    b = y;
}

int main()
{
    //implicit call
    complex a(3, 2);
 //explicit call
 complex b = complex(7, 8);

    a.printnumber();
    b.printnumber();

    return 0;
}    
