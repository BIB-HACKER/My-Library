#include<iostream>
using namespace std;

class complex{
    int a;
    int b;
    public:
    void setdata(int x1, int x2){
        a = x1;
        b =x2;
    }

    void setdatabysum(complex o1, complex o2){
        a = o1.a + o2.a;
        b = o1.b + o2.b;
    }
    void printnumber(){
        cout<<" your complex number is "<<a<< " + "<<b<< " i "<<endl;
    }
};
int main(){
    complex c1, c2, c3;
    c1.setdata(1, 2);
    c1.printnumber();

    c2.setdata(3, 4);
    c2.printnumber();

    c3.setdatabysum(c1, c2);
    c3.printnumber();
    
    return 0;
}  