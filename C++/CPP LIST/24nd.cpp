#include <iostream>
using namespace std;

class c2; //c2 is decleration

class c1
{
    int val1;

    friend void exchange(c1 & /*(& is call a referance)*/, c2 & /*(& is call a referance)*/);

public:
    void indata(int a)
    {
        val1 = a;
    }
    void display(void){
        cout<< val1 <<endl;
    }
};   //---------------------------------------------------------------------------------------

class c2
{
    int val2;

    friend void exchange(c1 & /*(& is call a referance)*/, c2 & /*(& is call a referance)*/);

public:
    void indata(int a)
    {
        val2 = a;
    }
      void display(void){
        cout<< val2 <<endl;
    }
};   //----------------------------------------------------------------------------------------------

//this bellow line call a referance line (& is referance value)
//*******trick to swap 2 number !!!!!!! a and b !!!!!!;
/*tem = a;
a = b;
b = tem;*/

void exchange(c1 & /*(& is call a referance)*/ x, c2 & /*(& is call a referance)*/ y)
{
    int tem = x.val1;
    x.val1 = y.val2;
    y.val2 = tem;
}  //------------------------------------------------------------------------------------------------

int main()
{
    c1 oc1;
    c2 oc2;

    oc1.indata(4);
    oc2.indata(6);
    exchange(oc1, oc2);

    cout << " the value of c1 after exchange becomes--> ";
    oc1.display();
    cout << " the value of c2 after exchange becomes--> ";
    oc2.display();
    return 0;
}   