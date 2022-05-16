#include<iostream>
using namespace std;

// base class
class employee{
 public :
    int id;
    float salary;
    employee(int inpId){
        id = inpId;
        salary = 101.0;
    }
    employee() {}
};

//drived class syntax
/*
class {{derived-class-name}} : {{visibility-mode}} {{base-class-name}}
{
    class member/methods/etc....
}
NOTE:
1.default visibility mode is private
2.public visibility mode: public members of the base class becomes public members of the drived class
3.private visibility mode: public members of the base class becomes private members of the drived class
4.private member are inherited
*/

//creating a programer class derived from employee base class
//BASE CLASS
class programmer : public employee{
    public:
    int languagecode;
    programmer(int inpId)
    {
        id = inpId;
        languagecode = 7;
    }
    void getdata(){
        cout<<id<<endl;
    }
};


int main()
{
 employee harry(1), papon(2);
 cout<<harry.salary<<endl;   
 cout<<papon.salary<<endl;
 programmer skillF(10);
 cout<<skillF.languagecode<<endl;
 cout<<skillF.id<<endl;
 skillF.getdata();  
    return 0;
}