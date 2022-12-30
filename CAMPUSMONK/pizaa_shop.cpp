// To prepare a pizza, he needs N items. Each itrems required quantity is denoted by the Ith element of array A.
// He buys each of the N items whoes quantites are denoted by array B i.e. A[i] donates the required quantity of item "I" and B[i] denotes the quantuty availabe charles.

// Given N and arrays A and B, print the maximum number of pizza chrles can make.

#include<iostream>

using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n]={0};
    int b[n]={0};

    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(int i=0;i<n;i++)
    {
        cin>>b[i];
    }
    
    int min=b[0]/a[0];
    for(int i=1;i<n;i++)
    {
        if(min>b[i]/a[i])
        {
            min=(b[i]/a[i]);
        }
    }

    cout<<min;
    return 0;
}