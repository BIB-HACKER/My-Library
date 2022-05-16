#include<iostream>
using namespace std;

 class Y; //THIS LINE IS DECLARATION

class X {
    int data;
    public:
    void setvalue(int value){
        data = value;
    }
    friend void ass(X, Y);
};

class Y {
    int non;
    public:
    void setvalue(int value){
        non = value;
    }
      friend void ass(X, Y);
};

void ass(X w1, Y w2){
    cout<<" THIS CLASS MEMBERS X & Y TOTAL SUM VALUE GIVES ME--> "<<w1.data + w2.non<<endl;
}

int main(){
    X w1;
    w1.setvalue(50);

    Y w2;
    w2.setvalue(20);

    ass(w1, w2);    
    return 0;
}