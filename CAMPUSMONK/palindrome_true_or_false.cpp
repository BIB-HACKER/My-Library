// You are given a function which checks if the string is a palindrome or not. A string is called a palindrome if it reads the same from both the ends. it returns 1 if string is a palindrome else 0.

#include<iostream>

using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i]; // a[121,122,221,222]
    }

    bool flag=true;

    for(int i=0;i<(n/2);i++)
    {
        if(a[i]!=a[n-1-i])
        {
            flag=false;
        }
    }

    cout<<flag;
    return 0;
}