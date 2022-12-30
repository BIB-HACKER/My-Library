#include<iostream>
using namespace std;
//FUNCTION
int reverse(int num){
    
    int copy=num;
    int revnum=0;
    while(num != 0)
    {   // how to reverse number
        int lst_digit=num%10;
        revnum=(revnum*10)+lst_digit;
        num=num/10;
    }
    return revnum;
}

int main()
{
    int num; cin>>num;
    cout<<reverse(num)<<endl;
    cout<<reverse(123)<<endl;
    cout<<reverse(557)<<endl;
    cout<<reverse(1999)<<endl;
    cout<<reverse(0)<<endl;
}