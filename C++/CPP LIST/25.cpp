//********************************DEFAULT CONSTRUCTOR**********************************

#include <iostream>
using namespace std;

class complex
{
    int a;
    int b;

public:
   
   /*
    # what is constructor?????
   -> when class name (complex) and function name (complex) are same, then clled is a constructon function
     and thats why it is automaticaly run.

   # why used a constructior?
   -> object valus set, then we used a constructior*/

    complex(void); //constructor declaration

   void printnumber()
    {
        cout << " your number is " << a << " + " << b << "i" << endl;
    }
};

complex ::complex(void) //----->this is a default constructor as it takes 2 parameters
{
    a = 10;
    b = 40;
}
int main()
{

   /*OBJECT*/ complex c1, c2, c3; /*VARIABLE NAMES*/;

    c1.printnumber();
    c2.printnumber();
    c3.printnumber();
    return 0;
}

/*
characteristic of constructor---->

1.it should be declared in the public section of the class
2. they are automatically invoked whwnever the object is created
3. they cannot return values and do not have return types
5. it can have default arguments
6. they cannot refer to their address
*/ 