#include<iostream>
using namespace std;
int main()
{
    //input -> int num
    //output -> prime ot not
    int num;
    cin>>num;
    if(num==1)
    {
        cout<<"is neither prime nor a composite number";
        return 0;
    }
    for(int i=2;i<=num-1;i++)
    {
        if(num%i==0)
        {
            cout<<"is not a prime number"<<endl;
            return 0;
        }   
    }
    cout<<"is a prime number"<<endl;
}

