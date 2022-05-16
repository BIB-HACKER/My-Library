#include<iostream>
using namespace std;

// ********************************* Ambiguity Resolution in Inheritance ***********************************

class b
{
    public:
    void say()
    {
        cout << "hello world "<<endl;
    }
};

class d /*: public b */ {
  //  int a;
    public:
    void say()
    {
        cout << "hello my beautiful people "<<endl;
    }
};

int main(){
    
    b v;
    v.say();
    d x;
    x.say();

    return 0;
}