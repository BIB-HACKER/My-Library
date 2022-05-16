//*****************************friend classes & member friend function*******************************

#include<iostream>
using namespace std;

class complex; //forward declaration

class calculator
{
    public:
    int add(int a, int b){
        return (a+b);
    }
    
    int sumrealcomplex(complex, complex );
    int sumcompcomplex(complex, complex );
};

class complex{
    int a;
    int b;
    public:

    // friend int calculator :: sumrealcomplex(complex, complex);
    // friend int calculator :: sumcompcomolex(complex, complex);
  
  /*********************************/  friend class calculator; /// this line allowed evrything a class function access

    void setnumber(int m1, int m2)//this line call is member of class
    {
        a = m1;
        b = m2;
    }
    // bellow the line means FRIEND function is allowed to UNKNOWN fuction do anything access with my privt part
      
    void printnumber()//this line call is member of class
    {
        cout<<" your number is "<<a<<" + "<<b<<endl;
    }
};
 // declear
int calculator :: sumrealcomplex(complex o1, complex o2){
    return (o1.a + o2.a);
}
int calculator :: sumcompcomplex(complex o1, complex o2){
    return (o1.b + o2.b);
}


int main(){
    complex o1, o2;
    o1.setnumber(3, 6);
    o2.setnumber(5, 9);
    calculator calc;
    int res = calc.sumrealcomplex(o1, o2);
    cout<<" the sum of real part of o1 ane o2 is "<<res<<endl;
    int reso = calc.sumcompcomplex(o1, o2);
    cout<<" the sum of realo part of o1 ane o2 is "<<reso<<endl;


     return 0;
}  