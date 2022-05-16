#include<iostream>
using namespace std;

//****************************construction with default argument*************************************

class simple{
    int data1;
    int data2;
    int data3;
    public:
    simple (int a = 444, int b = 222, int c=333){
        data1 = a;
        data2 = b;
        data3 = c;
    }

    void printdata();

};

void simple :: printdata(){
    cout<<"the value of data1, data2 and data3 is "<<data1<<" , "<<data2<<" and "<<data3<<endl;
}
int main(){
    simple s(1,2);
    s.printdata();

    return 0;
}  