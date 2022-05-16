//************************************OOPs programing******************************************

#include<iostream>
using namespace std;

//**************************CLASSES- public and privet****************************

class employee      // in office a job persion, (like bibhakar)
{
    private:
    int a, b, c;
    public:
    int d, e;
    void setdata(int a100, int b200, int c300); //declaration
    void getdata(){
        cout<<" the value of a is "<<a<<endl;
        cout<<" the value of b is "<<b<<endl;
        cout<<" the value of c is "<<c<<endl;
        cout<<" the value of d is "<<d<<endl;
        cout<<" the value of e is "<<e<<endl;
    }
};

void employee :: setdata(int a100, int b200, int c300){
    a = a100;// this is a data(a100) of job persion and this data is privet
    b = b200;// this is a data(b200) of job persion and this data is privet
    c = c300;// this is a data(c300) of job persion and this data is privet
}

int main(){
    employee bibhakar;
   // bibhakar.a = 22222; // this will throw error, because (A is a privet) 
    bibhakar.d = 2000000;
    bibhakar.e = 10;
    bibhakar.setdata(404, 404, 404);
    bibhakar.getdata();
    return 0;
}