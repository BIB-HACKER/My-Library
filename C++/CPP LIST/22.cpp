#include<iostream>
using namespace std;

//************************************friend function******************************************

class complex{
    int a;
    int b;
    public:
    void setnumber(int m1, int m2)//this line call is member of class
    {
        a = m1;
        b = m2;
    }
    // bellow the line means FRIEND function is allowed to UNKNOWN fuction do anything access with my privt part
    
    friend complex sumcomplex (complex q1, complex q2, complex q3);  
    void printnumber()//this line call is member of class
    {
        cout<<" your number is "<<a<<" + "<<b<<endl;
    }
    // void totalsumnum (complex q1, complex q2, complex q3){
    //     a = q1.a + q2.a + q3.a;
    //     b = q1.b + q2.b + q3.b;
    // }

    void sumnumber()//this line call is member of class
    {
        cout<<" your total calculation number is "<<a<<" + "<<b<<endl;

    }

};

complex sumcomplex(complex q1, complex q2, complex q3){
    complex q4;
    q4.setnumber((q1.a+q2.a+q3.a), (q1.b+q2.b+q3.b));
    return q4;

}


int main(){
    complex c1,c2, c3, sum;
    c1.setnumber(1, 4);
    c1.printnumber();

    c2.setnumber(5, 8);
    c2.printnumber();

    c3.setnumber(3, 9);
    c3.printnumber();
    
    // sum.totalsumnum(c1, c2, c3);
    // sum.sumnumber();

    sum = sumcomplex(c1, c2, c3);
    sum.sumnumber();
    return 0;
}     

/*
PROPERTIES OF FRIEND FUNCTIONS
1. not in the scope in class.
2. can be declared inside public or privet section of the class.
3. it cannot access the member directly by then names and
  need object name.mmber name to access any member.
4.can be invoked without the help of any class.
5. usually contant the object as argument.

*/
