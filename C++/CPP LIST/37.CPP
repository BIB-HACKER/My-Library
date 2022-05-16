#include <iostream>
#include <cmath>
using namespace std;

/*
CREAT calculator:
  1. simplecalculator - take input of 2 numbers using a utility function and performs
   +, -, *, / and display the rusults using another function.
  2. scientificcalculator - takes input of 2 number using a utility functions and perfoms any
    four scientific operation of your choice and display the results using another function.

    creat another class hybridcalculator and inherit it using these 2 classes :
    Q1. what type of inheritance are you using?
    Q2. which mode of inheritance are you using?
    Q3. create an object of hybridcalculator and display results of simple and scientific
        calculator.
    Q4. how is the resuablity implemented.
*/

class simplecalculator
{
    int a, b;

public:
    void getdatasimple()
    {
        cout << " enter the value of a " << endl;
        cin >> a;
        cout << " enter the value of b " << endl;
        cin >> b;
    }

    void performoperationsimple()
    {
        cout << " the value of a + b is " << a + b << endl;
        cout << " the value of a - b is " << a - b << endl;
        cout << " the value of a * b is " << a * b << endl;
        cout << " the value of a / b is " << a / b << endl;
    }
};

class scientificCalculator
{
    int a, b;

public:
    void getdatascientific()
    {
        cout << " enter the value of a " << endl;
        cin >> a;
        cout << " enter the value of b " << endl;
        cin >> b;
    }

    void performoperationscientific()
    {
        cout << " the value of cos(a) is " << cos(a) << endl;
        cout << " the value of sin(a) is " << sin(a) << endl;
        cout << " the value of exp(a) is " << exp(a) << endl;
        cout << " the value of tan(a) is " << tan(a) << endl;
    }
};

class hybridcalculator : public simplecalculator, public scientificCalculator
{
};

int main()
{
    /*simplecalculator cal;
    cal.getdata();
    cal.performoperation();*/

    hybridcalculator cal;
    cal.getdatascientific();
    cal.performoperationscientific();
    cal.getdatasimple();
    cal.performoperationsimple();

    return 0;
}