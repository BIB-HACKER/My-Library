#include<iostream>
using namespace std;
int main()
{
    // cout<<"hello world";
    // int variable=20;
    // cout<<variable;
    // int a=10;
    // int b=20;
    // int c=a+b;
    // cout<<c<<en;
    // cout<<1<<endl;
    // cout<<2<<endl;
    // cout<<3<<endl;
    // cout<<4<<endl;
    // cout<<5<<endl;
    // for(int i=1;i<=1000;i++)
    // {
    //     cout<<i;
    // }
    // int i=1;
    // while(i<=1000){
    //     cout<<i;
    //     i++;
    // }
    int num; cin>>num;
    
    int copy=num;
    int revnum=0;
    while(num != 0)
    {
        int lst_digit=num%10;
        revnum=(revnum*10)+lst_digit;
        num=num/10;
    }
    // cout<<revnum<<endl;
    if(copy==revnum)
    {
        cout<<"palindrome number";
    }
    else{
        cout<<"not palindrome";
    }
}