#include<iostream>
using namespace std; 

// ********************************* Ambiguity Resolution in Inheritance ***********************************

class base1{
   public:
   void jym(){
       cout << " how are you? "<<endl;
   }
};

class base2{
     public:
     void jym()
     {
         cout << " kmon acho? "<<endl;
     }
};

class derived : public base1, public base2{
    int a;
    public:
    void jym(){
        base1 :: jym();
    }
};


int main(){
    //Ambibuity
    base1 work1;
    base2 work2;
    work1.jym();    
    work2.jym();
    derived h;
    h.jym();

    return 0;
}