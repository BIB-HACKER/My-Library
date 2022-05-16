#include<iostream>
using namespace std;
//********************************** PROTECTED ACCESS MODIFIER *************************************
class base{
    protected: // private or protected are same but private are not inharitance or protected working on inharitnce 
    int a;
    private:
    int b;

};
/*
for a protected member :
                            public derivation   private derivation  protected derivation
  1. private mumbers          not inherited        not inhereted       not inherited
  2. protected mumbers         protected            private             protected
  3. public mumbers            public               private             protectd
  */              

class derived : protected base{
      

};

int main(){
     base b;
     derived d;
     //cout<<d.a;  //will not work since a is protected in both base as detived class
    return 0;
}