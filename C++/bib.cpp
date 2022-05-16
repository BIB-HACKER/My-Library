#include <iostream>
#include <string>
using namespace std;

int sum(int a, int b)
{
  int c;
  c = a + b;
  return c;
}

class Employee
{
public:
  string name;
  int salary;

  Employee(string name, int salary)
  {
    this->name = name;
    this->salary = salary;
  }

  void printdetails()
  {
    cout << "the name of good boy is " << this->name << " and har salary is " << this->salary << " lacs " << endl;
  }

  void getsecretpassword()
  {
    cout<<"the secret password of employee is "<<this->secretpassword;
  }

private:
  int secretpassword;
};
 
class programar : public empolyee
{
  public:
         int errors;
};

int main()
{

  //int a, b, c;
  //  short love=5;
  //      cout<< "filrugvortkgopetgkrohjhjlove" <<love;

  // int a, b;
  // cout <<"enter first number"<<endl;
  // cin >> a;

  // cout <<"enter second number"<<endl;
  // cin >> b;
  // cout<< "a + b is" <<a+b <<endl;
  // cout <<"a - b is" <<a-b <<endl;
  // cout <<"a * b is" <<a*b <<endl;
  // cout <<"a / b is" <<(float) a/b <<endl;

  // int age;
  // cout<<"enter your age"<<endl;
  // cin>>age;
  // if (age>150)
  // { cout <<"invalid age";
  // }
  // else if (age>=18)
  // {
  //   cout<<"you can vote";
  // }
  // else
  // {
  //   cout <<"you cannot vote";
  // }

  // switch(age)
  // { case 12:
  //      cout <<"you are 12 years old"<<endl;
  //      break;
  //      case 18:
  //      cout<<"you are 18 yeARS OLD"<<endl;
  //      break;

  //      default:
  //      cout <<"you are nither 12 nor 18 years old";

  // }
  // int a, b;
  // cout <<"enter first number"<<endl;
  // cin>>a;

  //  cout<<"enter second number"<<endl;
  //  cin>>b;

  //    cout<<"the function returned "<<sum(a, b);

  // int arr2d[2][3] ={{1,2,3},
  //                    {4,5,6}};

  // for (int i =0; i<2; i++)
  // {
  //   for (int j = 0; j < 3; j++)
  //   {
  //     cout<<"the value at "<<i<<","<<j<<" is "<<arr2d[i][j]<<endl;

  //   }
  // }

  // int a = 343;
  // float b = 8.98;

  // cout <<(float) a/34 <<endl;

  // cout <<() b;

  // string name = "bibhakar";

  // cout <<"the king is "<<name<<endl;
  // cout <<"the power of king "<<name.length()<<endl;
  // cout <<"the king is "<<name.substr(3,5)<<endl;
  // cout <<"the king loves "<<name.substr(0,2)<<endl;

  // int a = 34;
  // int* ptra;
  // ptra = &a;
  // cout<<"the value of a is "<<a<<endl;
  // cout<<"the value of a is "<<*ptra<<endl;
  // cout <<"the adresss of a is "<<&a<<endl;

  // Employee har("BIBHAKAR ", 234, 12345);

  // // har.name = "bibhakar";
  // // har.salary = 1000000;
  // // cout << "the name of good boy is " << har.name << " and har salary is " << har.salary << " lacs " << endl;
  // har.printdetails();
  // har.getsecretpassword();

  return 0;
}