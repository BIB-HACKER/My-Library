#include<iostream>
using namespace std;

//********************************DESTRUCTOR************************************ 

//destructor never takes an argument nor does it return any value
int count = 0;
//when need object and its working, then compiler is called CONSTUCTOR
//and, when don't need a object then compiler is called DESTRUCTOR

class num{
    public:
     num(){
         count++;
         cout<<" this is the time when constructor is called for object number "<<count<<endl;
     }

     ~num(){
         cout<<" this is the time when destructor is called for object number "<<count<<endl;
         count--;
     }
};
int main(){
    cout<<" we are inside our main function"<<endl;
    cout<<" creating first objects"<<endl;
    num n1;
    {
        cout<<" enterig this block"<<endl;
        cout<<" creating tow more object"<<endl;
        num n2, n3;
        cout<<" exiting this block"<<endl;
    }
    cout<<" back to main"<<endl;
    return 0;
}

