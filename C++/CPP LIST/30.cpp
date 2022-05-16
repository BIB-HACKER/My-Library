#include<iostream>
using namespace std;

//******************************* COPY CONSTUCTOR*****************************

class number{
    int a;
    // int b;
    public :
    number(){      /*this called default constructor*/
        a = 0;
    }
    number(int num){    /*this is constructor*/
        a = num;
    }
    
//  when no copy constructor is found, compiler supplies its own copy contructor
    number (number &obj){
        cout<< " copy constructor called!!!!!!"<<endl;
        a = obj.a;
    }

    void display(){
        cout<<" the number for this object is "<< a <<endl;
    }
};
int main(){
    number x(22), y, z(55), z3;
    
    z.display();
    y.display();
    x.display();

    number  z1(x);  //copy constructor invoked
    z1.display();

    z3 = z;   //copy constuctor not called
    z3.display();

    number z2 = z; //copy constructor invoked
    z2.display();
    return 0;
}